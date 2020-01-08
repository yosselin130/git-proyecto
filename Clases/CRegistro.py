import json
from Clases.CBase import *
from Clases.CSql import CSql

class CRegistro:
    def __init__(self):
        self.paData = []
        self.paDatos = []
        self.loSql = CSql()
        self.pcError = ''

    def omRegistro(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxRegistro()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def __mxRegistro(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_REGISTRO_SGRSIA('%s')"%(lcJson)
        RS = self.loSql.omExecRS(lcSql)
        print(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
