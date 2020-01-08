from flask import render_template, redirect, url_for, request
import os
from flask import render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
import urllib.request
import json
import jinja2
import pdfkit

from Clases.CBase import *
from Clases.CSql import CSql

path_wkthmltopdf = r'C:\Program Files\Python35\Lib\site-packages\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
path = 'C:\\tesis\\visual\\bd\\local\\git-proyecto\\static\\archivos\\reporte\\'

class CReportes:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.loSql = CSql()
      self.pcError = ''
      
   
   def writePDFPry(self):
       templateLoader = jinja2.FileSystemLoader(searchpath="./static/archivos/reporte_html")
       templateEnv = jinja2.Environment(loader=templateLoader)
       TEMPLATE_FILE = "proyectos.html"
       template = templateEnv.get_template(TEMPLATE_FILE)
       
       outputText = template.render(paDatos= self.paDatos)

       html_file=open('proyectos.html','w')
       html_file.write(outputText)
       html_file.close()

       pdfkit.from_file('proyectos.html', path + 'proyectos.pdf', configuration = config)

   def writePDFReq(self):
       templateLoader = jinja2.FileSystemLoader(searchpath="./static/archivos/reporte_html")
       templateEnv = jinja2.Environment(loader=templateLoader)
       TEMPLATE_FILE = "requisitos.html"
       template = templateEnv.get_template(TEMPLATE_FILE)
       
       outputText = template.render(paDatos= self.paDatos)

       html_file=open('requisitos.html','w')
       html_file.write(outputText)
       html_file.close()

       pdfkit.from_file('requisitos.html', path + 'requisitos.pdf', configuration = config)
    
   def writePDFAva(self):
       templateLoader = jinja2.FileSystemLoader(searchpath="./static/archivos/reporte_html")
       templateEnv = jinja2.Environment(loader=templateLoader)
       TEMPLATE_FILE = "avance.html"
       template = templateEnv.get_template(TEMPLATE_FILE)
       
       outputText = template.render(paDatos= self.paDatos)

       html_file=open('avance.html','w')
       html_file.write(outputText)
       html_file.close()

   def writePDFEsPor(self):
       templateLoader = jinja2.FileSystemLoader(searchpath="./static/archivos/reporte_html")
       templateEnv = jinja2.Environment(loader=templateLoader)
       TEMPLATE_FILE = "estados.html"
       template = templateEnv.get_template(TEMPLATE_FILE)
       
       outputText = template.render(paDatos= self.paDatos)

       html_file=open('estados.html','w')
       html_file.write(outputText)
       html_file.close()

       pdfkit.from_file('estados.html', path + 'estados.pdf', configuration = config)

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
      
   def onMostraProyectosPDF(self):
       llOk = self.loSql.omConnect()
       if not llOk:
            self.pcError = self.loSql.pcError
            return False
       llOk = self.__mxMostraProyectosPDF()
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

   def __mxMostraProyectosPDF(self):
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
        self.writePDFPry()
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

   def onMostraRequisitosPDF(self):
       llOk = self.loSql.omConnect()
       if not llOk:
            self.pcError = self.loSql.pcError
            return False
       llOk = self.__mxMostraRequisitosPDF()
       if llOk:
            self.loSql.omCommit()
       self.loSql.omDisconnect()
       return llOk
   def __mxMostraRequisitosPDF(self):
        lcSql = "SELECT * FROM v_h02ppry_REP" 
        print('===============')
        print(lcSql)
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
        self.writePDFReq()
        return True
      
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
   def onMostradetallereqPDF(self):
      llOk = self.loSql.omConnect()
      if not llOk:
            self.pcError = self.loSql.pcError
            return False
      llOk = self.__mxMostradetallereqPDF()
      if llOk:
            self.loSql.omCommit()
      self.loSql.omDisconnect()
   def __mxMostradetallereqPDF(self):
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
            self.pcError = "NO TIENE PROYECTOS"
            return False
        self.writePDFAva()
        return True   
   def onAgreAuditor(self):
      return render_template('Ind1130.html')
   def onAuditoriaReq(self):
      return render_template('auditarrequisitos.html')
    
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
   def __mxDevolverDatos(self):
       #traer tabla de proyectos
        lcSql = "select cidproy, cdescri from h02mpry  WHERE cestado='A' order by cidproy"
        RS = self.loSql.omExecRS(lcSql)
        self.paProyecto = RS
        #traer tabla de personas
        lcSql = "select cNroDni,  replace(cNombre,'/',' ') from S01MPER where cestado='A' limit 200"
        RS = self.loSql.omExecRS(lcSql)
        self.paPersonas = RS
        #traer estados de puente de auditor -041
        lcSql = "SELECT trim(cDescri) FROM V_S01TTAB WHERE cCodTab='041'"
        RS = self.loSql.omExecRS(lcSql)
        self.paEstadosAuditor = RS
        #traer estado de detalle de proyecto -228
        lcSql = "SELECT cDescri FROM V_S01TTAB WHERE cCodTab='228'"
        RS = self.loSql.omExecRS(lcSql)
        self.paEstadoDetalleProyectos = RS
        '''if not RS[0][0]:
            self.pcError = 'ERROR AL EJECUTAR SQL. COMUNICARSE CON ADMINISTRADOR DEL SISTEMA'
            return False
        self.paDatos = RS
        print(type(self.paDatos))
        print(self.paDatos)
        if 'ERROR' in self.paDatos:
            self.pcError = self.paDatos['ERROR']
            return False
        return True'''
   def omDevolverAuditor(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxDevolverAuditor()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   def __mxDevolverAuditor(self):
        lcSql = "select cNroDni,  replace(cNombre,'/',' ') from S01MPER where cestado='A' LIMIT 200"
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
   def onMostraEstadosTotalPDF(self):
       llOk = self.loSql.omConnect()
       if not llOk:
            self.pcError = self.loSql.pcError
            return False
       llOk = self.__mxMostraEstadosTotalPDF()
       if llOk:
            self.loSql.omCommit()
       self.loSql.omDisconnect()
       return llOk
   def __mxMostraEstadosTotalPDF(self):
        lcSql = "SELECT * FROM v_h02ppry_porcentaje" 
        RS = self.loSql.omExecRS(lcSql)
        self.paDatos = RS
        i = 1
        if len(RS) == 0:
            self.pcError = "NO TIENE PROYECTOS"
            return False
        self.writePDFEsPor()
        return True

