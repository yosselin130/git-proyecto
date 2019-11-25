---------------------------------------INSERCCIONES MAESTRO PROYECTOS-------------------------------------
INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00001', 'A', 'MODULO EVENTOS', '72518755', '72518755', '"2019-10-09 08:05:56.822106"');

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00002', 'A', 'MODULO GESTION CALIDAD', '72565894', '72518755', '"2019-10-09 08:05:56.822106"');

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00003', 'A', 'MODULO APP', '47289024', '72518755', '"2019-10-09 08:05:56.822106"');

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00004', 'A', 'MODULO INSTITUTOS', '47289024', '47289024', '"2019-10-09 08:05:56.822106"');

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00005', 'A', 'MODULO TRAMMITES WEB', '78945617', '72565894', '"2019-10-09 08:05:56.822106"');

INSERT INTO h02mpry(
            cidproy, cestado, cdescri, cdnires, cdninro, tmodifi)
    VALUES ('00006', 'A', 'MODULO OCRRII', '78945613', '75982364', '"2019-10-09 08:05:56.822106"');

SELECT * FROM h02mpry;

-----INSERCCIONES REQUISITOS----------

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00001', 'A', 'DNI LEGALIZADOS', 'I', '72518755', '2019-10-09 08:05:56.822106');

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00002', 'A', 'CESIÓN DE DERECHOS', 'I', '78945617', '2019-10-09 08:05:56.822106');

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00003', 'A', 'MANUAL DE USUARIO', 'I', '47289024', '2019-10-09 08:05:56.822106');

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00004', 'A', 'PRUEBAS DE AMBIENTE', 'I', '78945617', '2019-10-09 08:05:56.822106');

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00005', 'A', 'CÓDIGO FUENTE', 'I', '72565894', '2019-10-09 08:05:56.822106');

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00006', 'A', 'DISEÑO GENERAL DEL SISTEMA', 'A', '72565894', '2019-10-09 08:05:56.822106');   

INSERT INTO h02mreq(
            ccodreq, cestado, cdescri, ctipo, cdninro, tmodifi)
    VALUES ('R00007', 'A', 'ESTUDIO DE FACTIBILIDAD', 'A', '72565894', '2019-10-09 08:05:56.822106');   

SELECT * FROM h02mreq;


-----------------INSERCIONES DE TABLA DE PUENTE PROYECTOS-REQUISITOS-INTEGRANTE ---------------------------

INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000001', 'P0001', 'R00001', '72565894', 'P', '72565894', 
            '2019-10-09 08:05:56.822106');
            
INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000002', 'P0001', 'R00002', '47289024', 'O', '47289024', 
            '2019-10-09 08:05:56.822106');  

INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000003', 'P0002', 'R00001', '72518755', 'A', '72518755', 
            '2019-10-09 08:05:56.822106');

INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000004', 'P0003', 'R00004', '47289024', 'P', '47289024', 
            '2019-10-09 08:05:56.822106');

INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000005', 'P0004', 'R00006', '72565894', 'E', '72565894', 
            '2019-10-09 08:05:56.822106');
            
INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000006', 'P0005', 'R00001', '72565894', 'O', '72565894', 
            '2019-10-09 08:05:56.822106');

INSERT INTO h02ppry(
            ccodigo, cidproy, ccodreq, cnrodni, cestado, cdninro, 
            tmodifi)
    VALUES ('000007', 'P0005', 'R00005', '72518755', 'O', '72518755', 
            '2019-10-09 08:05:56.822106');


select * from h02ppry;

------------INSERCCION DE TABLA DE AUDITOR - PROYECYO------------

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00001', 'A', 'P0001', '72565894', '72565894', '2019-10-09 08:05:56.82210');

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00002', 'A', 'P0003', '72518755', '72518755', '2019-10-09 08:05:56.82210');

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00003', 'A', 'P0005', '47289024', '47289024', '2019-10-09 08:05:56.82210');

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00004', 'A', 'P0002', '72565894', '72565894', '2019-10-09 08:05:56.82210');

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00005', 'A', 'P0006', '78945617', '78945617', '2019-10-09 08:05:56.82210');

INSERT INTO h02paud(
            ccodaud, cestado, cidproy, cnrodni, cdninro, tmodifi)
    VALUES ('A00007', 'A', 'P0004', '72518755', '72518755', '2019-10-09 08:05:56.82210');

SELECT * FROM h02paud;


------------------TABLA DE DETALLE PROYECTO---------------------------------------------------

INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('1', '000001', 'A00001', 'A', '2019-10-09 08:05:56.82210', 'Observado documentos',  '78945617', '2019-10-09 08:05:56.82210');


INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('2', '000003', 'A00004', 'A', '2019-10-09 08:05:56.82210', 'Aprobado',  '78945617', '2019-10-09 08:05:56.82210');

 
INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('3', '000002', 'A00002', 'A', '2019-10-09 08:05:56.82210', 'Aprobado', '78945617', '2019-10-09 08:05:56.82210');


INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('4', '000004', 'A00005', 'A', '2019-10-09 08:05:56.82210', 'Observado', '78945617', '2019-10-09 08:05:56.82210');


INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('5', '000005', 'A00007', 'A', '2019-10-09 08:05:56.82210', 'Aprobado','78945617', '2019-10-09 08:05:56.82210');


INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('6', '000007', 'A00003', 'A', '2019-10-09 08:05:56.82210', 'Observado', '78945617', '2019-10-09 08:05:56.82210');


INSERT INTO h02dpry(
            nserial, ccodigo, ccodaud, cestado, tfecrev, mobserv, cdninro, tmodifi)
    VALUES ('7', '000006', 'A00005', 'A', '2019-10-09 08:05:56.82210', 'Aprobado' ,'78945617', '2019-10-09 08:05:56.82210');

select * from h02dpry;
    
select * from S01MPER;
