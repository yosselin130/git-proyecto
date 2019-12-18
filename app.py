'''from flask import Flask
from Clases.CAuditoria import CAuditoria
from Clases.CHome import CHome
from Clases.CLogin import CLogin
from Clases.CRegistro import CRegistro
from Clases.CProyecto import CProyecto
from Clases.CRevisarProyecto import CRevisarProyecto
from Clases.CRevisarReq import CRevisarReq
from Clases.CResponsables import CResponsables
from Clases.CRequisitos import CRequisitos
#from flask_bootstrap import Bootstrap
from os import path, walk
from flask import render_template, redirect, url_for, request,flash, session, abort
from werkzeug.datastructures import ImmutableMultiDict
import collections

UPLOAD_FOLDER = 'C:/tesis/visual/SGRSIA/archivos'

app = Flask(__name__)
#Bootstrap(app)
app.secret_key = 'super secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def f_InicioSesion():
   return render_template('index.html')

@app.route('/login', methods=['POST'])
def f_Login():
    x = request.form.to_dict()
    laData = f_GetDict(x, 'paData')
    if request.method == 'POST':
       lo = CLogin()
       lo.paData = laData
       llOk = lo.omLogin()
       if not llOk:
          print( '*** ERROR:', lo.pcError)
          return render_template('login.html', error = lo.pcError)
       else:
          return render_template('Mnu1000.html', error='')
    return 'YOSSELIN'



    #f = request.form.get('paData')
    #f = request.form.get()
    #f = request.form.post('paData')
    #f = request.form.post('paData[]')
    #f = request.form('paData')
    #f = request.args.get('paData', '')
    #f = request.args.get('paData')
    #f = request.args.get()
    #f = request.args.get('')
    #f = request.get_json().get('paData', '')
    f = request.values()
    print f
    print '-------------'
    print f.to_dict()
    print '-------------'
   
    #laData = request.form.get('pcNroDni')
    #laData = request.form.get('pcClave')
    #print(laData)
    for key in f.keys():
        for value in f.getlist(key):
            print key,":",value
    return render_template('login.html', error = '***')
    return 
    if request.method == 'POST':
       print(333)
       #laData= request.form.to_dict('paData')
       #laData = dict((key, request.form.getlist(key)) for key in request.form.keys())
       #laData = ImmutableMultiDict(request.form.to_dict('paData'))
       #laData=request.get_json('paData')
       laData = ImmutableMultiDict([(request.form.to_dict('paData'))])
       print (laData.getlist('paData'))
       #laData.to_dict()
       print(555)
       #x=laData.to_dict()
       print(laData.to_dict())
       #laData = request.form['paData']
       print(444)
       print (laData)
       lo = CLogin()
       lo.paData = laData
       llOk = lo.omLogin()
       if not llOk:
          print( '*** ERROR:', lo.pcError)
          return render_template('login.html', error = lo.pcError)
       else:
          return render_template('index.html', error=error)
    return 'YOSSELIN'
'''
# 2comentar
'''
@app.route('/home', methods=['GET', 'POST'])
def paginaprincipal():
   pp = CHome()
   lcResult = pp.onHome()
   return lcResult

@app.route('/registro', methods=['GET', 'POST'])
def f_Registro():
   re = CRegistro()
   lcResult = re.onRegistro()
   return lcResult

@app.route('/proyecto', methods=['GET', 'POST'])
def f_Proyecto():
   rpy = CProyecto()
   lcResult = rpy.onProyecto()
   return lcResult 

@app.route('/editarproyecto', methods=['GET', 'POST'])
def f_Editarproyecto():
   epy = CProyecto()
   lcResult = epy.onEditarProyecto()
   return lcResult 
@app.route('/crearproyecto', methods=['GET', 'POST'])
def f_Crearproyecto():
   cpy = CProyecto()
   lcResult = cpy.onCrearProyecto()
   return lcResult 

@app.route('/revisarauditoria', methods=['GET', 'POST'])
def f_RevisarAuditoria():
   ra = CAuditoria()
   lcResult = ra.onRevisarAuditoria()
   return lcResult 

@app.route('/auditoriareq', methods=['GET', 'POST'])
def f_AuditoriaReq():
   ar = CAuditoria()
   lcResult = ar.onAuditoriaReq()
   return lcResult 

@app.route('/agreauditor', methods=['GET', 'POST'])
def f_AgreAuditor():
   aga = CAuditoria()
   lcResult = aga.onAgreAuditor()
   return lcResult 

@app.route('/revisarproyectos', methods=['GET', 'POST'])
def f_RevisarProyectos():
   rp = CRevisarProyecto()
   lcResult = rp.onRevisarProyecto()
   return lcResult 

@app.route('/revisarreq', methods=['GET', 'POST'])
def f_RevisarReq():
   rr = CRevisarReq()
   lcResult = rr.onRevisarReq()
   return lcResult 

@app.route('/asigresponsables', methods=['GET', 'POST'])
def f_AsignacionRes():
   res = CResponsables()
   lcResult = res.onAsignacionRes()
   return lcResult 

@app.route('/mantresponsables', methods=['GET', 'POST'])
def f_MantRes():
   mres = CResponsables()
   lcResult = mres.onMantRes()
   return lcResult 

@app.route('/descreq', methods=['GET', 'POST'])
def f_DescReq():
   dreq = CRequisitos()
   lcResult = dreq.onDescargarReq()
   return lcResult 

@app.route('/subirreq', methods=['GET', 'POST'])
def f_SubirReq():
   sreq = CRequisitos()
   lcResult = sreq.onSubirReq()
   return lcResult 

@app.route('/crearreq', methods=['GET', 'POST'])
def f_CrearReq():
   creq = CRequisitos()
   lcResult = creq.onCrearReq()
   return lcResult 

@app.route('/progresoreq', methods=['GET', 'POST'])
def f_ProgresoReq():
   proreq = CRequisitos()
   lcResult = proreq.onProgReq()
   return lcResult 

def f_GetDict(paData, p_key):
   #laData = request.form.to_dict()
   #paData = {'paData[CNRODNI]': '47289024', 'paData[CCLAVE]': '1234', 'Boton0': 'IniciarSesion'}
   lcKey = '*'
   laDatos = collections.defaultdict(dict)
   for key in paData:
   	lnIndice = key.find('[')
   	if lnIndice != -1 :
   	   lcKey = key[:lnIndice]
   	   lcSubKey = key[lnIndice+1:key.find(']')]
   	   laDatos[lcKey][lcSubKey] = paData[key]
   	else:
   		lcKey = key
   		laDatos[lcKey] = paData[key]
   return laDatos[p_key]
if __name__ == '__main__':
   app.run( debug=True)

'''

