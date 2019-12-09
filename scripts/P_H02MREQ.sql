--BEGIN;SELECT P_H02MREQ('{"CCODREQ":"*","CDESCRI":"TEST1222","CESTADO":"A", "CDNINRO":"72518755"}');

CREATE OR REPLACE FUNCTION P_H02MREQ(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE CREA Y ACTUALIZA UN REQUERIMIENTO
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cCodReq  CHARACTER(6)   	NOT NULL := '';
   p_cDescri  VARCHAR(150)    	NOT NULL := '';
  -- p_cTipo    CHARACTER(1)   	NOT NULL := '';
   p_cDniNro  CHARACTER(8)   	NOT NULL := '';
   p_cEstado  CHARACTER(1)   	NOT NULL := '';
   --VARIABLES LOCALES
   loJson     JSON;
   lcCodReq   CHARACTER(6);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cCodReq := loJson->>'CCODREQ';
      p_cDescri := loJson->>'CDESCRI';
      p_cEstado := loJson->>'CESTADO';
     -- p_cTipo   := loJson->>'CTIPO';
      p_cDniNro := loJson->>'CDNINRO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   -- VALIDA DNI DE RESPONSABLE DEL REQUISITO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniNro AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
   END IF;
   --VALIDAR QUE SI EL TIPO DICE INDECOPI NO DEBE CREARSE Y/O EDITARSE
   --IF p_cTipo='I' THEN
    --  RETURN '{"ERROR": "NO SE PUEDE INSERTAR/MDIFICAR PORQUE ES UN REQUISITO DE INDECOPI"}'; 
   --END IF;
   --*******
   BEGIN
	   IF p_cCodReq='*' THEN 
	      -- NUEVO REQUISITO
	      SELECT MAX(cCodReq) INTO lcCodReq FROM H02MREQ;
	      IF lcCodReq ISNULL THEN
		 lcCodReq := '000000';
	      END IF;
	      lcCodReq := TRIM(TO_CHAR(lcCodReq::INT + 1, '000000'));
	      INSERT INTO H02MREQ (cCodReq, cEstado, cDescri, cTipo, cDniNro, tModifi) VALUES 
				  (lcCodReq, p_cEstado, p_cDescri, 'A' , p_cDniNro, NOW());
	   ELSE
	      UPDATE H02MREQ SET cDescri=p_cDescri, cDniNro=p_cDniNro, tModifi=NOW() WHERE cCodReq = p_cCodReq;
	   END IF;
   EXCEPTION WHEN OTHERS THEN 
	RETURN '{"ERROR": "ERROR AL CREAR O ACTUALIZAR UN REQUISITO , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;