from flask import render_template, redirect, url_for, request

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
   def __mxCrearResp(self):
        # return render_template('Ind1160.html')
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02MREQ('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
   def __mxMostrarResp(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT a.cCodReq,a.cDescri,c.cDescri Tipo, b.cDescri Estado FROM H02MREQ a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '041' inner JOIN V_S01TTAB c ON TRIM(c.cCodigo) = a.cTipo AND c.cCodTab = '226'  LIMIT 200"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE NINGÚN REQUISITO"
            return False
        return True
   def __mxEditarResp(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02MREQ('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True