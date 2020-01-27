--TABLA DE MAESTRO PROYECTOS 
CREATE TABLE H02MPRY (
   cIdProy  CHARACTER(5)   NOT NULL PRIMARY KEY,
   cEstado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [225] A:ACTIVO, F:FINALIZADO, X:ANULADO
   cDescri  VARCHAR(200)   NOT NULL,
   cDniRes  CHARACTER(8)   NOT NULL REFERENCES S01MPER (cNroDni) ON DELETE RESTRICT ON UPDATE CASCADE,
   cDniNro  CHARACTER(8)   NOT NULL,
   tModifi  TIMESTAMP      NOT NULL DEFAULT NOW()
);

INSERT INTO S01TTAB VALUES
(DEFAULT,'225',0,'H02MPRY.cEstado','0','0','* ESTADO DE PROYECTO','','U666',NOW()),
(DEFAULT,'225',1,'','1','A','ACTIVO','','U666',NOW()),
(DEFAULT,'225',2,'','1','F','FINALIZADO','','U666',NOW()),
(DEFAULT,'225',2,'','1','X','ANULADO','','U666',NOW());

--TABLA DE MAESTRO REQUISITOS
CREATE TABLE H02MREQ (
   cCodReq  CHARACTER(6)   NOT NULL PRIMARY KEY,
   cEstado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [041]
   cDescri  VARCHAR(150)   NOT NULL,
   cTipo    CHARACTER(1)   NOT NULL DEFAULT 'A',   --[226] A:AUDITORIA, I:INDECOPI
   cDniNro  CHARACTER(8)   NOT NULL,
   tModifi  TIMESTAMP      NOT NULL DEFAULT NOW()
);

INSERT INTO S01TTAB VALUES
(DEFAULT,'226',0,'H02MREQ.cTipo','0','0','* TIPO DE REQUISITO','','U666',NOW()),
(DEFAULT,'226',1,'','1','A','AUDITORIA','','U666',NOW()),
(DEFAULT,'226',2,'','1','I','INDECOPI','','U666',NOW());

--TABLA DE PUENTE DE PROYECTOS-REQUISITOS-INTEGRANTE
CREATE TABLE H02PPRY (
   cCodigo  CHARACTER(6)   NOT NULL PRIMARY KEY,
   cIdProy  CHARACTER(5)   NOT NULL REFERENCES H02MPRY (cIdProy) ON DELETE RESTRICT ON UPDATE CASCADE,  
   cCodReq  CHARACTER(6)   NOT NULL REFERENCES H02MREQ (cCodReq) ON DELETE RESTRICT ON UPDATE CASCADE,
   cNroDni  CHARACTER(8)   NOT NULL REFERENCES S01MPER (cNroDni) ON DELETE RESTRICT ON UPDATE CASCADE,   
   cEstado  CHARACTER(1)   NOT NULL, --[227]  P:PENDIENTE, E:ENTREGADO, O:OBSERVADO, A:AUDITADO, X:ANULADO
   cDniNro  CHARACTER(8)   NOT NULL,
   tFecSub  TIMESTAMP      NOT NULL,
   mInfoad  TEXT           NOT NULL,
   cArchivo CHARACTER(6)   ,
   cExtension CHARACTER(5) ,
   tModifi  TIMESTAMP      NOT NULL DEFAULT NOW(),
);

INSERT INTO S01TTAB VALUES
(DEFAULT,'227',0,'H02PPRY.cEstado','0','0','* ESTADO DE PUENTE REQUISITO INTEGRANTE','','U666',NOW()),
(DEFAULT,'227',1,'','1','P','PENDIENTE','','U666',NOW()),
(DEFAULT,'227',2,'','1','E','ENTREGADO','','U666',NOW()),
(DEFAULT,'227',3,'','1','O','OBSERVADO','','U666',NOW()),
(DEFAULT,'227',4,'','1','A','AUDITADO','','U666',NOW()),
(DEFAULT,'227',5,'','1','X','ANULADO','','U666',NOW());

