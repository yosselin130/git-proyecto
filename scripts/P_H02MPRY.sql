--BEGIN;SELECT P_S01MPRY('{"CIDPROY":"*","CDESCRI":"TEST1222","CDNIRES":"47289024","CDNINRO":"47289024"}');
--BEGIN;SELECT P_S01MPRY('{"CIDPROY":"00001","CDESCRI":"TEST1222","CDNIRES":"47289024","CDNINRO":"47289024"}');
SELECT P_S01MPRY('{"CDNIRES": "72518755", "CIDPROY": " ", "CDESCRI": "MODULO APP"}');

SELECT P_S01MPRY('{"CIDPROY": "*", "CDESCRI": "modulo app", "CDNIRES": "47289024"}');
SELECT cNroDni FROM S01MPER WHERE cNroDni = '72518755' AND cEstado = 'A'
--SELECT * FROM H02MPRY
CREATE OR REPLACE FUNCTION P_H02MPRY(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE CREA Y ACTUALIZA UN PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cIdProy  CHARACTER(5)    NOT NULL := '';
   p_cDescri  VARCHAR(200)    NOT NULL := '';
   p_cDniRes  CHARACTER(8)    NOT NULL := '';
   p_cDniNro  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1)    NOT NULL := '';
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(5);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cIdProy := loJson->>'CIDPROY';
      p_cDescri := loJson->>'CDESCRI';
      p_cDniRes := loJson->>'CDNIRES';
      p_cEstado := loJson->>'CESTADO';
     -- p_cDniNro := loJson->>'CDNINRO';
   --EXCEPTION WHEN OTHERS THEN
     -- RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
    -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniRes AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
   END IF;
   BEGIN
      IF p_cIdProy='*' THEN 
      -- NUEVO PROYECTO
         SELECT MAX(cIdProy) INTO lcIdProy FROM H02MPRY;
         IF lcIdProy ISNULL THEN
            lcIdProy := '00000';
         END IF;
         lcIdProy := TRIM(TO_CHAR(lcIdProy::INT + 1, '00000'));
         INSERT INTO H02MPRY (cIdProy, cEstado, cDescri, cDniRes, cDniNro, tModifi) VALUES 
                (lcIdProy,'A', p_cDescri, p_cDniRes,p_cDniRes ,NOW());
      ELSE
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
         IF NOT EXISTS (SELECT cDniRes FROM H02MPRY WHERE cDniRes = p_cDniRes AND cIdProy = p_cIdProy) THEN
            RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO PERTENECE AL PROYECTO"}';
         END IF;
         lcIdProy := p_cIdProy;
         UPDATE H02MPRY SET cDescri=p_cDescri, cDniRes=p_cDniRes, cEstado=p_cEstado, tModifi=NOW() WHERE cIdProy=lcIdProy;
      END IF;
  -- EXCEPTION WHEN OTHERS THEN 
    --  RETURN '{"ERROR": "ERROR AL CREAR/ACTUALIZAR UN PROYECTO, COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;