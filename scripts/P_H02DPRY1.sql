CREATE OR REPLACE FUNCTION public.p_h02dpry1(text)
  RETURNS text AS
$BODY$
DECLARE
   --PROCEDIMENTO QUE APRUEBA DETALLE DE PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_nSerial  INTEGER       NOT NULL := 0;
   p_cCodigo  CHARACTER(6);    --NOT NULL := '';
   p_cNroDniAud  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1);
   p_tFecRev  TIMESTAMP;
   p_mObserv  TEXT;           
   p_cDniNro  CHARACTER(8);    --NOT NULL := '';
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(8);
   lcmObserv text;
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_nSerial := loJson->>'NSERIAL';
      p_cCodigo := loJson->>'CCODIGO';
      p_cNroDniAud := loJson->>'CNRODNIAUD';
      p_mObserv := loJson->>'MOBSERV';
      p_tFecRev := loJson->>'TFECREV';
      p_cDniNro := loJson->>'CDNINRO';
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
   IF NOT EXISTS (SELECT cNroDniAud FROM H02MPRY WHERE cNroDniAud = p_cNroDniAud) THEN
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
   select mobserv into lcmObserv from h02dpry1 WHERE nSerial = p_nSerial;
   /*IF EXISTS (select mobserv from h02dpry1 WHERE nSerial = p_nSerial) THEN
	select mobserv into lcmObserv from h02dpry1 WHERE nSerial = p_nSerial;
	UPDATE H02DPRY1 SET cEstado = 'O', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=lcmObserv||','||p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = CAST (p_nSerial AS INTEGER);
   ELSE
	UPDATE H02DPRY1 SET cEstado = 'O', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = CAST (p_nSerial AS INTEGER);
   END IF;*/
   IF  lcmObserv is NOT NULL THEN
	select mobserv into lcmObserv from h02dpry1 WHERE nSerial = p_nSerial;
	UPDATE H02DPRY1 SET cEstado = 'A', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=lcmObserv||','||p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = CAST (p_nSerial AS INTEGER);
   ELSE
	UPDATE H02DPRY1 SET cEstado = 'A', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = CAST (p_nSerial AS INTEGER);
   END IF;
   --UPDATE H02DPRY1 SET cEstado = 'A', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=lcmObserv||','||p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = p_nSerial;
   RETURN '{"OK": "OK"}';
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.p_h02dpry1(text)
  OWNER TO postgres;