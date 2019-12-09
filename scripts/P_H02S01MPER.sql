--SELECT * FROM P_H02S01MPER('{"CNRODNI":"56896324","CNOMBRE":"YOSSE", "CSEXO":"F", "CNROCEL":"1564897562", "CEMAIL":"yoss@gmail.com","CESTADO":"A","CNUEVO":"S"}');                                                                                                                            
--PROCEDIMIENTO QUE CREA Y ACTUALIZA RESPONSABLE
SELECT * FROM  S01MPER WHERE cNroDni = '56896324';
CREATE OR REPLACE FUNCTION P_H02S01MPER(text)
  RETURNS text AS
$BODY$
DECLARE
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cNroDni   CHARACTER(8)   	NOT NULL := '';
   p_cNombre   VARCHAR(100)     NOT NULL := '';
   p_cSexo     CHARACTER(1)   	NOT NULL := '';
   p_cNroCel   VARCHAR(12)   	NOT NULL := '';
   p_cEmail    VARCHAR(90)   	NOT NULL := '';
   p_cEstado   CHARACTER(1)   	NOT NULL := '';
   lcNuevo     CHARACTER(1)     NOT NULL := '';
   --VARIABLES LOCALES
   loJson    JSON;
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cNroDni := loJson->>'CNRODNI';
      p_cNombre := loJson->>'CNOMBRE';
      p_cSexo   := loJson->>'CSEXO';
      p_cNroCel := loJson->>'CNROCEL';
      p_cEmail  := loJson->>'CEMAIL';
      p_cEstado := loJson->>'CESTADO';
      lcNuevo   := loJson->>'CNUEVO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   
   --VALIDANDO EMAIL TIENE @ Y .
   IF p_cEmail NOT LIKE '%@%.%' THEN
      RETURN '{"ERROR": "ERROR DE VALIDACIÓN DEL CORREO ELECTRÓNICO, INGRESAR UNO VÁLIDO"}';
   END IF;
   --VALIDANDO NRO CELULAR SOLO CONTIENE NUMEROS
   IF p_cNroCel !~ '^[0-9]*$' THEN
      RETURN '{"ERROR": "ERROR DE VALIDACIÓN DEL NÚMERO DE CELULAR, INGRESAR UNO VÁLIDO"}';
   END IF;
   --REGISTRANDO A PERSONA
   BEGIN 
	 IF lcNuevo = 'S' THEN 
      -- NUEVO RESPONSABLE
		--VALIDANDO DNI NO ESTÁ REGISTRADO
	   IF EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cNroDni) THEN
	      RETURN '{"ERROR": "DNI DE PERSONA YA EXISTE, NO PUEDE SER INGRESADO NUEVAMENTE"}';
	   END IF;
	   INSERT INTO S01MPER (cNroDni, cEstado, cNombre, cSexo, cNroCel, cEmail, cClave, cUsuCod, tModifi) 
	   VALUES (p_cNroDni, 'A', p_cNombre, p_cSexo, p_cNroCel, p_cEmail, TRIM(ENCODE(DIGEST(p_cNroDni, 'sha512'), 'hex')), 'U666', NOW());
	 ELSE
	 ----ACTALIZA DATOS DE LA PERSONA 
		UPDATE S01MPER SET cNombre=p_cNombre, cSexo=p_cSexo, cNroCel=p_cNroCel, cEmail=p_cEmail, cEstado=p_cEstado, tModifi=NOW() WHERE cNroDni=p_cNroDni;
	 END IF;	 
   EXCEPTION WHEN OTHERS THEN 
      RETURN '{"ERROR": "ERROR AL INGRESAR/ACTUALIZAR RESPONSABLE, COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;