--BEGIN;SELECT P_S01DPRY_1('{"NSERIAL":"2","CCODIGO":"000002", "CCODAUD":"A00002"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;
select * from h02paud;
SELECT * FROM H02DPRY
SELECT * FROM H02PPRY
CREATE OR REPLACE FUNCTION P_H02DPRY1(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE APRUEBA DETALLE DE PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_nSerial  CHARACTER(1)    NOT NULL := '';
   p_cCodigo  CHARACTER(6);    --NOT NULL := '';
   p_cCodAud  CHARACTER(6)    NOT NULL := '';
   p_cEstado  CHARACTER(1);
   p_cDniNro  CHARACTER(8);
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(8);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_nSerial := loJson->>'NSERIAL';
      p_cCodigo := loJson->>'CCODIGO';
      p_cCodAud := loJson->>'CCODAUD';
      --p_cEstado := loJson->>'CESTADO';
      --p_cEstado := loJson->>'CESTADO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   --IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniNro AND cEstado = 'A') THEN
   --   RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE O NO ESTÁ ACTIVO"}';
   --END IF;
   -- VALIDA QUE USUARIO PERTENEZCA A PROYECTO
   --SELECT cDniRes INTO p_cDniRes FROM H02MPRY WHERE cIdProy = p_cIdProy
   --IF p_cDniRes IS NOT cDniRes THEN
    --  RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE EN PROYECTO O NO ESTÁ ACTIVO"}';
   --END IF;
   -- Valida AUDITOR
   IF NOT EXISTS (SELECT cCodAud FROM H02PAUD WHERE cCodAud = p_cCodAud) THEN
      RETURN '{"ERROR": "EL CODIGO DEL AUDITOR NO EXISTE"}';
   END IF;
     -- Valida REQUISITO
   SELECT cEstado INTO p_cEstado  FROM H02MREQ WHERE cCodReq = p_cCodigo;
   IF NOT EXISTS (SELECT cCodReq FROM H02MREQ WHERE cCodReq = p_cCodigo) THEN
      RETURN '{"ERROR": "EL CODIGO DEL REQUISITO NO EXISTE"}';
   END IF;
      -- Valida Estado de estado de requisitos-proyecto
      SELECT cEstado INTO p_cEstado FROM H02PPRY WHERE cCodigo = p_cCodigo;
      IF p_cEstado = 'X' AND  p_cEstado =  'O' THEN
         RETURN '{"ERROR": "PUENTE PROYECTO YA FUE ANUALDO Y OBSERVADO, NO SE PUEDE APROBAR"}';
      END IF;
      -- Valida Estado de estado de detalle-proyecto
      SELECT cEstado INTO p_cEstado FROM H02DPRY WHERE nSerial = p_nSerial AND cCodigo = p_cCodigo;
      IF p_cEstado = 'O' THEN
         RETURN '{"ERROR": "REQUISITO YA FUE OBSERVADO, NO SE PUEDE APROBAR"}';
      END IF;
   UPDATE H02DPRY SET cEstado = 'A', cCodAud = p_cCodAud, tModifi = NOW() WHERE nSerial = p_nSerial;
   RETURN '{"OK": "OK"}';
END $$ LANGUAGE plpgsql VOLATILE;

--UPDATEEE
UPDATE h02dpry set cEstado=''
  where nSerial='2';