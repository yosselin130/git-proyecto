import os
from flask import render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import urllib.request
import json
from Clases.CBase import *
from Clases.CSql import CSql
""" from contants import SUCCESS_FILE_MESSAGE """


class CRequisitos:
    def __init__(self):
        self.paData = []
        self.paDatos = []
        self.loSql = CSql()
        self.pcError = ''

    def omRequisito(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCrearReq()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omMostrarRequisitos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxMostrarRequisito()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def omEditarRequisitos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxEditarRequisito()
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
    
    def omMostrarTipos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverTipo()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

    def __mxCrearReq(self):
        # return render_template('Ind1160.html')
        lcJson = json.dumps(self.paData)
        print(lcJson)
        lcSql = "SELECT P_H02MREQ('%s')" % (lcJson)
        print("datossss")
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

    def __mxMostrarRequisito(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT a.cCodReq,a.cDescri,c.cDescri Tipo, b.cDescri Estado, a.cDniNro FROM H02MREQ a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '041' inner JOIN V_S01TTAB c ON TRIM(c.cCodigo) = a.cTipo AND c.cCodTab = '226' ORDER BY  a.cCodReq LIMIT 200"
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

    def __mxEditarRequisito(self):
        lcJson = json.dumps(self.paData)
        lcSql = "UPDATE H01DPAR SET cEstado = 'A', cDniNro = '00000000', tModifi = NOW() WHERE nSerial = '%s'"%(R2[0][0])
        lcSql = "SELECT P_H02MREQ('%s')" % (RS[0][0])
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
        print("estado")
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='041'"
        print(lcSql)
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
    
    def __mxDevolverTipo(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='226'"
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True

    def omAsignarRequisito(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxAsignarRequisito()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
    def __mxAsignarRequisito(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='226'"
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True

    def onDescargarReq(self):
        return render_template('requisitos.html')

    def onSubirReq(self):
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    'C:/tesis/visual/SGRSIA/archivos', filename))
                flash('Se subío con éxito el archivo')
                return redirect('/subirreq')
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return redirect(request.url)
        return render_template('subirarchivo.html')

    def onProgReq(self):
        return render_template('progresoreq.html')

    def omInit(self):
        error = None
        return render_template('proyecto.html', error=error)

        