--TABLA DE PUENTE AUDITOR
CREATE TABLE H02PAUD (
   cCodAud  CHARACTER(6)   NOT NULL PRIMARY KEY,
   cEstado  CHARACTER(1)   NOT NULL DEFAULT 'A',   -- [041]
   cIdProy  CHARACTER(6)   NOT NULL REFERENCES H02MPRY (cIdProy) ON DELETE RESTRICT ON UPDATE CASCADE,  
   cNroDni  CHARACTER(8)   NOT NULL REFERENCES S01MPER (cNroDni) ON DELETE RESTRICT ON UPDATE CASCADE,
   cDniNro  CHARACTER(8)   NOT NULL,
   tModifi  TIMESTAMP      NOT NULL DEFAULT NOW(),
);

--TABLA DE DETALLE DE PROYECTO
CREATE TABLE H02DPRY (
   nSerial  CHARACTER(1)   NOT NULL,
   cCodigo  CHARACTER(6)   NOT NULL REFERENCES H02PPRY (cCodigo) ON DELETE RESTRICT ON UPDATE CASCADE,  
   cCodAud  CHARACTER(6)   NOT NULL REFERENCES H02PAUD (cCodAud) ON DELETE RESTRICT ON UPDATE CASCADE,
   cEstado  CHARACTER(1)   NOT NULL,  --[228] A:APROBADO, O:OBSERVADO
   tFecRev  TIMESTAMP      NOT NULL,
   mObserv  TEXT           NOT NULL,
   cDniNro  CHARACTER(8)   NOT NULL,
   tModifi  TIMESTAMP      NOT NULL DEFAULT NOW()
);

INSERT INTO S01TTAB VALUES
(DEFAULT,'228',0,'H02DPRY.cEstado','0','0','* ESTADO DE DETALLE PROYECTO','','U666',NOW()),
(DEFAULT,'228',1,'','1','A','APROBADO','','U666',NOW()),
(DEFAULT,'228',2,'','1','O','OBSERVADO','','U666',NOW());


----VISTAS
----PUENTE PORYECTOS
--SELECT * FROM v_H02PPRY;


 CREATE OR REPLACE VIEW public.v_h02ppry AS 
 SELECT a.ccodigo,
    a.cidproy AS codigoproy,
    c.cdescri AS proyecto,
    a.ccodreq AS codigoreq,
    d.cdescri AS requisito,
    e.cnrodni AS dni,
    replace(e.cnombre::text, '/'::text, ' '::text) AS replace,
    a.minfoad,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni
  WHERE c.cestado = 'A'::bpchar AND d.cestado = 'A'::bpchar
  ORDER BY a.ccodigo
 LIMIT 200;

ALTER TABLE public.v_h02ppry
  OWNER TO postgres;


----vista de auditores 
CREATE OR REPLACE VIEW public.v_h02paud AS 
select a.cCodAud,a.cEstado,a.cIdProy,a.cNroDni, b.cNombre, a.cDniNro, a.tModifi from H02PAUD a inner join S01MPER b on b.cNroDni=a.cNroDni;

select * from H02PAUD
select * from v_h02paud

--------vista de puente con repsonsable y estados descripcion

 CREATE OR REPLACE VIEW public.v_h02ppry_name1 AS 
 SELECT a.ccodigo,
    a.cidproy,
    d.cdescri,
    a.ccodreq,
    a.cnrodni,
    replace(b.cnombre::text, '/'::text, ' '::text) AS responsable,
    a.cestado,
    c.cdescri AS estadodes,
    a.minfoad,
    a.carchivo,
    a.cextension
   FROM h02ppry a
     JOIN s01mper b ON b.cnrodni = a.cnrodni
     JOIN h02mpry d ON d.cidproy = a.cidproy
     JOIN v_s01ttab c ON btrim(c.ccodigo::text) = a.cestado::text AND c.ccodtab = '227'::bpchar where d.cestado in ('A', 'F');

ALTER TABLE public.v_h02ppry_name1
  OWNER TO postgres;

---------VISTA PARA VER DETALLES REQUISITOS 
SELECT * FROM v_H02DPRY
CREATE OR REPLACE VIEW public.v_h02dpry AS 
 SELECT DISTINCT f.cidproy,
    a.nserial,
    a.ccodigo,
    d.cdescri,
    replace(e.responsable, '/'::text, ' '::text) AS responsable,
    a.ccodaud,
    replace(c.cnombre::text, '/'::text, ' '::text) AS auditor,
    a.tfecrev,
    b.cdescri AS estado,
    a.mobserv,
    f.carchivo,
    f.cextension
   FROM h02dpry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '228'::bpchar
     JOIN v_h02paud c ON c.ccodaud = a.ccodaud
     JOIN h02mreq d ON d.ccodreq = a.ccodigo
     JOIN v_h02ppry_name e ON e.ccodreq = a.ccodigo
     JOIN h02ppry f ON f.ccodreq = a.ccodigo
  ORDER BY a.nserial
 LIMIT 200;

