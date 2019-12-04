--BEGIN;SELECT P_S01PAUD('{"CCODAUD":"000021","CIDPROY":"P0002","CNRODNI":"72518755","CDNINRO":"72518755"}');
CREATE OR REPLACE FUNCTION P_H02PAUD(text)
   RETURNS text AS $$
DECLARE
--PROCEDIMENTO QUE CREA Y ACTUALIZA UN AUDITOR 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cCodAud  CHARACTER(6)   	NOT NULL := '';
   p_cIdProy  CHARACTER(5)   	NOT NULL := '';
   p_cNroDni  CHARACTER(8)   	NOT NULL := '';
   p_cDniNro  CHARACTER(8)   	NOT NULL := '';
 
   --VARIABLES LOCALES
   loJson    JSON;
   lcCodAud   CHARACTER(6);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cCodAud := loJson->>'CCODAUD';
      p_cIdProy := loJson->>'CIDPROY';
      p_cNroDni := loJson->>'CNRODNI';
      p_cDniNro := loJson->>'CDNINRO';
      
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   -- VALIDA DNI DE AUDITOR
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniNro AND cEstado = 'A') THEN
      RETURN '{"ERROR": "USUARIO NO EXISTE O NO TIENE LOS PERMISOS SUFICIENTES"}';
   END IF;
   BEGIN
      IF p_cCodAud='*' THEN 
      -- NUEVO AUDITOR
         SELECT MAX(cCodAud) INTO lcCodAud FROM H02PAUD;
         IF lcCodAud ISNULL THEN
            lcCodAud := '000001';
         END IF;
         lcCodAud := TRIM(TO_CHAR(lcCodAud::INT + 1, '000001'));
         INSERT INTO H02PAUD (cCodAud, cEstado, cIdProy, cNroDni, cDniNro, tModifi) VALUES 
               (lcCodAud, 'A',p_cIdProy, p_cNroDni, p_cDniNro ,NOW());
      ELSE
         -- ACTUALIZA AUDITOR EXISTENTE
         UPDATE H02PAUD SET cIdProy = p_cIdProy, cNroDni = p_cNroDni, cDniNro = p_cDniNro, tModifi = NOW() WHERE cCodAud = p_cCodAud;
      END IF;
   EXCEPTION WHEN OTHERS THEN 
	RETURN '{"ERROR": "ERROR AL CREAR/ACTUALIZAR UN AUDITOR , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;


select * from h02mpry;
select * from H02PAUD;

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('P0002', 'A', 'MODULO GESTION CALIDAD', '72518755', '72518755', '"2019-10-09 08:05:56.822106"');