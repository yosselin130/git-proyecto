--SELECT * FROM P_LOGIN_TEST('{"CNRODNI":"47289024","CCLAVE":"47289024"}');


SELECT P_LOGIN_SGRSIA('{"CNRODNI": "72518755", "CCLAVE": "72518755"}')

select * from S01MPER where cnrodni='72518755'
CREATE OR REPLACE FUNCTION public.p_login_sgrsia(text)
  RETURNS text AS
$BODY$
DECLARE
   p_cData   ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cNroDni  CHARACTER(8)   NOT NULL := '';
   p_cClave   CHARACTER(128) NOT NULL := '';
   --VARIABLES LOCALES
   loJson    JSON;
   lcEstado  CHARACTER(1);
   lcNombre  CHARACTER(200);
   lcCodUsu  CHARACTER(4);
   lcCenCos  CHARACTER(10);
   lcDesCco  CHARACTER(100)         := 'SIN ASIGNAR';
   lcCargo   CHARACTER(3);
   lcNivel   CHARACTER(2);
   lcPrefij  CHARACTER(1);
   lcClave   CHARACTER(128);
   lcTipo    CHARACTER(1);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cNroDni := loJson->>'CNRODNI';
      p_cClave  := loJson->>'CCLAVE';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   SELECT cNombre INTO lcNombre FROM S01MPER WHERE cNroDni = p_cNroDni;
   IF lcNombre ISNULL THEN 
      RETURN '{"ERROR": "USUARIO INCORRECTO, DNI  NO ES CORRECTO"}';
   END IF;
   -- Usuario
   lcClave := TRIM(ENCODE(DIGEST(p_cClave, 'sha512'), 'hex'));
   SELECT cNombre, cTipo INTO lcNombre,lcTipo FROM S01MPER WHERE cNroDni = p_cNroDni AND cClave = lcClave AND cEstado = 'A';
   IF lcNombre ISNULL THEN 
      RETURN '{"ERROR": "USUARIO O CLAVE INCORRECTOS"}';
   END IF;
   SELECT cEstado, cNombre, cTipo INTO lcEstado, lcNombre,lcTipo FROM S01MPER WHERE cNroDni = p_cNroDni AND cEstado = 'A';
   IF lcEstado ISNULL THEN
      RETURN '{"ERROR": "USUARIO NO ESTÁ ACTIVO"}';
   END IF;
   RETURN '{"CNOMBRE":"'||lcNombre||'","CNRODNI":"'||p_cNroDni||'","CTIPO":"'||lcTipo||'"}';
END $BODY$
  LANGUAGE plpgsql STABLE
  COST 100;
ALTER FUNCTION public.p_login_sgrsia(text)
  OWNER TO postgres;