from flask import Flask
from Clases.CBase import *
from Clases.CLogin import CLogin
from Clases.CRegistro import CRegistro
from Clases.CProyecto import CProyecto
from Clases.CRequisitos import CRequisitos
from Clases.CAuditoria import CAuditoria
from Clases.CResponsables import CResponsables
from os import path, walk
import os
import urllib.request
from datetime import timedelta
from datetime import datetime
from flask_datepicker import datepicker
from werkzeug.utils import secure_filename
from flask import send_from_directory, app, make_response, request, render_template, redirect, url_for, request, flash, session, abort
UPLOAD_FOLDER = '127.0.0.1:5000/static/archivos/'




app = Flask(__name__, static_url_path='')
app.config['DEBUG']
# Bootstrap(app)
app.secret_key = 'super secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.before_request
def before_request_func():
    if(session.get('log') is None and (request.endpoint != 'f_InicioSesion' and request.endpoint != 'f_Login' and request.endpoint != 'f_Registro' and request.endpoint != 'send_static')):
        return render_template('index.html', pcError='Tiempo expirado!')
@app.route('/')
def f_InicioSesion():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def f_Login():
    if request.method == 'POST':
        x = request.form.to_dict()
        laData = f_GetDict(x, 'paData')
        lo = CLogin()
        lo.paData = laData #usermane y pass
        llOk = lo.omLogin()
        if not llOk:
            resp = make_response(render_template('index.html', pcError=lo.pcError))
            return resp
        else:
            #session['']
            session["log"] = True
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=30)
            nombre = lo.paDatos['CNOMBRE'].replace('/', ' ')
            dni = lo.paDatos['CNRODNI']
            ''''session['dni'] = request.form["CNRODNI"]'''
            resp = make_response(render_template('Mnu1000.html', nombre=nombre))
            resp.set_cookie('dni', lo.paDatos['CNRODNI'])
            dni = request.cookies.get('dni')
            resp.set_cookie('nombre', lo.paDatos['CNOMBRE'])
            #print('cookie get success' + request.cookies.get('test'))
            return resp
    else:
        return render_template('index.html')