ALTER TABLE public.v_h02dpry
  OWNER TO postgres;


------------------vista de revision proyectos 
 select * from v_h02ppry_rev

CREATE OR REPLACE VIEW public.v_h02ppry_rev AS 
 SELECT a.cCodigo,a.cIdProy,
    c.cdescri AS proyecto,
    a.cCodReq,
    d.cdescri AS requisito,
    a.cnrodni,
    replace(e.cNombre,'/',' ') AS responsable,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni order by a.cCodigo
 LIMIT 200;


 ------funcion
CREATE OR REPLACE FUNCTION public.v_h02paud(IN p_cnombre text)
  RETURNS TABLE(cnrodni character, cnombre character) AS
$BODY$

	select cnrodni, replace(cnombre,'/',' ') from s01mper where cnombre like '%' || UPPER(p_cnombre) || '%' LIMIT 5 

	
$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;

  select * from v_h02paud('miguel')
------funcion de proyecto------------------
SELECT * FROM v_H02PPRY3('00002')

CREATE OR REPLACE FUNCTION public.v_h02ppry3(IN p_cidproy text)
  RETURNS TABLE(nserial character, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character) AS
$BODY$


	 SELECT  DISTINCT a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto FROM H02DPRY a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where d.cestado='A' and c.cestado='A' and e.cIdProy= p_cidproy  order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.v_h02ppry3(text)
  OWNER TO postgres;


  select * from v_H02PPRY3('00002')


----reportessssss
CREATE OR REPLACE VIEW public.v_h02ppry_REP AS 

SELECT  a.nSerial,e.cIdProy,f.cdescri as Proyecto,a.cCodigo, d.cDescri,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension FROM H02DPRY a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME e ON e.cCodReq=a.cCodigo inner join h02mpry f ON e.cIdProy=f.cIdProy  order by a.nSerial LIMIT 200;


select * from v_h02ppry_REP



CREATE OR REPLACE VIEW public.v_h02ppry_porcentaje AS
select cCodigo, estado,round(cCodigo::numeric*100/total_general::numeric,2) FROM (SELECT count(*) as cCodigo, estado , 
    (SELECT count(*) FROM v_h02ppry_rev) as total_general FROM v_h02ppry_rev GROUP BY  estado ) AS porcentaje;


---------------funcioness--------------------------
-------funcion_auditor----------------------------------------------------
 SELECT * FROM f_auditor('72518755')

CREATE OR REPLACE FUNCTION public.f_auditor(IN p_cnrodni text)
  RETURNS TABLE(cCodaud character, cNroDni character, cNombre character, cIdProy character, cDescri character, Estado character) AS
$BODY$


 SELECT a.cCodaud,a.cNroDni,replace(c.cNombre,'/',' ') as Auditor, a.cIdProy, d.cDescri as Proyecto,b.cDescri as Estado FROM H02PAUD a 
  INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '041' INNER JOIN S01MPER c ON c.cNroDni=a.cNroDni INNER JOIN H02MPRY d ON d.cIdproy=a.cIdProy WHERE a.cestado='A'  AND d.cestado='A' and a.cNroDni=p_cnrodni ORDER BY  a.cCodaud LIMIT 200


$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_auditor(text)
  OWNER TO postgres;
--------funcion de puente proyectos ---------------
CREATE OR REPLACE FUNCTION public.f_resp_proy(IN p_cnrodni text)
  RETURNS TABLE(ccodigo character, cidproy character, proyecto character, ccodreq character, requisito character, cnrodni character, cnombre character, minfoad character, estado character) AS
$BODY$

	SELECT DISTINCT a.ccodigo,
    a.cidproy AS codigoproy,
    c.cdescri AS proyecto,
    a.ccodreq AS codigoreq,
    d.cdescri AS requisito,
    e.cnrodni AS dni,
    replace(e.cnombre::text, '/'::text, ' '::text) AS replace,
    a.minfoad,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni
  WHERE c.cestado = 'A'::bpchar AND d.cestado = 'A'::bpchar AND a.cestado in ('P','E','O','A') and  a.cnrodni='72518755'
  ORDER BY a.ccodigo
 LIMIT 200;

