SELECT P_H02DPRY2('{"CCODAUD": "000024", "CESTADO": "A", "CDESCRIPCION": "DISE\u00d1O GENERAL DEL SISTEMA", "CDNINRO": "72518755", "CCODIGO": "000006", "TFECREV": "2020-01-20",
 "NSERIAL": "4", "RESPONSABLE": "VILLANUEVA ROSAS GLENNY DORA", "MOBSERV": "DISE\u00d1O GENERAL DEL SISTEMA"}')



 --BEGIN;SELECT P_S01DPRY_2('{"NSERIAL":"2","CCODIGO":"000002", "CCODAUD":"A00002", "MOBSERV":"OBSERVADO"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;

--SELECT P_S01DPRY_2{'CCODIGO': '000004', 'CCODAUD': '000005', 'RESPONSABLE': 'MEDINA HUAMANI MIGUEL ANGEL', 'TFECREV': '2019-12-17', 'CDESCRIPCION': 'PRUEBAS DE AMBIENTE', 'NSERIAL': '4', 'MOBSERV': 'JKJHKH', 'CDNINRO': '47289024', 'CESTADO': 'O'}
select * from h02paud;
SELECT * FROM H02DPRY1
SELECT * FROM H02PPRY

SELECT P_H02DPRY2('{"CESTADO": "A", "RESPONSABLE": "PERALES BARRIOS YOSSELIN VANESSA", "MOBSERV": "sdasd", "TFECREV": "2020-01-26", "CDESCRIPCION": "PRUEBA9", "CCODAUD": "72518755", 
"CCODIGO": "000041", "CDNINRO": "72518755", "NSERIAL": "11"}')

CREATE OR REPLACE FUNCTION P_H02DPRY2(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE OBSERVA DETALLE DE PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   --p_nSerial=:CAST(p_nSerial AS INTEGER) ;
   p_nSerial INTEGER NOT NULL := 0;
   --select cast(nSerial as INTEGER) FROM H02DPRY1;
   p_cCodigo  CHARACTER(6);    --NOT NULL := '';
   p_cNroDniAud  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1);
   p_tFecRev  TIMESTAMP;
   p_mObserv  TEXT;        
   p_cDniNro  CHARACTER(8);
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(8);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_nSerial := loJson->>'NSERIAL';
      p_cCodigo := loJson->>'CCODIGO';
      p_cNroDniAud := loJson->>'CNRODNIAUD';
      p_mObserv := loJson->>'MOBSERV';
      p_tFecRev := loJson->>'TFECREV';
      p_mObserv := loJson->>'MOBSERV';
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
      IF p_cEstado = 'X' AND  p_cEstado =  'A' THEN
         RETURN '{"ERROR": "PUENTE PROYECTO YA FUE AUDITADO O ANULADO, NO SE PUEDE OBSERVAR"}';
      END IF;
   UPDATE H02DPRY1 SET cEstado = 'O', cNroDniAud = p_cNroDniAud,tFecRev=p_tFecRev,mObserv=p_mObserv,cDniNro=p_cDniNro,tModifi = NOW() WHERE nSerial = CAST (p_nSerial AS INTEGER);
   RETURN '{"OK": "OK"}';
END $$ LANGUAGE plpgsql VOLATILE;

--UPDATEEE
UPDATE h02dpry set cEstado='A'
  where nSerial='4';


UPDATE h02dpry set mObserv=''
  where nSerial='2';



 select CAST (nserial AS INTEGER) from H02DPRY1 ;