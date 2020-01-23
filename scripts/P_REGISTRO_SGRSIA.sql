--SELECT * FROM P_REGISTRO_SGRSIA('{"CNRODNI":"72565894","CNOMBRE":"YOSS", "CSEXO":"F", "CNROCEL":"1564897562", "CEMAIL":"yoss@gmail.com"}');
CREATE OR REPLACE FUNCTION P_REGISTRO_SGRSIA(text)
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
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   --VALIDANDO DNI NO ESTÁ REGISTRADO
   IF EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cNroDni) THEN
      RETURN '{"ERROR": "DNI DE PERSONA YA EXISTE, NO PUEDE SER REGISTRADO NUEVAMENTE"}';
   END IF;
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
      INSERT INTO S01MPER (cNroDni, cEstado, cNombre, cSexo, cNroCel, cEmail, cClave, cUsuCod, tModifi,cTipo) 
            VALUES (p_cNroDni, 'A', p_cNombre, p_cSexo, p_cNroCel, p_cEmail, TRIM(ENCODE(DIGEST(p_cNroDni, 'sha512'), 'hex')), 'U666', NOW(),'N');
   EXCEPTION WHEN OTHERS THEN 
      RETURN '{"ERROR": "ERROR AL REGISTRAR A LA PERSONA, COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
