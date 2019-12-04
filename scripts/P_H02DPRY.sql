SELECT * FROM H02PPRY
--BEGIN;SELECT P_S01DPRY('{"NSERIAL":"*","CCODIGO":"000001","CCODAUD":"000021","CESTADO":"A", "TFECREV": "2019-10-13 18:21:16", "MOBSERV":"APROBADO", "CDNINRO":"72518755"}');
--BEGIN;SELECT P_S01PPRY('{"CCODIGO":"*","CIDPROY":"P0001","CCODREQ":"000001","CNRODNI":"47289024", "CESTADO":"P", "DNINRO":"72518755"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;
select * from h02paud;
SELECT * FROM H02DPRY

CREATE OR REPLACE FUNCTION P_H02DPRY(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE CREA DETALLE PROYECTO
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_nSerial  CHARACTER(1)    NOT NULL := '';
   p_cCodigo  CHARACTER(6)    NOT NULL := '';
   p_cCodAud  CHARACTER(6)    NOT NULL := '';
   p_cEstado  CHARACTER(1)    NOT NULL := '';
   p_tFecRev  TIMESTAMP;
   p_mObserv  TEXT            NOT NULL := '';
   p_cDniNro  CHARACTER(8)    NOT NULL := '';
  

   --VARIABLES LOCALES
   loJson    JSON;
   lnSerial   CHARACTER(1);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_nSerial := loJson->>'NSERIAL';
      p_cCodigo := loJson->>'CCODIGO';
      p_cCodAud := loJson->>'CCODAUD';
      p_cEstado := loJson->>'CESTADO';
      p_tFecRev := loJson->>'TFECREV';
      p_mObserv := loJson->>'MOBSERV';
      p_cDniNro := loJson->>'CDNINRO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
    -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniNro AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
   END IF;
   -- VALIDA REQUISITO
   IF NOT EXISTS (SELECT cCodReq FROM H02MREQ WHERE cCodReq = p_cCodigo AND cEstado = 'A') THEN
      RETURN '{"ERROR": "REQUISITO NO EXISTE, O NO TIENE EL ESTADO CORRECTO"}';
   END IF;
    -- VALIDA AUDITOR
   IF NOT EXISTS (SELECT cCodAud FROM H02PAUD WHERE cCodAud = p_cCodAud AND cEstado = 'A' ) THEN
      RETURN '{"ERROR": "CODIGO DEL AUDITOR NO EXISTE,O NO TIENE EL ESTADO CORRECTO"}';
   END IF;
   BEGIN
      IF p_nSerial='*' THEN 
      -- NUEVO PUENTE DE PROYECTO
         SELECT MAX(p_nSerial) INTO lnSerial FROM H02DPRY;
         IF lnSerial ISNULL THEN
            lnSerial := '0';
         END IF;
         lnSerial := TRIM(TO_CHAR(lnSerial::INT + 1, '0'));
         INSERT INTO H02DPRY (nSerial, cCodigo, cCodAud, cEstado, tFecRev, mObserv, cDniNro, tModifi) VALUES 
                (lnSerial,p_cCodigo, p_cCodAud, p_cEstado, p_tFecRev, p_mObserv, p_cDniNro ,NOW());
      /*ELS
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
         IF NOT EXISTS (SELECT cDniRes FROM H02MPRY WHERE cDniRes = p_cDniRes AND p_cCodigo = p_p_cCodigo) THEN
            RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
         END IF;
         lcCodigo := p_cCodigo;
         UPDATE H02MPRY SET cDescri=p_cDescri, cDniRes=p_cDniRes, cDniNro=p_cDniNro, tModifi=NOW() WHERE cCodigo=lcCodigo;*/
      END IF;
   EXCEPTION WHEN OTHERS THEN 
      RETURN '{"ERROR": "ERROR AL ASIGNAR UN RESPONSABLE-REQUISITO-PROYECTO , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;