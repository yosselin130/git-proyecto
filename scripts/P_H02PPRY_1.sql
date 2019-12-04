--BEGIN;SELECT P_S01MPRY_1('{"CIDPROY":"P0004","CDNIRES":"72518755"}');
--BEGIN;SELECT P_S01PPRY_1('{"CCODIGO":"000002","CIDPROY":"P0002","CCODREQ":"000004", "CNRODNI":"72518755"}');
--SELECT * FROM H02MPRY
--SELECT * FROM H02MREQ;
select * from h02paud;
SELECT * FROM H02DPRY
SELECT * FROM H02PPRY

CREATE OR REPLACE FUNCTION P_H02PPRY_1(text)
  RETURNS text AS $$
DECLARE
   --PROCEDIMENTO QUE ANULA ASIGNACION DE PROYECTO REQUISITO INTEGRANTE 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cCodigo  CHARACTER(6)    NOT NULL := '';
   p_cIdProy  CHARACTER(5);    --NOT NULL := '';
   p_cCodReq  CHARACTER(6)    NOT NULL := '';
   p_cNroDni  CHARACTER(8);    --NOT NULL := '';
   p_cEstado  CHARACTER(1);
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(8);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cCodigo := loJson->>'CCODIGO';
      p_cIdProy := loJson->>'CIDPROY';
      p_cCodReq := loJson->>'CCODREQ';
      p_cNroDni := loJson->>'CNRODNI';
      --p_cEstado := loJson->>'CESTADO';
   EXCEPTION WHEN OTHERS THEN
      RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
   -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cNroDni AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE O NO ESTÁ ACTIVO"}';
   END IF;
   -- VALIDA QUE USUARIO PERTENEZCA A PROYECTO
   --SELECT cDniRes INTO p_cDniRes FROM H02MPRY WHERE cIdProy = p_cIdProy
   --IF p_cDniRes IS NOT cDniRes THEN
    --  RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE EN PROYECTO O NO ESTÁ ACTIVO"}';
   --END IF;
   -- Valida PROYECTO
   SELECT cEstado, cDniRes INTO p_cEstado, p_cNroDni FROM H02MPRY WHERE cIdProy = p_cIdProy;
   IF NOT EXISTS (SELECT cIdProy FROM H02MPRY WHERE cIdProy = p_cIdProy) THEN
      RETURN '{"ERROR": "EL CODIGO DEL PROYECTO NO EXISTE"}';
   ELSIF NOT p_cEstado IN ('A', 'F', 'X') THEN   
      RETURN '{"ERROR": "ESTADO DEL PROYECTO NO PERMITE ANULAR"}';
   END IF;
     -- Valida REQUISITO
   SELECT cEstado INTO p_cEstado  FROM H02MREQ WHERE cCodReq = p_cCodReq;
   IF NOT EXISTS (SELECT cCodReq FROM H02MREQ WHERE cCodReq = p_cCodReq) THEN
      RETURN '{"ERROR": "EL CODIGO DEL REQUISITO NO EXISTE"}';
   ELSIF NOT p_cEstado IN ('A', 'I') THEN   
      RETURN '{"ERROR": "ESTADO DEL PROYECTO NO PERMITE ANULAR"}';
   END IF;
      -- Valida Estado de estado de requisitos-proyecto
      SELECT cEstado INTO p_cEstado FROM H02PPRY WHERE cCodigo = p_cCodigo;
      IF p_cEstado = 'A' THEN
         RETURN '{"ERROR": "PROYECTO YA FUE APROBADO Y AUDITADO, NO SE PUEDE ANULAR"}';
      END IF;
      -- Valida Estado de estado de detalle-proyecto
      SELECT cEstado INTO p_cEstado FROM H02DPRY WHERE cCodigo = p_cCodReq;
      IF p_cEstado = 'A' THEN
         RETURN '{"ERROR": "REQUISITO YA FUE APROBADO Y AUDITADO, NO SE PUEDE ANULAR"}';
      END IF;
   UPDATE H02PPRY SET cEstado = 'X', cNroDni = p_cNroDni, tModifi = NOW() WHERE cCodigo = p_cCodigo;
   RETURN '{"OK": "OK"}';
END $$ LANGUAGE plpgsql VOLATILE;

