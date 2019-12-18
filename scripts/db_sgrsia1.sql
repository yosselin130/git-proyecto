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
CREATE OR REPLACE VIEW public.v_H02PPRY_NAME AS 
select a.cCodigo,a.cIdProy,a.cCodReq,a.cNroDni,replace(b.cNombre,'/',' ') as Responsable , a.cEstado, c.cDescri as Estadodes, a.mInfoAd from H02PPRY a 
inner join S01MPER b on b.cNroDni=a.cNroDni inner join V_S01TTAB c ON TRIM(c.cCodigo) = a.cEstado AND c.cCodTab = '227';
---------VISTA PARA VER DETALLES REQUISITOS 
SELECT * FROM v_H02DPRY
CREATE OR REPLACE VIEW public.v_H02DPRY AS 
SELECT DISTINCT a.nSerial,a.cCodigo, d.cDescri,replace(e.responsable,'/',' ') as Responsable,a.cCodAud,replace(c.cNombre,'/',' ') as Auditor, 
a.tFecRev,b.cDescri as Estado, a.mobserv FROM H02DPRY a 
INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '228' INNER JOIN v_h02paud c ON c.cCodAud=a.cCodAud
INNER JOIN H02MREQ d ON d.cCodReq=a.cCodigo INNER JOIN v_H02PPRY_NAME e ON e.cCodReq=a.cCodigo order by nSerial LIMIT 200;



------------------vista de revision proyectos 
 CREATE OR REPLACE VIEW public.v_h02ppry_rev AS 
 SELECT a.cIdProy,
    c.cdescri AS proyecto,
    d.cdescri AS requisito,
    replace(e.cNombre,'/',' ') AS responsable,
    b.cdescri AS estado
   FROM h02ppry a
     JOIN v_s01ttab b ON btrim(b.ccodigo::text) = a.cestado::text AND b.ccodtab = '227'::bpchar
     JOIN h02mpry c ON c.cidproy = a.cidproy
     JOIN h02mreq d ON d.ccodreq = a.ccodreq
     JOIN s01mper e ON e.cnrodni = a.cnrodni order by a.cIdProy
 LIMIT 200;