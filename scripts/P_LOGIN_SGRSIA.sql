--SELECT * FROM P_LOGIN_TEST('{"CNRODNI":"47289024","CCLAVE":"47289024"}');
CREATE OR REPLACE FUNCTION P_LOGIN_SGRSIA(text)
   RETURNS text AS $$
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
   SELECT cNombre INTO lcNombre FROM S01MPER WHERE cNroDni = p_cNroDni AND cClave = lcClave AND cEstado = 'A';
   IF lcNombre ISNULL THEN 
      RETURN '{"ERROR": "USUARIO O CLAVE INCORRECTOS"}';
   END IF;
   SELECT cEstado, cNombre INTO lcEstado, lcNombre FROM S01MPER WHERE cNroDni = p_cNroDni AND cEstado = 'A';
   IF lcEstado ISNULL THEN
      RETURN '{"ERROR": "USUARIO NO ESTÁ ACTIVO"}';
   END IF;
   RETURN '{"CNOMBRE":"'||lcNombre||'","CNRODNI":"'||p_cNroDni||'"}';
END $$ LANGUAGE plpgsql STABLE;