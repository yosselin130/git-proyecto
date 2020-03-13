
SELECT P_H02MPRY('{"CESTADO": "A", "CAUDITOR": "None", "CIDPROY": "00002", "CNRODNI": "73047719", "CDESCRI": "MODULO GESTION CALIDAD1", "CDNIRES": "72565894", "CRESPONSABLE": "YOSSI"}')

SELECT P_H02MPRY('{"CRESPONSABLE": "REVILLA FLORES RAUL ROLANDO", "CIDPROY": "00026", "CNRODNIAUD": "T0000028", "CAUDITOR": "CACERES BAUTISTA SHIRLEY CRESSY", "CESTADO": "A", "CDNIRES": "70127517", "CDESCRI": "pppp"}')
select * from H02MPRY
CREATE OR REPLACE FUNCTION public.p_h02mpry(text)
  RETURNS text AS
$BODY$
DECLARE
   --PROCEDIMENTO QUE CREA Y ACTUALIZA UN PROYECTO 
   p_cData     ALIAS FOR $1;
   --PARÁMETROS CABECERA
   p_cIdProy  CHARACTER(5)    NOT NULL := '';
   p_cDescri  VARCHAR(200)    NOT NULL := '';
   p_cDniRes  CHARACTER(8)    NOT NULL := '';
   p_cNroDniAud  CHARACTER(8)    NOT NULL := '';
   p_cDniNro  CHARACTER(8)    NOT NULL := '';
   p_cEstado  CHARACTER(1)    NOT NULL := '';
   p_cCodReq  CHARACTER(6); 
   R1         RECORD;
   --VARIABLES LOCALES
   loJson    JSON;
   lcIdProy   CHARACTER(5);
   lcCodigo   CHARACTER(6);
BEGIN
   BEGIN
      loJson := p_cData::JSON;
      p_cIdProy := loJson->>'CIDPROY';
      p_cDescri := loJson->>'CDESCRI';
      p_cDniRes := loJson->>'CDNIRES';
      p_cNroDniAud := loJson->>'CNRODNIAUD';
      p_cEstado := loJson->>'CESTADO';
     -- p_cDniNro := loJson->>'CDNINRO';
   --EXCEPTION WHEN OTHERS THEN
     -- RETURN '{"ERROR":"ERROR EN ENVÍO PARÁMETROS"}';
   END;
    -- VALIDA DNI DE RESPONSABLE DEL PROYECTO
   IF NOT EXISTS (SELECT cNroDni FROM S01MPER WHERE cNroDni = p_cDniRes AND cEstado = 'A') THEN
      RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO EXISTE"}';
   END IF;
   BEGIN
      IF p_cIdProy='*' THEN 
      -- NUEVO PROYECTO
         SELECT MAX(cIdProy) INTO lcIdProy FROM H02MPRY;
         IF lcIdProy ISNULL THEN
            lcIdProy := '00000';
         END IF;
         lcIdProy := TRIM(TO_CHAR(lcIdProy::INT + 1, '00000'));
         INSERT INTO H02MPRY (cIdProy, cEstado, cDescri, cDniRes, cDniNro, tModifi, cNroDniAud) VALUES 
                (lcIdProy,p_cEstado, p_cDescri, p_cDniRes,p_cDniRes ,NOW(),p_cNroDniAud);
                
	--select count(*) into tot from H02MREQ where cestado='A';
	
	for R1 in select ccodreq 
		from H02MREQ where cestado='A' LOOP
		 SELECT MAX(cCodigo) INTO lcCodigo FROM H02PPRY;
		 IF lcCodigo ISNULL THEN
		    lcCodigo := '00000';
		 END IF;
		 lcCodigo := TRIM(TO_CHAR(lcCodigo::INT + 1, '000000'));
		select R1.ccodreq INTO p_cCodReq
		from H02MREQ where cestado='A' and ccodreq=R1.ccodreq ;
		---inserta puente proyectos 
		INSERT INTO H02PPRY (cCodigo, cIdProy,
		 cCodReq, cNroDni, cEstado, cDniNro, tModifi) VALUES 
                (lcCodigo,lcIdProy, p_cCodReq, NULL,'P' , p_cDniRes ,NOW());
                --inserta detalle proyecto
                 --SELECT cNroDniAud into p_cNroDniAud FROM H02MPRY where cIdProy=p_cIdProy;
                 INSERT INTO H02DPRY1 (cCodigo, cNroDniAud, cEstado, tFecRev, mObserv, cDniNro, tModifi, cidproy) VALUES 
                (p_cCodReq, p_cNroDniAud, 'A', NULL, NULL, p_cDniRes ,NOW(),lcIdProy);
         END LOOP;
      ELSE
         -- VALIDA QUE LA PERSONA QUE ACTUALIZA EL PROYECTO SEA EL RESPONSABLE
         IF NOT EXISTS (SELECT cDniRes FROM H02MPRY WHERE cDniRes = p_cDniRes AND cIdProy = p_cIdProy) THEN
            RETURN '{"ERROR": "DNI DE USUARIO/RESPONSABLE NO PERTENECE AL PROYECTO"}';
         END IF;
         lcIdProy := p_cIdProy;
         UPDATE H02MPRY SET cDescri=p_cDescri, cDniRes=p_cDniRes, cEstado=p_cEstado, tModifi=NOW(), cNroDniAud=p_cNroDniAud WHERE cIdProy=lcIdProy;
	 for R1 in select ccodreq 
		from H02MREQ where cestado='A' LOOP
		 SELECT MAX(cCodigo) INTO lcCodigo FROM H02PPRY;
		 IF lcCodigo ISNULL THEN
		    lcCodigo := '00000';
		 END IF;
		 lcCodigo := TRIM(TO_CHAR(lcCodigo::INT + 1, '000000'));
		select R1.ccodreq INTO p_cCodReq
		from H02MREQ where cestado='A' and ccodreq=R1.ccodreq ;
                --inserta detalle proyecto
                UPDATE H02DPRY1 SET cNroDniAud=p_cNroDniAud WHERE cCodigo=p_cCodReq;
         END LOOP;
         --UPDATE H02DPRY1 SET cNroDniAud=p_cNroDniAud WHERE cCodigo=p_cCodReq;
      END IF;
  -- EXCEPTION WHEN OTHERS THEN 
    --  RETURN '{"ERROR": "ERROR AL CREAR/ACTUALIZAR UN PROYECTO, COMUNICARSE CON EL ADMINISTRADOR DE LA APLICACIÓN"}'; 
   END;
   RETURN '{"OK":"OK"}';
END $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.p_h02mpry(text)
  OWNER TO postgres;