$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_resp_proy(text)
  OWNER TO postgres;
  
select * from  f_resp_proy('72518755')
select * from h02mreq where cestado='A'
select * from h02ppry;

---------ESTADO FULL----PPRY
CREATE OR REPLACE FUNCTION public.f_h02ppry3_all(
    IN p_cnrodni text,
    IN p_cidproy text)
  RETURNS TABLE(nserial character, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character) AS
$BODY$


	 SELECT  DISTINCT a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto FROM H02DPRY a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cIdProy= p_cidproy and e.cnrodni=p_cnrodni order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_h02ppry3_all(text, text)
  OWNER TO postgres;

  -------funcion de auditor_ppry_full--------
  
SELECT * FROM f_h02ppry3_all_audit('72518755','00004')

CREATE OR REPLACE FUNCTION public.f_h02ppry3_all_audit(
    IN p_cnrodni text,
    IN p_cidproy text)
  RETURNS TABLE(codppry character, nserial integer, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character, estadogeneral character) AS
$BODY$


	 SELECT  DISTINCT e.ccodigo as codppry,a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cnrodniaud,c.Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto, e.estadodes as estadogeneral FROM H02DPRY1 a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_auditor c ON c.cnrodniaud=a.cnrodniaud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cIdProy= p_cidproy and c.cnrodniaud=p_cnrodni order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_h02ppry3_all_audit(text, text)
  OWNER TO postgres;
------funcion auditor -asignar---------
SELECT * FROM f_h02ppry3_all_audit_1('47289024','00005')
CREATE OR REPLACE FUNCTION public.f_h02ppry3_all_audit(
    IN p_cnrodni text,
    IN p_cidproy text)
  RETURNS TABLE(codppry character,nserial integer, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, 
  proyecto character,estadogeneral character ) AS
$BODY$


	 SELECT  DISTINCT e.ccodigo as codppry,a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto, e.estadodes as estadogeneral FROM H02DPRY1 a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cIdProy= p_cidproy and c.cnrodni=p_cnrodni order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_h02ppry3_all_audit(text, text)
  OWNER TO postgres;

  ---------funcion responsable -requisitos 

  CREATE OR REPLACE FUNCTION public.f_res_req(IN p_cidproy text, IN p_cnrodni text)
  RETURNS TABLE(ccodigo character, codigoproy character, proyecto character, codigoreq character, requisito character, dni character, cnombre character, minfoad text, cestado character) AS
$BODY$
   SELECT a.ccodigo,
    a.cidproy AS codigoproy,
    c.cdescri AS proyecto,
    a.ccodreq AS codigoreq,
    d.cdescri AS requisito,
    e.cnrodni AS dni,
    replace(e.cnombre::text, '/'::text, ' '::text) AS replace,
    a.minfoad,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni
  WHERE c.cestado = 'A'::bpchar AND d.cestado = 'A'::bpchar and a.cidproy=p_cidproy and e.cnrodni=p_cnrodni
  ORDER BY a.ccodigo
 LIMIT 200;



$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_res_req(text, text)
  OWNER TO postgres;

------------------vista auditores 

select  f.nSerial,f.cCodigo, d.cDescri,a.cnrodni ,e.cIdProy,e.cdescri,b.cDescri as Estado
from h02paud a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228'  INNER JOIN v_H02PPRY_NAME1 e ON a.cIdProy=e.cIdProy  INNER JOIN H02MREQ d ON d.cCodReq=e.cCodReq INNER JOIN H02DPRY f ON f.cCodigo=d.cCodReq  
where a.cnrodni='72518755';


-----vista auditoressss-----

 CREATE OR REPLACE VIEW public.v_auditor AS 
 SELECT a.cidproy,
    a.cdescri,
    a.cnrodniaud,
    replace(d.cnombre::text, '/'::text, ' '::text) AS auditor,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = a.cestado::text AND c.ccodtab = '225'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = a.cnrodniaud
  WHERE a.cestado = 'A'::bpchar
  ORDER BY a.cidproy;

ALTER TABLE public.v_auditor
  OWNER TO postgres;
