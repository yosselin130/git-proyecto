
SELECT p_h02ppry_ed('{"CCODREQ": "000037", "CCODIGO": "*", "CESTADO": "P", "CRESPONSABLE": "", "CNRODNI": "72518755", "CIDPROY": "00026", "CDESCRI": "PRUEBA12"}')

SELECT p_h02ppry_ed('{"CDESCRI": "MODULO PRUEBAS 123", "CCODREQ": "000038", "CNRODNI": "72518755", "CIDPROY": "00025", "CESTADO": "P", "CRESPONSABLE": "", "CCODIGO": "*"}')

CREATE OR REPLACE FUNCTION public.p_h02ppry_ed(text)
  RETURNS text AS
$BODY$
DECLARE
   --PROCEDIMENTO QUE CREA PUENTE PROYECTO-REQUSITO- INTEGRANTE 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cCodigo  CHARACTER(6)    NOT NULL := '';
   p_cIdProy  CHARACTER(5)    NOT NULL := '';
   p_cCodReq  CHARACTER(6)    NOT NULL := '';
   p_cNroDni  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1)    NOT NULL := '';
   p_cArchivo CHARACTER(255);
   p_cExtension CHARACTER(5);
   p_tFecSub  TIMESTAMP;
   p_minfoad  TEXT;
   p_cNroDniAud CHARACTER(8);
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
                
         --INSERCCION DPRY
         SELECT cNroDniAud into p_cNroDniAud FROM H02MPRY where cIdProy=p_cIdProy;
         INSERT INTO H02DPRY1 (cCodigo, cNroDniAud, cEstado, tFecRev, mObserv, cDniNro, tModifi) VALUES 
                (p_cCodReq, p_cNroDniAud, 'A', NULL, NULL, p_cNroDni ,NOW());
      ELSE
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
           UPDATE H02PPRY SET cIdProy=p_cIdProy, cCodReq=p_cCodReq, cNroDni=p_cNroDni,cEstado=p_cEstado, minfoad=p_minfoad,carchivo=p_cArchivo, cextension=p_cExtension, tFecSub=p_tFecSub,tModifi=NOW() WHERE cCodigo=p_cCodigo;
      END IF;
   --EXCEPTION WHEN OTHERS THEN 
     -- RETURN '{"ERROR": "ERROR AL ASIGNAR UN RESPONSABLE-REQUISITO-PROYECTO , COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.p_h02ppry_ed(text)
  OWNER TO postgres;