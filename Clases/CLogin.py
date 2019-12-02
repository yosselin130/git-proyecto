
'''class CLogin:
    def __init__(self):
        self.paData = []
        self.paDatos = []
        self.cNombre = None

    def omInit(self):
        pass

    def omLogin(self):
        print('1)', self.paData['CNRODNI'])
        print('1)', self.paData['CCLAVE'])
        if self.paData['CNRODNI'] != 'admin' or self.paData['CCLAVE'] != 'admin':
            self.pcError = 'Credenciales Invalidas, volver a ingresar por favor.'
            return False
        return True '''

import json
from Clases.CBase import *
from Clases.CSql import CSql

class CLogin:
    def __init__(self):
        self.paData = []
        self.paDatos = []
        self.loSql = CSql()
        self.pcError = ''

    def omLogin(self):
        llOK = self.__mxValLogin()
        if not llOk:
            return False
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError    
            return False
        llOk = self.__mxLogin()
        self.loSql.omDisconnect()
        return llOk

    def __mxValLogin(self):

        if len(self.paData['CNRODNI'])== 0 or self.paData['CNRODNI'] == null or len(self.paData['CNRODNI']) != 8 :
            self.pcError="INGRESAR NUMERO DE DNI VÁLIDO"
            return False
        elif len(self.paData['CCLAVE']) == 0:
            self.pcError="CONTRASEÑA NO DEFINIDA"
            return False
        self.paData['CCLAVE'] = hash('sha512', self.paData['CCLAVE'])
        return True

    def __mxLogin(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_LOGIN_SGRSIA('%s')"%(lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
