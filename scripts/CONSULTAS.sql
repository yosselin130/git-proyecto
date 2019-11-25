SELECT * FROM H02MPRY
SELECT * FROM H02MREQ;
select * from h02paud;
SELECT * FROM H02DPRY
SELECT * FROM H02PPRY

SELECT cIdProy ,cDescri,cDniNro, cEstado FROM H02MPRY 

select cCodigo, cIdProy, cCodReq, cEstado, cNroDni FROM H02PPRY 

SELECT d.nSerial, pr.cIdProy,p.cDescri Proyecto, pr.cEstado estado_asig,d.cCodigo, r.cDescri Requisito, r.cTipo,r.cEstado estadoreq, d.cCodAud,a.cNroDni DNI_AUD, d.cEstado, d.tFecRev, mObserv FROM H02DPRY d,
 H02MREQ r, H02PPRY pr,H02MPRY p , h02paud a where d.cCodigo = r.cCodReq and pr.cCodReq=r.cCodReq and pr.cIdProy = p.cIdProy and d.cCodAud= a.cNroDni;

SELECT distinct d.nSerial, pr.cIdProy,p.cDescri Proyecto, pr.cEstado estado_asig,d.cCodigo, r.cDescri Requisito, r.cTipo,r.cEstado estadoreq, d.cCodAud,a.cNroDni DNI_AUD, d.cEstado, d.tFecRev, mObserv FROM H02DPRY d,
 H02MREQ r, H02PPRY pr,H02MPRY p , h02paud a where d.cCodigo = r.cCodReq and pr.cCodReq=r.cCodReq and pr.cIdProy = p.cIdProy  and pr.cIdProy='P0003' ;