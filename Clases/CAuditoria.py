import os
from flask import render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import urllib.request
import json
from Clases.CBase import *
from Clases.CSql import CSql

class CAuditoria:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.loSql = CSql()
      self.pcError = ''
   def omAuditor(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCrearAuditor()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxCrearAuditor(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02PAUD('%s')" % (lcJson)
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
   def __mxEditarAuditor(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02PAUD('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = json.loads(RS[0][0])
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True
   def omEditarAuditor(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxEditarAuditor()
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
   def __mxDevolverEstado(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='041'"
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
   def omMostrarEstados2(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverEstado2()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxDevolverEstado2(self):
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='228'"
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
   def omMostrarDatos(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverDatos()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxDevolverDatos(self):
        lcSql = "SELECT cCodaud,cIdProy FROM H02PAUD'"
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
   def omMostrarAuditor(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxMostrarAuditor()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxMostrarAuditor(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT a.cCodaud,a.cNroDni,replace(c.cNombre,'/',' ') as Auditor, a.cIdProy, d.cDescri as Proyecto,b.cDescri as Estado FROM H02PAUD a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '041' INNER JOIN S01MPER c ON c.cNroDni=a.cNroDni INNER JOIN H02MPRY d ON d.cIdproy=a.cIdProy ORDER BY  a.cCodaud LIMIT 200"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE NINGÚN AUDITOR"
            return False
        return True


    #######REVISAR AUDITORIA #############
   def onMostraProyectos(self):
       llOk = self.loSql.omConnect()
       if not llOk:
            self.pcError = self.loSql.pcError
            return False
       llOk = self.__mxMostraProyectos()
       if llOk:
            self.loSql.omCommit()
       self.loSql.omDisconnect()
       return llOk
      
   
   def __mxMostraProyectos(self):
      
        lcSql = "select * from v_h02ppry_rev"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE PROYECTOS"
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
     
        lcSql = "SELECT * FROM v_H02PPRY3('%s')" % (self.paData)
        print('===============')
        print(lcSql)
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        print('*******************************')
        print(self.paDatos)
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE REQUISITOS"
            return False
        return True
    
   def onMostradetallereq(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxMostradetallereq()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   
   def __mxMostradetallereq(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT a.cCodaud,replace(c.cNombre,'/',' ') as Auditor, d.cDescri as Proyecto,b.cDescri as Estado FROM H02PAUD a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '041' INNER JOIN S01MPER c ON c.cNroDni=a.cNroDni INNER JOIN H02MPRY d ON d.cIdproy=a.cIdProy LIMIT 200"
        # lcSql = "SELECT a.cIdProy,a.cDescri,a.cDniRes,b.cDescri FROM H02MPRY a INNER JOIN V_S01TTAB b ON TRIM(b.cCodigo) = a.cEstado AND b.cCodTab = '160' LIMIT 200" # vista con dni
        # lcSql = "SELECT cIdProy, cDescri, cDniRes, cEstado FROM H02MPRY('%s')%(lcJson) where cEstado ='A' ORDER BY cEvento DESC LIMIT 200"";
        # $lcSql = "SELECT cNroDni, cNombre FROM S01MPER
        # WHERE cEstado = 'A' AND (cNroDni = '$lcNroDni' OR cNombre LIKE '%$lcNroDni%') AND cNroDni NOT LIKE 'X%' ORDER BY cNombre";
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE INFORMACION"
            return False
        return True
   def onAprobarReq(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxAprobarReq()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   
   def __mxAprobarReq(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02DPRY1('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO SE PUEDE APROBAR"
            return False
        return True
   def onObservarReq(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxObservarReq()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   
   def __mxObservarReq(self):
        lcJson = json.dumps(self.paData)
        lcSql = "SELECT P_H02DPRY2('%s')" % (lcJson)
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO SE PUEDE OBASERVAR"
            return False
        return True


   def onAgreAuditor(self):
      return render_template('Ind1130.html')
   def onAuditoriaReq(self):
      return render_template('auditarrequisitos.html')


   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)

   """ def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def omTraerNombre(self):
      self.mxValidarNombre()
      self.mxTraerNombre()
      return render_template('Aud1110.html', name=self.cNombre)

   def mxValidarNombre(self):
   	return True

   def mxTraerNombre(self):
   	self.cNombre = 'YOssE'"""

   

