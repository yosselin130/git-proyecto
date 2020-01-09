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
    a.cidproy as codigoproy,
    c.cdescri AS proyecto,
    a.ccodreq AS codigoreq,
    d.cdescri AS requisito,
    e.cnrodni as DNI,
    replace(e.cNombre,'/',' '),
    a.mInfoad AS mInfoad,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni order by a.ccodigo
 LIMIT 200;


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
    a.carchivo, a.cextension 
   FROM h02ppry a
     JOIN s01mper b ON b.cnrodni = a.cnrodni
     JOIN H02MPRY d ON d.cidproy=a.cidproy
     JOIN v_s01ttab c ON btrim(c.ccodigo::text) = a.cestado::text AND c.ccodtab = '227'::bpchar;

ALTER TABLE public.v_h02ppry_name
  OWNER TO postgres;

---------VISTA PARA VER DETALLES REQUISITOS 
SELECT * FROM v_H02DPRY
CREATE OR REPLACE VIEW public.v_H02DPRY AS 
SELECT DISTINCT a.nSerial,a.cCodigo, d.cDescri,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
a.tFecRev,b.cDescri as Estado, a.mobserv FROM H02DPRY a 
INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME e ON e.cCodReq=a.cCodigo order by nSerial LIMIT 200;



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
  RETURNS TABLE(nserial character, ccodigo character, cdescri character, cnrodni character,responsable character, ccodaud character, cnombre character, tfecrev timestamp without time zone, cestado character, mobserv text, carchivo character, cextension character, cidproy character, proyecto character) AS
$BODY$


	 SELECT  DISTINCT a.nSerial,a.cCodigo, d.cDescri,e.cnrodni,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
	a.tFecRev,b.cDescri as Estado, a.mobserv,  e.carchivo, e.cextension,  e.cIdProy,e.cdescri as proyecto FROM H02DPRY a 
	INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
	INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME1 e ON e.cCodReq=a.cCodigo where e.cIdProy= p_cidproy  order by nSerial LIMIT 200;




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