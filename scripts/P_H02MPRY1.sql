--BEGIN;SELECT P_S01MPRY_1('{"CIDPROY":"P0003","CDNIRES":"72518755"}');
select * from H02MPRY;
CREATE OR REPLACE FUNCTION P_H02MPRY1(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE ANULA UN PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cIdProy  CHARACTER(5)    NOT NULL := '';
   p_cDniRes  CHARACTER(8)    ;--NOT NULL := '';
   p_cEstado  CHARACTER(1);
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy  CHARACTER(8);
   lcDniRes  CHARACTER(8);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cIdProy := loJson->>'CIDPROY';
      p_cDniRes := loJson->>'CDNIRES';
      --p_cEstado := loJson->>'CESTADO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniRes AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE O NO ESTÁ ACTIVO"}';
   END IF;
   -- VALIDA QUE USUARIO PERTENEZCA A PROYECTO
   SELECT cDniRes INTO lcDniRes FROM H02MPRY WHERE cIdProy = p_cIdProy;
   IF p_cDniRes != lcDniRes THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE EN PROYECTO O NO ESTÁ ACTIVO"}';
   END IF;
   -- Valida PROYECTO
   SELECT cEstado, cDniRes INTO p_cEstado, p_cDniRes FROM H02MPRY WHERE cIdProy = p_cIdProy;
   IF NOT EXISTS (SELECT cIdProy FROM H02MPRY WHERE cIdProy = p_cIdProy) THEN
      RETURN '{"ERROR": "EL CODIGO DEL PROYECTO NO EXISTE"}';
   ELSIF NOT p_cEstado IN ('A', 'F', 'X') THEN   
      RETURN '{"ERROR": "ESTADO DEL PROYECTO NO PERMITE ANULAR"}';
   END IF;
   -- Valida Estado de estado de requisitos-proyecto
   SELECT cEstado INTO p_cEstado FROM H02PPRY WHERE cIdProy = p_cIdProy;
   IF p_cEstado = 'A' THEN
      RETURN '{"ERROR": "PROYECTO YA FUE APROBADO Y AUDITADO, NO SE PUEDE ANULAR"}';
   END IF;
   UPDATE H02MPRY SET cEstado = 'X', cDniRes = p_cDniRes, tModifi = NOW() WHERE cIdProy = p_cIdProy;
   RETURN '{"OK": "OK"}';
END $$ LANGUAGE plpgsql VOLATILE;