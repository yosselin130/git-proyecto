import json
from Clases.CBase import *
from Clases.CSql import CSql

class CResponsables:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.loSql = CSql()
      self.pcError = ''

   def onAsignacionRes(self):
      return render_template('Ind1140.html')
   def onMantRes(self):
      return render_template('mantresponsables.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)
   
   def omResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCrearResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   
   def omMostrarResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxMostrarResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def omMostrarResponsable1(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxMostrarResp1()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def omEditarResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxEditarResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def omAsignarResp(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxAsignaResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def omSubirArvhivo(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxSubirArchivos()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def omDevolverDatos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverDatos()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

   '''def omMostrarEstados(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverEstado()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxDevolverEstado(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='227'"
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        print(type(self.paDatos))
        print(self.paDatos)
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True'''
   def __mxDevolverDatos(self):
        #traer tabla de proyectos
        lcSql = "select cidproy, cdescri from h02mpry  WHERE cestado='A' order by cidproy"
        RS = self.loSql.omExecRS(lcSql)
        self.paProyecto = RS
        #traer requisitos
        lcSql = "select cCodReq, cDescri from h02mreq where cEstado='A' order by cCodReq"
        RS = self.loSql.omExecRS(lcSql)
        self.paRequisito = RS
        #traer tabla de personas
        lcSql = "select cNroDni,  replace(cNombre,'/',' ') from S01MPER where cestado='A' LIMIT 200"
        RS = self.loSql.omExecRS(lcSql)
        self.paPersonas = RS
        #traer estados de puente de auditor -041
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='041'"
        RS = self.loSql.omExecRS(lcSql)
        self.paEstadosAuditor = RS
        #traer estado de detalle de proyecto -228
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='227'"
        RS = self.loSql.omExecRS(lcSql)
        self.paEstadoPuenteProyectos = RS

   def __mxCrearResp(self):
        # return render_template('Ind1160.html')
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02S01MPER('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
   
   def __mxMostrarResp1(self):
        lcJson = json.dumps(self.paData)
        #lcSql = "select * from  f_resp_proy('%s')" % (self.paData)
        lcSql = "select * from  v_resp_auditor"
        #lcSql = "select cidproy,cdescri from h02mpry where cestado = 'A' order by cidproy"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO HAY ASIGNACIONES DE REQUISITOS A RESPONSABLES"
            return False
        return True
   def __mxMostrarResp(self):
        lcJson = json.dumps(self.paData)
        lcSql = "select * from v_H02PPRY"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO HAY ASIGNACIONES DE REQUISITOS A RESPONSABLES"
            return False
        return True
   def __mxEditarResp(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02S01MPER('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
   def __mxAsignaResp(self):
        # return render_template('Ind1160.html')
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT p_h02ppry_ed('%s')" % (lcJson)
        print("procdimiento")
        print(lcSql)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True

   def __mxSubirArchivos(self):
        # return render_template('Ind1160.html')
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02PPRY('%s')" % (lcJson)
        print(lcSql)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
   def onListarResponsables(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxListarResponsables()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   
   def __mxListarResponsables(self):
        '''lcJson = json.dumps(self.paData)'''
        lcSql = "select * from v_h02paud('%s')" % (self.paData)
        print('**********************************LISTAR RESPONSABLES')
        print('===============')
        print(lcSql)
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        print('*******************************')
        print(self.paDatos)
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE RESPONSABLES"
            return False
        return True

   def onMostraRequisitos(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxMostraRequisistos()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   def __mxMostraRequisistos(self):
        '''lcJson = json.dumps(self.paData)'''
        lcSql = "SELECT * FROM f_res_req('%s','%s')" % (self.paData[0],self.paData[1])
        print('===============')
        print(self.paData[0])
        print(self.paData[1])
        print(lcSql)
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO HAY ASIGNACIONES DE REQUISITOS A RESPONSABLES"
            return False
        return True
      