----- vista,aud y resp
CREATE OR REPLACE VIEW public.v_resp_auditor AS 
 SELECT a.cidproy,
    a.cdescri,
    b.ccodigo,
    b.ccodreq AS codigoreq,
    e.cdescri AS requisito,
    b.cnrodni,
    replace(d.cnombre::text, '/'::text, ' '::text) AS responsable,
    f.ccodaud,
    f.auditor,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN h02ppry b ON b.cidproy = a.cidproy
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = b.cestado::text AND c.ccodtab = '227'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = b.cnrodni
     LEFT JOIN h02mreq e ON e.ccodreq = b.ccodreq
     LEFT JOIN v_auditor f ON f.cidproy = a.cidproy
  WHERE a.cestado = 'A'::bpchar 
  ORDER BY a.cidproy;

ALTER TABLE public.v_resp_auditor
  OWNER TO postgres;


  select * from v_resp_auditor;
--------FUNCION PPRY
CREATE OR REPLACE FUNCTION public.f_h02ppry3(IN p_cidproy text)
  RETURNS TABLE(nserial INTEGER, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character) AS
$BODY$


	 SELECT  DISTINCT a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto FROM H02DPRY1 a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cIdProy= p_cidproy order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_h02ppry3(text)
  OWNER TO postgres;

  -----FUNCION DE PUENTE - DETALLE PROYECTOS- DNI
  
CREATE OR REPLACE FUNCTION public.f_h02ppry3_dni(IN p_cnrodni text)
  RETURNS TABLE(nserial INTEGER, ccodigo character, cdescri character, cnrodni character, responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character) AS
$BODY$


	 SELECT  DISTINCT a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto FROM H02DPRY1 a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cnrodni= p_cnrodni  order by nSerial LIMIT 200;




$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_h02ppry3_dni(text)
  OWNER TO postgres;

  ---tabla dpry
  
