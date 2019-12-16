--BEGIN;SELECT P_H02PPRY('{"CCODIGO":"*","CIDPROY":"00001","CCODREQ":"000001","CNRODNI":"47289024", "CESTADO":"P"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;
--select * from H02PPRY
SELECT * FROM H02PPRY

SELECT P_H02PPRY('{"CCODIGO": "000003", "CCODREQ": "00001", "TFECSUB": "2019-12-16", "CESTADO": "A", "CDESCRIPCION": "DNI LEGALIZADOS", "CRESPONSABLE": "PERALES BARRIOS YOSSELIN VANESSA", "CNRODNI": "72518755", "CIDPROY": "00002"}')

SELECT cCodReq FROM H02MREQ WHERE cCodReq = '000001' AND cEstado = 'A'
 
CREATE OR REPLACE FUNCTION P_H02PPRY(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE CREA PUENTE PROYECTO-REQUSITO- INTEGRANTE 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cCodigo  CHARACTER(6)    NOT NULL := '';
   p_cIdProy  CHARACTER(5)    NOT NULL := '';
   p_cCodReq  CHARACTER(6)    NOT NULL := '';
   p_cNroDni  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1)    NOT NULL := '';
   p_cArchivo CHARACTER(6);
   p_cExtension CHARACTER(5);
   p_tFecSub  TIMESTAMP;
   p_minfoad  TEXT;
   --p_cDniNro  CHARACTER(8)    NOT NULL := '';
 
   --VARIABLES LOCALES
   loJson    JSON;
   lcCodigo   CHARACTER(6);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cCodigo := loJson->>'CCODIGO';
      p_cIdProy := loJson->>'CIDPROY';
      p_cCodReq := loJson->>'CCODREQ';
      p_cNroDni := loJson->>'CNRODNI';
      p_cEstado := loJson->>'CESTADO';
      p_cArchivo := loJson->>'CARCHIVO';
      p_cExtension := loJson->>'CEXTENSION';
      p_tFecSub := loJson->>'TFECSUB';
      p_minfoad := loJson->>'MINFOAD';
      --p_cDniNro := loJson->>'CDNINRO';
   --EXCEPTION WHEN OTHERS THEN
      --RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
    -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cNroDni AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
   END IF;
    -- VALIDA PROYECTO
   IF NOT EXISTS (SELECT cIdProy FROM H02MPRY WHERE cIdProy = p_cIdProy AND cEstado = 'A') THEN
      RETURN '{"ERROR": "PROYECTO NO EXISTE"}';
   END IF;
   -- VALIDA REQUISITO
   IF NOT EXISTS (SELECT cCodReq FROM H02MREQ WHERE cCodReq = p_cCodReq AND cEstado = 'A') THEN
      RETURN '{"ERROR": "REQUISITO NO EXISTE, O NO TIENE EL ESTADO CORRECTO"}';
   END IF;
   BEGIN
      IF p_cCodigo='*' THEN 
      -- NUEVO PUENTE DE PROYECTO
         SELECT MAX(cCodigo) INTO lcCodigo FROM H02PPRY;
         IF lcCodigo ISNULL THEN
            lcCodigo := '00000';
         END IF;
         lcCodigo := TRIM(TO_CHAR(lcCodigo::INT + 1, '000000'));
         INSERT INTO H02PPRY (cCodigo, cIdProy, cCodReq, cNroDni, cEstado, cDniNro, tModifi) VALUES 
                (lcCodigo,p_cIdProy, p_cCodReq, p_cNroDni, p_cEstado, p_cNroDni ,NOW());
      ELSE
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
           UPDATE H02PPRY SET cIdProy=p_cIdProy, cCodReq=p_cCodReq, cDniNro=p_cNroDni,cEstado='E', minfoad=p_minfoad,carchivo=p_cArchivo, cextension=p_cExtension, tFecSub=p_tFecSub,tModifi=NOW() WHERE cCodigo=p_cCodigo;
      END IF;
   --EXCEPTION WHEN OTHERS THEN 
     -- RETURN '{"ERROR": "ERROR AL ASIGNAR UN RESPONSABLE-REQUISITO-PROYECTO , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;