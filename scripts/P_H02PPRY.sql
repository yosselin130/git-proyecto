--BEGIN;SELECT P_H02PPRY('{"CCODIGO":"*","CIDPROY":"00001","CCODREQ":"000001","CNRODNI":"47289024", "CESTADO":"P"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;
--select * from H02PPRY
SELECT * FROM H02PPRY
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
      --p_cDniNro := loJson->>'CDNINRO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
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
      /*ELS
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
         IF NOT EXISTS (SELECT cDniRes FROM H02MPRY WHERE cDniRes = p_cDniRes AND p_cCodigo = p_p_cCodigo) THEN
            RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
         END IF;
         lcCodigo := p_cCodigo;
         UPDATE H02MPRY SET cDescri=p_cDescri, cDniRes=p_cDniRes, cDniNro=p_cDniNro, tModifi=NOW() WHERE cCodigo=lcCodigo;*/
      END IF;
   --EXCEPTION WHEN OTHERS THEN 
     -- RETURN '{"ERROR": "ERROR AL ASIGNAR UN RESPONSABLE-REQUISITO-PROYECTO , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $$ LANGUAGE plpgsql VOLATILE;