CREATE TABLE public.h02dpry1
(
  nserial integer NOT NULL DEFAULT nextval('h02dpry1_nserial_seq'::regclass),
  ccodigo character(6) NOT NULL,
  ccodaud character(6) NOT NULL,
  cestado character(1) NOT NULL,
  tfecrev timestamp without time zone,
  cdninro character(8) NOT NULL,
  tmodifi timestamp without time zone NOT NULL DEFAULT now(),
  mobserv text,
  CONSTRAINT h02dpry_ccodaud_fkey FOREIGN KEY (ccodaud)
      REFERENCES public.h02paud (ccodaud) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT h02dpry1_nserial_key UNIQUE (nserial)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.h02dpry1
  OWNER TO postgres;

  ----TABLA DE S01MPER--------------------------------------------------------------
  UPDATE public.s01mper
   SET cnrodni=?, cestado=?, cnombre=?, csexo=?, cnrocel=?, cemail=?, 
       cclave=?, cusucod=?, tmodifi=?, "cTipo"=?
 WHERE <condition>;


----ASGANACION SUPER USER (ADMIN)
UPDATE public.s01mper
   SET cTipo='S'
 WHERE cnrodni='47289024';


ALTER TABLE public.s01mper ADD COLUMN cTipo character(1);

SELECT * FROM s01mper WHERE cnrodni='47289024';

INSERT INTO S01TTAB VALUES
(DEFAULT,'229',0,'s01mper.cTipo','0','0','* TIPO USUARIO','','U666',NOW()),
(DEFAULT,'229',1,'','1','S','SUPERUSUARIO','','U666',NOW()),
(DEFAULT,'229',2,'','1','N','NORMAL','','U666',NOW());

---ASIGNACION USUARIO NORMAL 
UPDATE public.s01mper
   SET cTipo='N'
 WHERE cnrodni='72518755';


SELECT * FROM s01mper WHERE cnrodni='72518755';

----------------------------------------------------JUNTAR-PY-AUDITOR--------------
---vista completa auditor
  CREATE OR REPLACE VIEW public.v_auditor_py_all1 AS 
 SELECT DISTINCT  a.cidproy,
    a.cdescri,
    a.cdnires,
    replace(c.cnombre::text, '/'::text, ' '::text) AS responsable,
    d.cnrodniaud,
    d.auditor,
    d.ctipo,
    b.cdescri AS estado
   FROM h02mpry a
     LEFT outer JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '225'::bpchar
     LEFT JOIN s01mper c ON c.cnrodni = a.cdnires
     LEFT JOIN v_auditor_py1 d ON d.cnrodniaud = a.cnrodniaud
  WHERE a.cestado = ANY (ARRAY['A'::bpchar, 'F'::bpchar])  
  ORDER BY a.cidproy
 LIMIT 200;

ALTER TABLE public.v_auditor_py_all1
  OWNER TO postgres;


ALTER TABLE public.H02MPRY ADD COLUMN cNroDniAud character(8);

select * from H02MPRY

---VISTA DE AUDITOR-PROYECTO
CREATE OR REPLACE VIEW public.v_auditor_py1 AS 
 SELECT a.cidproy,
    a.cdescri,
    a.cnrodniaud,
    replace(c.cnombre::text, '/'::text, ' '::text) AS auditor,
    c.cTipo,
    b.cdescri AS estado
   FROM h02mpry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '225'::bpchar
     JOIN s01mper c ON c.cnrodni = a.cnrodniaud
  WHERE a.cestado = ANY (ARRAY['A'::bpchar, 'F'::bpchar])
  ORDER BY a.cidproy
 LIMIT 200;

ALTER TABLE public.v_auditor_py1
  OWNER TO postgres;
select * from v_AUDITOR_PY
select * from v_AUDITOR_PY_all

------------------------------funciones nuevas---------------------------------------
CREATE OR REPLACE FUNCTION public.f_res_aud(
    IN p_cidproy text,
    IN p_cnrodni text)
  RETURNS TABLE(cidproy character, cdescri character, ccodigo character, codigoreq character, requisito character, cnrodni character, responsable character, cnrodniaud character, auditor character, carchivo character, estado character) AS
$BODY$
 SELECT a.cidproy,
    a.cdescri,
    b.ccodigo,
    b.ccodreq AS codigoreq,
    e.cdescri AS requisito,
    b.cnrodni,
    replace(d.cnombre::text, '/'::text, ' '::text) AS responsable,
    f.cnrodniaud,
    f.auditor,
    b.carchivo,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN h02ppry b ON b.cidproy = a.cidproy
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = b.cestado::text AND c.ccodtab = '227'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = b.cnrodni
     LEFT JOIN h02mreq e ON e.ccodreq = b.ccodreq
     LEFT JOIN v_auditor f ON f.cidproy = a.cidproy
  WHERE a.cestado = 'A'::bpchar and a.cidproy=p_cidproy and b.cnrodni=p_cnrodni
  ORDER BY a.cidproy;
$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_res_aud(text, text)
  OWNER TO postgres;

-----------------------------------------responsable proyecto--------------
CREATE OR REPLACE FUNCTION public.f_resp(IN p_cnrodni text)
  RETURNS TABLE(cidproy character, cdescri character, ccodigo character, codigoreq character, requisito character, cnrodni character, responsable character, cnrodniaud character, auditor character, estado character) AS
$BODY$
SELECT a.cidproy,
    a.cdescri,
    b.ccodigo,
    b.ccodreq AS codigoreq,
    e.cdescri AS requisito,
    b.cnrodni,
    replace(d.cnombre::text, '/'::text, ' '::text) AS responsable,
    f.cnrodniaud,
    f.auditor,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN h02ppry b ON b.cidproy = a.cidproy
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = b.cestado::text AND c.ccodtab = '227'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = b.cnrodni
     LEFT JOIN h02mreq e ON e.ccodreq = b.ccodreq
     LEFT JOIN v_auditor f ON f.cidproy = a.cidproy
  WHERE a.cestado = 'A'::bpchar and b.cnrodni=p_cnrodni
  ORDER BY a.cidproy;

 $BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_resp(text)
  OWNER TO postgres;

  -------vista de repsnsables-asignacion ultimoo
 CREATE OR REPLACE VIEW public.v_resp AS 
 SELECT DISTINCT a.cidproy,
    a.cdescri,
    b.ccodigo,
    b.ccodreq AS codigoreq,
    e.cdescri AS requisito,
    b.cnrodni,
    replace(d.cnombre::text, '/'::text, ' '::text) AS responsable,
    f.cnrodniaud,
    f.auditor,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN h02ppry b ON b.cidproy = a.cidproy
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = b.cestado::text AND c.ccodtab = '227'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = b.cnrodni
     LEFT JOIN h02mreq e ON e.ccodreq = b.ccodreq
     LEFT JOIN v_auditor f ON f.cidproy = a.cidproy
  WHERE a.cestado = 'A'::bpchar
  ORDER BY a.cidproy;

ALTER TABLE public.v_resp
  OWNER TO postgres;


  -------------------vista py and req 
CREATE OR REPLACE VIEW public.v_req_res AS 
SELECT DISTINCT b.ccodigo, a.cCodReq, a.cDescri, b.cIdProy, b.cDescri as proyecto, b.cnrodni, b.responsable, b.cArchivo,b.estadodes FROM H02MREQ a LEFT JOIN v_H02PPRY_NAME1 b ON b.cCodReq=a.cCodReq 
WHERE a.cEstado='A' order by cCodReq LIMIT 200;
-------funcion para subir archivos-req
CREATE OR REPLACE FUNCTION public.f_res_req1(
    IN p_cidproy text,
    IN p_cnrodni text)
  RETURNS TABLE(ccodigo character, ccodreq character, cdescri character, cidproy character, proyecto character, cnrodni character, responsable character, carchivo character, estadodes character) AS
$BODY$
SELECT DISTINCT b.ccodigo,
    a.ccodreq,
    a.cdescri,
    b.cidproy,
    b.cdescri AS proyecto,
    b.cnrodni,
    b.responsable,
    b.carchivo,
    b.estadodes
   FROM h02mreq a
     LEFT JOIN v_h02ppry_name1 b ON b.ccodreq = a.ccodreq
  WHERE a.cestado = 'A'::bpchar and b.cidproy=p_cidproy and b.cnrodni=p_cnrodni
  ORDER BY a.ccodreq
 LIMIT 200;
	

$BODY$
  LANGUAGE sql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.f_res_req1(text, text)
  OWNER TO postgres;
--------------------------------------------------LOS PROYECTOS QUE NO TIENEN REQUISITOS----------------
CREATE OR REPLACE VIEW public.v_proy_req AS 
 SELECT DISTINCT b.ccodigo, a.cidproy,
    a.cdescri,
    b.ccodreq AS codigoreq,
    e.cdescri AS requisito,
    b.cnrodni,
    replace(d.cnombre::text, '/'::text, ' '::text) AS responsable,
    c.cdescri AS estado
   FROM h02mpry a
     LEFT JOIN h02ppry b ON b.cidproy = a.cidproy
     LEFT JOIN v_s01ttab c ON btrim(c.ccodigo::text) = b.cestado::text AND c.ccodtab = '227'::bpchar
     LEFT JOIN s01mper d ON d.cnrodni = b.cnrodni
     FULL JOIN h02mreq e ON e.ccodreq = b.ccodreq
  WHERE a.cestado = 'A'::bpchar
  ORDER BY a.cidproy;

ALTER TABLE public.v_proy_req
  OWNER TO postgres;

select * from v_proy_req;


----------------------------------------V_RES_REQ---requisitos que no tienen proyecto o requisitos
CREATE OR REPLACE VIEW public.V_RES_REQ AS 
SELECT DISTINCT b.ccodigo, a.cCodReq, a.cDescri, b.cIdProy, b.cDescri as proyecto, b.cnrodni, b.responsable, b.cArchivo,b.estadodes FROM H02MREQ a LEFT JOIN v_H02PPRY_NAME1 b ON b.cCodReq=a.cCodReq 
WHERE a.cEstado='A' order by cCodReq LIMIT 200;
v_req_res

------------------reporte---proyectos---
CREATE OR REPLACE VIEW public.v_auditor_py_all1_reportes AS 
 SELECT DISTINCT e.ccodigo,a.cidproy,
    a.cdescri,
    a.cdnires,
    replace(c.cnombre::text, '/'::text, ' '::text) AS responsable_proyecto,
    e.ccodreq,
    e.requisito,
    e.cnrodni,
    e.responsable,
    d.cnrodniaud,
    d.auditor,
    --d.ctipo,
    b.cdescri AS estado
   FROM h02mpry a
     INNER JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     INNER JOIN s01mper c ON c.cnrodni = a.cdnires
     INNER JOIN v_auditor_py1 d ON d.cnrodniaud = a.cnrodniaud INNER JOIN v_h02ppry_rev e ON e.cidproy=a.cidproy
  --WHERE a.cestado = ANY (ARRAY['A'::bpchar, 'F'::bpchar])
  ORDER BY a.cidproy
 LIMIT 200;
