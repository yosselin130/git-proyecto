import json
from Clases.CBase import *
from Clases.CSql import CSql


class CProyecto:
    def __init__(self):
        self.paData = []
        self.paDatos = []
        self.loSql = CSql()
        self.pcError = ''

    def omProyecto(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCrearProyecto()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omMostrarProyectos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxMostrarProyecto()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omEditarProyectos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxEditarProyecto()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omCerrarProyecto(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCerrarProyecto()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omMostrarEstados(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverEstado()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def __mxCrearProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02MPRY('%s')" % (lcJson)
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

    def __mxMostrarProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT a.cIdProy,a.cDescri,cDniRes,replace(c.cNombre,'/',' '),b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '225' INNER JOIN S01MPER C ON c.cNroDni=a.cDniRes ORDER BY  a.cIdProy LIMIT 200"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE NINGÚN PROYECTO"
            return False
        return True
    def __mxEditarProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02MPRY('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True

    def __mxDevolverEstado(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='225'"
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
        return True
    def __mxCerrarProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02MPRY2('%s')" % (lcJson)
        #lcSql = "SELECT P_H02MPRY2('%s')" % (self.paData)
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
