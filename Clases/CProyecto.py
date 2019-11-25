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
        print(llOk)
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def __mxCrearProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_S01MPRY('%s')"%(lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True

    def __mxMostrarProyecto(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT cIdProy,cDescri,cDniRes,cEstado FROM H02MPRY LIMIT 200"
        #lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        #$lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        #WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        '''while laFila = loSql.fetch(RS):
            self.paData[] ={['CIDPROY'.laFila[0], 'CDESCRI'.laFila[1],'CDNIRES'.laFila[2],
            'CDNIRES'.laFila[3],'CESTADO'.laFila[4]}
            i = i + 1
        '''
        if len(RS)==0:
            self.pcError="NO TIENE NINGÚN PROYECTO"
            return False
        return True


           



   
  