@app.route('/logout')
def f_Logout():
    if request.method == 'GET':
        session.pop("log", False)
        return render_template('index.html')

@app.route('/home')
def f_PaginaPrincipal():
    '''if "CNRODNI" in session:
       return "tu eres %s"  % escape(session["CNRODNI"])

    return "tu deberias logearte" '''
    return render_template('Mnu1000.html')


@app.route('/registro', methods=['GET', 'POST'])
def f_Registro():
    if request.method == 'POST':
        x = request.form.to_dict()
        laData = f_GetDict(x, 'paData')
        re = CRegistro()
        re.paData = laData
        llOk = re.omRegistro()
        if not llOk:
            return render_template('index.html', pcError=re.pcError)
        else:
            return render_template('registro.html', paDatos=re.paDatos)
    else:
        return render_template('registro.html')

#proyecto(crear,editar)
@app.route('/proyecto', methods=['GET', 'POST'])
def f_Proyecto():
    py = CProyecto()
    if request.method == 'POST':
        if  request.form.get("button0", False) == 'Proyectos':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData = laData
            llOk = py.omMostrarProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1110.html', pcError=py.pcError)
            else:
                return render_template('Ind1110_1.html', paDatos=py.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
           llOk = py.omMostrarEstados()
           dni = request.cookies.get('dni')
           nombre = request.cookies.get('nombre')
           nombre = nombre.replace('/', ' ')
           id_project = request.form['button0'] == 'Nuevo' and '*' or request.form['key']
           nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii']
           if request.form['button0'] == 'Nuevo':
               dni = request.cookies.get('dni')
               nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii'] 
               resp= request.form['button0'] == 'Nuevo' and request.cookies.get('nombre') or request.form['responsable'].replace('/', ' ')
               #print('mostrar dniiiii')
               #print (dni)
               return render_template('Ind1110.html', project = id_project ,paDatos=py.paDatos, cnrodni=nrodni,nombre=nombre, resp=resp)
           #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
           if request.form['button0'] == 'Editar' or request.form['key']:
               id_project = request.form['key']
               descri= request.form['descripcion']
               nrodni = request.form.get("dnii", False)
               resp = request.form.get("responsable", False)
               estado = request.form.get("estado", False)
               return render_template('Ind1110.html', project = id_project , descri=descri,cnrodni=nrodni,estado=estado, resp=resp, paDatos=py.paDatos, nombre=nombre)

           return render_template('Ind1110.html', project = id_project ,paDatos=py.paDatos, cnrodni=nrodni, nombre=nombre)
        if request.form.get("button1", False) == 'Grabar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData = laData
            llOk = py.omProyecto()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1110.html', pcError=py.pcError)
            else:
                dni = request.cookies.get('dni')
                return render_template('Ind1110.html',nombre=nombre)

        elif request.form.get("button1", False) == 'Cancelar':
            llOk = py.omMostrarProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1110_1.html', nombre=nombre,paDatos=py.paDatos)

        elif request.form.get("button0", False) == 'Salir':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html',nombre=nombre)
        
        if request.form.get("button1", False) == 'Editar1':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData = laData
            cIdProy = request.form.get('cIdProy')
            llOk = py.omEditarProyectos()
            if not llOk:
                return render_template('Ind1110.html', pcError=py.pcError)
            else:
                dni = request.cookies.get('dni')
                return render_template('Ind1110.html', cIdProy=cIdProy)
        elif request.form['button0'] == 'Cerrar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData =laData
            print(laData)
            llOk = py.omCerrarProyecto()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1140_2.html', pcError=py.pcError)
            else:
                llOk = py.omMostrarProyectos()
                return render_template('Ind1110_1.html', paDatos=py.paDatos,nombre=nombre)
            
#copia de crear py
'''@app.route('/crearproyecto', methods=['GET', 'POST'])
def f_Crearproyecto():
    py = CProyecto()
    if request.method == 'GET':
        llOk = py.omMostrarEstados()
        if not llOk:
            return render_template('Ind1110.html', pcError=py.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1110.html', paDatos=py.paDatos, dni=dni)
    else:
        x = request.form.to_dict()

        laData = f_GetDict(x, 'paData')
        py.paData = laData
        llOk = py.omProyecto()

        if not llOk:
            return render_template('Ind1110.html', pcError=py.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1110.html', success=py.paDatos, dni=dni)
    if request.method == 'POST':
        llOk = py.omMostrarEstados()
        if not llOk:
            return render_template('Ind1110.html', pcError=py.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1110.html', paDatos=py.paDatos, dni=dni)
    else:
        x = request.form.to_dict()

        laData = f_GetDict(x, 'paData')
        py.paData = laData
        llOk = py.omProyecto()

        if not llOk:
            return render_template('Ind1110.html', pcError=py.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1110.html', success=py.paDatos, dni=dni)'''


#requisitos(crear,editar)
@app.route('/requisito', methods=['GET', 'POST'])
def f_Requisito():
    re = CRequisitos()
    if request.method == 'POST':
        #if request.form['button0'] == 'Requisitos':
        if request.form.get("button0", False) == 'Requisitos':
        #request.form.get("something", False)
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            re = CRequisitos()
            re.paData = laData
            llOk = re.omMostrarRequisitos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1170.html', pcError=re.pcError)
            else:
                return render_template('Ind1130_1.html', paDatos=re.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False)== 'Editar' :
            llOk = re.omMostrarEstados()
            print("prueba")
            print(llOk)
            print(re.paDatos)
            dni = request.cookies.get('dni')
            cCodRequi = request.form['button0'] == 'Nuevo' and '*' or request.form['key']
            nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii']
            if request.form['button0'] == 'Nuevo':
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii']
                return render_template('Ind1170.html',cCodReq=cCodRequi, paDatos=re.paDatos, cnrodni=nrodni, nombre=nombre)
            if request.form['button0'] == 'Editar' or request.form['key']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                cCodRequi = request.form['key']
                descri= request.form['descripcion']
                estado = request.form.get("estado", False)
                nrodni = request.form.get("dnii", False)
                return render_template('Ind1170.html', cCodReq = cCodRequi , descri=descri, estado=estado,cnrodni=nrodni, nombre=nombre, paDatos=re.paDatos)

            return render_template('Ind1170.html', cCodReq = cCodRequi ,paDatos=re.paDatos, cnrodni=nrodni)
        if request.form.get("button1", False) == 'Grabar':
            print("datos")
            x = request.form.to_dict()
            print(x)
            laData = f_GetDict(x, 'paData')
            print(laData)
            re.paData = laData
            llOk = re.omRequisito()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1170.html', pcError=re.pcError)
            else:
                return render_template('Ind1170.html',nombre=nombre)
        elif request.form.get("button1", False) == 'Cancelar':
            llOk = re.omMostrarRequisitos()
            return render_template('Ind1130_1.html', paDatos=re.paDatos)
        elif request.form.get("button0", False) == 'Salir':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html',nombre=nombre)
        if request.form.get("button1", False) == 'Editar1':
            llOk = re.omMostrarRequisitos()
            cCodReq = request.form.get('cCodReq')
            print("#######codddddddd")
            print(cCodReq)
            return render_template('Ind1170.html', paDatos=re.paDatos,cCodReq=cCodReq )

@app.route('/auditor', methods=['GET', 'POST'])
def f_Auditor():
    au = CAuditoria()
    if request.method == 'POST':
        if request.form.get("button0", False) == 'Auditor':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.omMostrarAuditor()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1140_2.html', pcError=au.pcError)
            else:
                return render_template('Ind1140.html', paDatos=au.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
            llOk = au.omMostrarEstados()
            cCodAudi= request.form['button0'] == 'Nuevo' and '*' or request.form['codaud']
            if request.form['button0'] == 'Nuevo':
               nrodni= request.form['button0'] == 'Nuevo' or  request.form['dnii']
               dni = request.cookies.get('dni')
               nombre = request.cookies.get('nombre')
               nombre = nombre.replace('/', ' ')
               #print('mostrar dniiiii')
               #print (dni)
               return render_template('Ind1140_2.html', cCodAud =cCodAudi ,nombre=nombre, paDatos=au.paDatos)
            if request.form['button0'] == 'Editar' or request.form['codaud']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                cCodAudi = request.form['codaud']
                nrodni = request.form.get("dnii", False)
                cIdProy= request.form['proyecto']
                estado = request.form.get("estado", False)
                return render_template('Ind1140_2.html',  cCodAud =cCodAudi , cIdProy=cIdProy,cnrodni=nrodni,estado=estado, nombre=nombre, paDatos=au.paDatos)

            #return render_template('Ind1140_2.html', cCodAud =cCodAudi ,paDatos=au.paDatos, cnrodni=nrodni)
        if request.form.get("button1", False) == 'Grabar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.omAuditor()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1110.html', pcError=au.pcError)
            else:
                return render_template('Ind1140_2.html', nombre=nombre)
        elif request.form.get("button1", False) == 'Cancelar':
            llOk = au.omMostrarAuditor()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1140.html', paDatos=au.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Salir':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html',nombre=nombre)
        if request.form.get("button1", False) == 'Editar1':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.omEditarAuditor()
            dni = request.cookies.get('dni')
            if not llOk:
                return render_template('Ind1110.html', pcError=au.pcError)
            else:
                dni = request.cookies.get('dni')
                return render_template('Ind1140_2.html')
        elif request.form['button0'] == 'Guardar':
            return render_template('Mnu1000.html')

#repsonsable(crear,editar)
@app.route('/responsable', methods=['GET', 'POST'])
def f_Responsable():
    rp = CResponsables()
    if request.method == 'POST':      
        if request.form.get("button0", False) == 'Responsable':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            rp.paData = laData
            llOk = rp.omMostrarResponsable()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1120.html', pcError=rp.pcError)
            else:
                return render_template('Ind1120.html', paDatos=rp.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
           print('ssssssssssssssssssssssssssssssssss editar')
           print(request.form)
           print("prueba")
           print(rp.paDatos)
           #llOk = rp.omMostrarEstados()
           codigo = request.form['button0'] == 'Nuevo' and '*' or request.form['key']
           nrodni= request.form['button0'] == 'Nuevo' and request.form['dnii']
           if request.form['button0'] == 'Nuevo':
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                llOk= rp.omDevolverProyecto()
                llOk= rp.omDevolverRequisito()
                return render_template('Ind1140_1.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos)
           #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
           if request.form['button0'] == 'Editar' or request.form['key']:
               #a= rp.omDevolverProyecto()
               dni = request.cookies.get('dni')
               nombre = request.cookies.get('nombre')
               nombre = nombre.replace('/', ' ')
               id_project = request.form['key']
               codpy= request.form['codpy']
               codreq= request.form['codreq']
               nrodni = request.form.get("dnii", False)
               estado = request.form.get("estado", False)
               date = request.form.get("paData[TFECSUB]")
               info= request.form.get("paData[MINFOAD]")
               return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq, cnrodni=nrodni,estado=estado, nombre=nombre,paDatos=rp.paDatos)
           return render_template('Ind1140_1.html', cCodigo = codigo, paDatos=rp.paDatos, cnrodni=nrodni)
        if request.form.get("button1", False) == 'Grabar':
            print("datos")
            x = request.form.to_dict()
            print(x)
            laData = f_GetDict(x, 'paData')
            print(laData)
            rp.paData = laData
            llOk = rp.omAsignarResp()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1140_1.html', pcError=rp.pcError)
            else:
                return render_template('Ind1140_1.html',nombre=nombre)

        elif request.form.get("button1", False) == 'Cancelar':
            llOk = rp.omMostrarResponsable()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1120.html', paDatos=rp.paDatos, nombre=nombre)

        elif request.form.get("button0", False) == 'Salir':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html',nombre=nombre)
        
        elif request.form.get("button0", False) == 'Guardar':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1120.html', nombre=nombre)
    

        if request.form.get("button0", False) == 'Editar1':
            x = request.form.to_dict()
            print("e###############editar")
            print(x)
            laData = f_GetDict(x, 'paData')
            rp.paData = laData
            print(laData)
            cIdProy = request.form.get('cIdProy')
            print(cIdProy)
            llOk = rp.omEditarResponsable()
            if not llOk:
                return render_template('Ind1140_1.html', pcError=rp.pcError)
            else:
                dni = request.cookies.get('dni')
                return render_template('Ind1140_1.html', cIdProy=cIdProy)

        elif request.form.get("button0", False) =='Subir':
            cCodReq = request.form['button0'] == 'Subir' and request.form['codreq']
            nrodni= request.form['button0'] == 'Subir' and request.form['dnii']
            #request.form['button0'] == 'Subir' or request.form['codreq']:
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            cidproy=request.form['codpy']
            cCodReq = request.form['codreq']
            req= request.form['req']
            nrodni = request.form.get("dnii", False)
            resp = request.form.get("resp", False)
            estado = request.form.get("estado", False)
            cod = request.form.get("key", False)
            return render_template('Ind1130.html', cCodReq = cCodReq , cdescri=req, cnrodni=nrodni,cresp=resp, estado=estado, codigo=cod , cidproy=cidproy, nombre=nombre, paDatos=rp.paDatos)
        #return render_template('Ind1130.html', cCodReq = cCodReq ,paDatos=rp.paDatos, cnrodni=nrodni)

        if request.form.get("button1", False) =='Cargar':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No file selected for uploading')
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename).split('.')
                x = request.form.to_dict()
                x['paData[CARCHIVO]'] = filename[0]
                x['paData[CEXTENSION]'] = filename[1]
                print('dictionary')
                print(x)
                laData = f_GetDict(x, 'paData')
                print('=======================')
                print(laData)
                rp.paData = laData
                llOk = rp.omSubirArvhivo()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1140_1.html', pcError=rp.pcError)
                else:
                    file.save(os.path.join(
                        'C:/yoss/GIT/git-proyecto/static/archivos', file.filename))
                    flash('Se subío con éxito el archivo')
                    return render_template('Ind1130.html', nombre=nombre)
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return redirect('Ind1130.html')  
        else:
            if  request.form.get("button1", False) == 'Cancelar':
                llOk = rp.omMostrarResponsable()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
            return render_template('Ind1120.html', nombre=nombre, paDatos=rp.paDatos)
    
@app.route('/revisar', methods=['GET', 'POST'])
def f_Revisar():
    au = CAuditoria()
    if request.method == 'POST':
        if request.form.get("button0", False) == 'Revisar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.onMostraProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1150_1.html', pcError=au.pcError)
            else:
                print('salida================')
                print(au.paDatos)
                return render_template('Ind1150.html', paDatos=au.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Cancelar':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html', nombre=nombre)

        if request.form.get("button0", False) == 'Abrir_detalle':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            au.paData = request.form.get("paData[CIDPROY]")
            #au.paData=laData
            llOk = au.onMostraRequisitos()
            print('**********')
            print(au.paDatos)
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1150_1.html', nombre=nombre, paDatos=au.paDatos)
        
        elif request.form.get("button1", False) == 'Abrir_Requisito':
            llOk = au.onMostradetallereq()
            if request.form.get("button1", False) == 'Abrir_Requisito':
                llOk = au.omMostrarEstados2()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                serial = request.form['button1'] == 'Abrir_Requisito' and request.form['key']
                nrodni= request.form['button1'] == 'Abrir_Requisito' and  request.cookies.get('dni') or request.form['dnii']
                serial=request.form['key']
                cCodReq=request.form['codreq']
                codaud = request.form.get("codaud", False)
                fecha = request.form.get("paData[TFECSUB]", False)
                obs = request.form.get("paData[MOBSERV]", False)
                descri= request.form.get("descripcion", False)
                resp = request.form.get("responsable", False)
                archivo= request.form.get("archivo", False).strip()
                extension= request.form.get("extension", False)
                estado = request.form.get("estado", False)

                return render_template('Ind1150_2.html', archivo = archivo, extension = extension,  nserial=serial,codreq = cCodReq , ccodaud=codaud,fecha=fecha,dni=nrodni, descri=descri,resp=resp, estado=estado ,nombre=nombre,paDatos=au.paDatos)
            #return render_template('Ind1150_2.html', paDatos=au.paDatos, dni=dni)
        elif request.form.get("button1", False) == 'Cancelar':
            au.paData = request.form.get("paData[CIDPROY]")
            llOk = au.onMostraProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1150.html', paDatos=au.paDatos, nombre=nombre)

        if request.form.get("button2", False) == 'Aprobar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            print('================')
            print(laData)
            llOk = au.onAprobarReq()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1150_2.html', pcError=au.pcError)
            else:
                llOk = au.onMostradetallereq()
                return render_template('Ind1150_2.html',paDatos=rp.paDatos, nombre=nombre )
        elif request.form.get("button2", False) == 'Observar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.onObservarReq()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1150_2.html', pcError=au.pcError)
            else:
                llOk = au.onMostradetallereq()
                return render_template('Ind1150_2.html',paDatos=au.paDatos, nombre=nombre)
        if request.form.get("button2", False) == 'Cancelar':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            llOk = au.onMostraRequisitos()
            return render_template('Ind1150.html',  nombre=nombre, paDatos=au.paDatos)


if __name__ == '__main__':
    app.run(debug=True)

