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
from Clases.CReportes import CReportes
from os import path, walk
import os
import urllib.request
from datetime import timedelta
from datetime import datetime
import time
from flask_datepicker import datepicker
from werkzeug.utils import secure_filename
from flask import send_file, send_from_directory, app, make_response, request, render_template, redirect, url_for, request, flash, session, abort, jsonify
UPLOAD_FOLDER = '127.0.0.1:5000/static/archivos/'

path = 'C:\\tesis\\visual\\bd\\local\\git-proyecto\\static\\archivos\\reporte\\'


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
            tipo = lo.paDatos['CTIPO']
            print ("tipo")
            print(tipo)
            ''''session['dni'] = request.form["CNRODNI"]'''
            resp = make_response(render_template('Mnu1000.html', nombre=nombre,tipo=tipo))
            resp.set_cookie('dni', lo.paDatos['CNRODNI'])
            dni = request.cookies.get('dni')
            resp.set_cookie('nombre', lo.paDatos['CNOMBRE'])
            resp.set_cookie('tipo', lo.paDatos['CTIPO'])
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
    dni = request.cookies.get('dni')
    nombre = request.cookies.get('nombre')
    nombre = nombre.replace('/', ' ')
    '''if "CNRODNI" in session:
       return "tu eres %s"  % escape(session["CNRODNI"])

    return "tu deberias logearte" '''
    return render_template('Mnu1000.html', nombre=nombre)

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
            return render_template('registro.html', paDatos=re.paDatos, success=re.paDatos)
    else:
        return render_template('registro.html')

#proyecto(crear,editar)
@app.route('/proyecto', methods=['GET', 'POST'])
def f_Proyecto():
    py = CProyecto()
    ''' GET == RETORNA INFORMACION '''
    if request.method == 'GET':
        if request.args['autocomplete'] == 'Auditor':
            name = request.args['auditor']
            py.paData = name 
            llOk = py.onListarAuditores()
            return jsonify({'data':  py.paDatos})
            print("datos")
            print(py.paDatos)
    if request.method == 'GET':
        if request.args['autocomplete'] == 'Responsable':
            name = request.args['respon']
            py.paData = name 
            llOk = py.onListarResponsables()
            return jsonify({'data':  py.paDatos})
            print("datos")
            print(py.paDatos)
    dni = request.cookies.get('dni')
    nombre = request.cookies.get('nombre')
    nombre = nombre.replace('/', ' ')
    tipo=request.cookies.get('tipo')
    if tipo=='S':
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
                #dni = request.cookies.get('dni')
                #nombre = request.cookies.get('nombre')
                #nombre = nombre.replace('/', ' ')
                id_project = request.form['button0'] == 'Nuevo' and '*' or request.form['key']
                #nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii']
                nrodni= request.form['button0'] == 'Nuevo'  or  'None' or request.form['key']
                dniaud= request.form['button0'] == 'Nuevo' and  request.form['cnrodniaud'] or  'None'
                if request.form['button0'] == 'Nuevo'  :
                    #dni = request.cookies.get('dni')
                    #nrodni= request.form['button0'] == 'Nuevo' and request.cookies.get('dni') or request.form['dnii'] 
                    #nrodni= request.form['button0'] == 'Nuevo' and request.form['dnii']
                    resp= request.form['button0'] == 'Nuevo' and request.form['responsable']
                    nrodni= request.form['dnii']
                    cnrodniaud= request.form['cnrodniaud']
                    auditor= request.form['auditor']
                    resp= request.form['responsable']
                     
                    return render_template('Ind1110.html', project = id_project ,paDatos=py.paDatos, cnrodni=nrodni,nombre=nombre,cnrodniaud=cnrodniaud)
            #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
                if request.form['button0'] == 'Editar' or request.form['key']:
                    id_project = request.form['key']
                    descri= request.form['descripcion']
                    nrodni = request.form.get("dnii", False)
                    resp = request.form.get("responsable", False)
                    estado = request.form.get("estado", False)
                    cnrodniaud= request.form['cnrodniaud']
                    auditor= request.form['auditor']
                    return render_template('Ind1110.html', project = id_project , descri=descri,cnrodni=nrodni,estado=estado, resp=resp, paDatos=py.paDatos, nombre=nombre, cnrodniaud=cnrodniaud, auditor=auditor)

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
                        llOk = py.omMostrarProyectos()
                        dni = request.cookies.get('dni')
                        return render_template('Ind1110_1.html',nombre=nombre, success=py.paDatos,paDatos=py.paDatos)

            elif request.form.get("button1", False) == 'Cancelar':
                    llOk = py.omMostrarProyectos()
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    return render_template('Ind1110_1.html', nombre=nombre,paDatos=py.paDatos)

            if request.form.get("button0", False) == 'Salir':
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
    else:
        dni = request.cookies.get('dni')
        nombre = request.cookies.get('nombre')
        nombre = nombre.replace('/', ' ')
        return render_template('Mnu1000.html',nombre=nombre)
            #return False      
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
        tipo=request.cookies.get('tipo')
        if tipo=='S':
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
                    llOk = re.omMostrarRequisitos()
                    return render_template('Ind1130_1.html',nombre=nombre, success=re.paDatos,paDatos=re.paDatos)
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
        else:
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html',nombre=nombre)
            #return False      
@app.route('/auditor', methods=['GET', 'POST'])
def f_Auditor():
    au = CAuditoria()
    ''' GET == RETORNA INFORMACION '''
    if request.method == 'GET':
        if request.args['autocomplete'] == 'Auditor':
            name = request.args['auditor']
            au.paData = name 
            llOk = au.onListarAuditores()
            return jsonify({'data':  au.paDatos})
            print("datos")
            print(au.paDatos)
        
    ''' POST === RETORNA VISTA '''
    if request.method == 'POST':
        print('ingreso aca********************* nivel 0')
        print(request.form)
        print('end request form==============')
        if request.form.get('button2', False) == 'AutoComplete':
            print('entro aqui=============== nivel 1')
        if request.form.get("button0", False) == 'Auditor':
            #x = request.form.to_dict()
            #laData = f_GetDict(x, 'paData')
            #au.paData = laData
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            au.paData = dni
            llOk = au.omMostrarAuditor()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1140.html', pcError=au.pcError)
            else:
                return render_template('Ind1140.html', paDatos=au.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
            #llOk = au.omMostrarEstados()
            llOk = au.omDevolverDatos()
            #au.paProyecto = laData
            cCodAudi= request.form['button0'] == 'Nuevo' and '*' or 'None' or request.form['codaud']
            if request.form['button0'] == 'Nuevo':
               #nrodni= request.form['button0'] == 'Nuevo' or  request.form['dnii']
               cnrodni =  request.args.get('auditor')
               print('######dniiiiiiii')
               print(cnrodni)
               dni = request.cookies.get('dni')
               nombre = request.cookies.get('nombre')
               nombre = nombre.replace('/', ' ')
               #desproy= request.form['proyectodes']
               #print('mostrar dniiiii')
               #print (dni)
               return render_template('Ind1140_2.html', cCodAud =cCodAudi ,nombre=nombre, paDatos=au.paDatos ,paProyecto=au.paProyecto,cnrodni =cnrodni, paEstadosAuditor=au.paEstadosAuditor)
            if request.form['button0'] == 'Editar' or request.form['codaud']:
                if request.form['codaud'] =='None':
                    cCodAudi = '*'
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    cnrodni =  request.args.get('dnii',False)
                    cIdProy= request.form['proyecto'].strip()
                    desproy= request.form['proyectodes']
                    auditor=request.form['auditor']
                    return render_template('Ind1140_2.html',  cCodAud =cCodAudi , cIdProy=cIdProy, nombre=nombre, paDatos=au.paDatos,paProyecto=au.paProyecto , paEstadosAuditor=au.paEstadosAuditor, cnrodni =cnrodni,desproy=desproy,auditor=auditor)
                else:
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    cCodAudi = request.form['codaud']
                    cnrodni =  request.args.get('dnii',False)
                    cIdProy= request.form['proyecto'].strip()
                    desproy= request.form['proyectodes']
                    auditor=request.form['auditor']
                    return render_template('Ind1140_2.html',  cCodAud =cCodAudi , cIdProy=cIdProy, nombre=nombre, paDatos=au.paDatos,paProyecto=au.paProyecto , paEstadosAuditor=au.paEstadosAuditor, cnrodni =cnrodni,desproy=desproy,auditor=auditor)

            #return render_template('Ind1140_2.html', cCodAud =cCodAudi ,paDatos=au.paDatos, cnrodni=nrodni)
        if request.form.get("button1", False) == 'Grabar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.omAuditor()
            print(llOk)
            print("#############################")
            print('data')
            print(au.paData)
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1110.html', pcError=au.pcError)
            else:
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.omMostrarAuditor()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1140.html', nombre=nombre,  success=au.paDatos, paDatos=au.paDatos)
        elif request.form.get("button1", False) == 'Cancelar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            au.paData = dni
            llOk = au.omMostrarAuditor()
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
    
        if request.form.get("button0", False)== 'Requisitos':
                nSerial= request.form['button0'] == 'Requisitos' and '*' or request.form['nSerial']
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1140_3.html' ,nSerial=nSerial, nombre=nombre, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =dni)
        elif request.form.get("button2", False) == 'Grabar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            au.paData = laData
            llOk = au.onAsigReqAu()
            print(llOk)
            print("#############################")
            print('data')
            print(au.paData)
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            print("**************llok")
            print(llOk)
            '''if not llOk:
                return render_template('Ind1110.html', pcError=au.pcError)
                print(au.pcError)
            else:'''
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            au.paData = dni
            llOk = au.omMostrarAuditor()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1140.html', nombre=nombre,  success=au.paDatos,  paDatos=au.paDatos)
        if request.form.get("button2", False) == 'Cancelar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            au.paData = dni
            llOk = au.omMostrarAuditor()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1140.html', paDatos=au.paDatos, nombre=nombre)
        elif request.form.get("button0", False)== 'Abrir_Requisitos':
                '''nSerial= request.form['button0'] == 'Requisitos' and '*' 
                cCodAudi = request.form['codaud']
                cnrodni =  request.args.get('auditor',False)
                cIdProy= request.form['proyecto'].strip()
                desproy= request.form['proyectodes']
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')'''

                ###########pruebaaaaaa
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni').strip()
                codpy=request.form.get("proyecto").strip()
                datos=list({dni,codpy})
                au.paData=datos   
                datos_f=(au.paData[0],au.paData[1])
                au.paData=datos_f
                desproy= request.form.get("proyectodes")
                llOk = au.onMostrarReqAu()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                #return render_template('Ind1140_3.html', nombre=nombre, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =dni,desproy=desproy)
                return render_template('Ind1140_4.html', nombre=nombre,  success=au.paDatos,  paDatos=au.paDatos,desproy=desproy)'''
                nSerial=  request.form['button0'] == 'Abrir_Requisitos' and '*' or request.form['nserial']
                cnrodni= request.form['button0'] == 'Abrir_Requisitos' and  request.cookies.get('dni') or request.form['dnii']
                nSerial= '*'
                cCodAudi = request.form['codaud']
                ccodigo= request.args.get('ccodigo',False)
                desreq= request.args.get('desreq',False)
                auditor=request.args.get('auditor',False)
                cIdProy= request.form['proyecto'].strip()
                desproy= request.form['proyectodes']
                print('proyecto')
                print(desproy)
                estado = request.form.get("estado", False)
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                x = request.form.to_dict()
                '''laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni').strip()
                codpy=request.form.get("proyecto").strip()
                datos=list({dni,codpy})
                au.paData=datos   
                #datos_f=(au.paData[0],au.paData[1])
                #au.paData=datos_f
                desproy= request.form.get("proyectodes")
                llOk = au.onMostrarReqAu()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')'''
                return render_template('Ind1140_3.html', nombre=nombre,nSerial=nSerial, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =cnrodni,desproy=desproy,cCodReq=ccodigo)
        if request.form.get("button5", False) == 'Salir':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            au.paData = dni
            llOk = au.omMostrarAuditor()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1140.html', paDatos=au.paDatos, nombre=nombre)
        if  request.form.get("button5", False)== 'Asignar_Requisitos':
                nSerial=  request.form['button5'] == 'Asignar_Requisitos' and request.form['nserial']
                cnrodni= request.form['button5'] == 'Asignar_Requisitos' and  request.cookies.get('dni') or request.form['dnii']
                nSerial = request.form['nserial']
                cCodAudi = request.form['codaud']
                ccodigo= request.form['ccodigo']
                desreq= request.form['desreq']
                auditor=request.args.get('auditor',False)
                cIdProy= request.form['proyecto'].strip()
                desproy= request.form['proyectodes']
                print('proyecto')
                print(desproy)
                estado = request.form.get("estado", False)
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                x = request.form.to_dict()
                '''laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni').strip()
                codpy=request.form.get("proyecto").strip()
                datos=list({dni,codpy})
                au.paData=datos   
                #datos_f=(au.paData[0],au.paData[1])
                #au.paData=datos_f
                desproy= request.form.get("proyectodes")
                llOk = au.onMostrarReqAu()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')'''
                return render_template('Ind1140_3.html', nombre=nombre,nSerial=nSerial, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =cnrodni,desproy=desproy,cCodReq=ccodigo)
                #return render_template('Ind1140_4.html', nombre=nombre,  success=au.paDatos,  paDatos=au.paDatos,desproy=desproy)
        elif request.form.get("button5", False) == 'Nuevo' or request.form.get("button5", False) == 'Editar' :
            #llOk = au.omMostrarEstados()
            llOk = au.omDevolverDatos()
            #au.paProyecto = laData
            nSerial= request.form['button5'] == 'Nuevo' and '*' or request.form['nserial']
            if request.form['button5'] == 'Nuevo':
               #nrodni= request.form['button0'] == 'Nuevo' or  request.form['dnii']
                nSerial= '*'
                cCodAudi =  request.args.get('codaud',False)
                cnrodni =  request.args.get('dnii',False)
                ccodigo = request.args.get('ccodigo',False)
                desreq = request.args.get('desreq',False)
                auditor=request.args.get('auditor',False)
                cIdProy= request.args.get('proyecto',False)
                desproy= request.args.get('proyectodes',False)
                print("proyecto")
                print(desproy)
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1140_3.html', nombre=nombre,nSerial=nSerial, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =dni,desproy=desproy,cCodReq=ccodigo,desreq=desreq)
            if request.form['button5'] == 'Editar' or request.form['nserial']:
                nSerial= request.form['nserial']
                cCodAudi = request.form['codaud']
                cnrodni =  request.args.get('dnii',False)
                ccodigo = request.args.get('ccodigo',False)
                desreq = request.args.get('desreq',False)
                auditor=request.args.get('auditor',False)
                cIdProy= request.form['proyecto'].strip()
                desproy= request.form['proyectodes']
                llOk = au.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1140_3.html', nombre=nombre,nSerial=nSerial, paDatos=au.paDatos,paAuditor=au.paAuditor, paRequisito=au.paRequisito  , paEstadoDetalleProyectos=au.paEstadoDetalleProyectos, dni =dni,desproy=desproy,cCodReq=ccodigo,desreq=desreq)
#repsonsable(crear,editar)
@app.route('/responsable', methods=['GET', 'POST'])
def f_Responsable():
    rp = CResponsables()
    ''' GET == RETORNA INFORMACION '''
    if request.method == 'GET':
        if request.args['autocomplete'] == 'Responsable':
            name = request.args['responsable'] 
            rp.paData = name 
            llOk = rp.onListarResponsables()
            print('===============')
            print(rp.paDatos)
            return jsonify({'data':  rp.paDatos})
    tipo=request.cookies.get('tipo')
    if tipo!='S':
        ''' POST === RETORNA VISTA '''
        if request.method == 'POST':      
            if request.form.get("button0", False) == 'Responsable':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1120.html', pcError=rp.pcError)
                else:
                    return render_template('Ind1120_1.html', paDatos=rp.paDatos, nombre=nombre)
            elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
                print('ssssssssssssssssssssssssssssssssss editar')
                print(request.form)
                print("prueba")
                print(rp.paDatos)
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                codpy= request.form.get('codpy')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = codpy
                #llOk = rp.omMostrarEstados()
                llOk = rp.omDevolverDatos()
                codigo = request.form['button0'] == 'Nuevo' and '*' or 'None' or request.form['key']
                nrodni= request.form['button0'] == 'Nuevo' and request.args.get('dnii',False)
                if request.form['button0'] == 'Nuevo':
                    '''codpy= request.form['codpy']
                    py=request.form['py']'''
                    boton='Nuevo'
                    print("boton")
                    print(boton)
                    py=request.form.get('py')
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    return render_template('Ind1140_1.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, paPersonas=rp.paPersonas, py=py,cIdProy=codpy, boton=boton)
                #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
                if request.form['button0'] == 'Editar' or request.form['key'] or  request.form.get('codpy') :
                    #a= rp.omDevolverProyecto()
                    if request.form['key'] =='None' :
                            codigo = '*'
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            codpy= request.form.get('codpy')
                            py=request.form.get('py')
                            print("codigo py traido")
                            print(codpy)
                            print(py)
                            codreq= request.form['codreq']
                            req= request.form['req']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni =  request.args.get('dnii',False)
                            estado = request.form.get("estado", False)
                            resp=request.form.get("resp", False)
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py, req=req ,resp=resp)
                    else:
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            codigo= request.form['key']
                            codpy= request.form.get('codpy')
                            py=request.form.get('py')
                            print("codigo py recueperadoo")
                            print(codpy)
                            print(py)
                            codreq= request.form['codreq']
                            req= request.form['req']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni = request.form.get("dnii")
                            estado = request.form.get("estado")
                            resp=request.form.get("resp")
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py, req=req ,resp=resp)

                return render_template('Ind1140_1.html', cCodigo = codigo, paDatos=rp.paDatos, cnrodni=nrodni, nombre=nombre)
            if request.form.get("button2", False) == 'Grabar':
                print("datos")
                ''' x = request.form.to_dict()
                print(x)
                laData = f_GetDict(x, 'paData')
                print(laData)
                rp.paData = laData
                llOk = rp.omAsignarResp()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #dni = request.cookies.get('dni')
                #rp.paData = dni
                codpy=request.form.get("codpy")
                descri= request.form.get("py")
                #datos=list({codpy,dni})
                rp.paData=codpy       
                #llOk = rp.onMostraRequisitos()
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html',nombre=nombre,  success=rp.paDatos, paDatos=rp.paDatos, py= descri,cIdProy=codpy)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni')
                print('laData*************')
                print(laData)
                #rp.paData = laData
                print("#######padataaaa")
                print(laData)
                codpy=request.form.get("paData[CIDPROY]")
                #datos=list({codpy,dni})
                rp.paData=codpy           
                #rp.paproy = request.form.get("codpy") 
                #datos_f=(rp.paData[0],rp.paData[1])
                #rp.paData=datos_f
                print("datosss finales")
                print(rp.paData)
                descri= request.form.get("paData[CDESCRI]")
                print('**********')
                #au.paData=laData
                llOk = rp.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120.html',nombre=nombre, paDatos=rp.paDatos, py= descri,cIdProy=codpy)
            elif request.form.get("button1", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html', paDatos=rp.paDatos, nombre=nombre)
            if  request.form.get("button4", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html', paDatos=rp.paDatos, nombre=nombre)

            elif request.form.get("button0", False) == 'Salir':
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Mnu1000.html',nombre=nombre)    

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
                '''cCodReq = request.form['button0'] == 'Subir' and request.form['codreq']
                nrodni= request.form['button0'] == 'Subir' and request.form['dnii']
                #request.form['button0'] == 'Subir' or request.form['codreq']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                cidproy=request.form['codpy']
                py=request.form['py']
                cCodReq = request.form['codreq']
                req= request.form['req']
                nrodni = request.form.get("dnii", False)
                resp = request.form.get("resp", False)
                estado = request.form.get("estado", False)
                cod = request.form.get("key", False)
                return render_template('Ind1130.html', cCodReq = cCodReq , cdescri=req, cnrodni=nrodni,cresp=resp, estado=estado, codigo=cod , cidproy=cidproy, nombre=nombre, paDatos=rp.paDatos,py=py)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html',nombre=nombre,  paDatos=rp.paDatos)  
            #return render_template('Ind1130.html', cCodReq = cCodReq ,paDatos=rp.paDatos, cnrodni=nrodni)

            elif request.form.get("button4", False) =='subir_Requisitos':
                cCodReq = request.form['button4'] == 'subir_Requisitos' and request.form['codreq']
                #nrodni= request.form['button4'] == 'subir_Requisitos' and request.form['dnii']
                #request.form['button0'] == 'Subir' or request.form['codreq']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                #cidproy=request.form['codpy']
                #py=request.form['py']
                cCodReq = request.form['codreq']
                cidpy= request.form.get("cidpy", False)
                py= request.form.get("py", False)
                req= request.form['req']
                nrodni = request.form.get("dni", False)
                resp = request.form.get("responsable", False)
                estado = request.form.get("estado", False)
                cod = request.form.get("key", False)
                return render_template('Ind1130.html', cCodReq = cCodReq , cdescri=req,cresp=resp, estado=estado, codigo=cod , nombre=nombre, paDatos=rp.paDatos, cnrodni=nrodni,py=py,cidproy=cidpy)
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
                            'C:/tesis/visual/bd/local/git-proyecto/static/archivos', file.filename))
                        flash('Se subío con éxito el archivo')
                        x = request.form.to_dict()
                        laData = f_GetDict(x, 'paData')
                        dni = request.cookies.get('dni')
                        rp.paData = dni
                        llOk = rp.omMostrarResponsable1()
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        return render_template('Ind1120_1.html', nombre=nombre,  paDatos=rp.paDatos, success=rp.paDatos)
                else:
                    flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                    return redirect('Ind1130.html')  
            elif request.form.get("button3", False) == 'Salir':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                llOk = rp.omMostrarResponsable1()
                return render_template('Ind1120_1.html',nombre=nombre, paDatos=rp.paDatos)   
            if request.form.get("button3", False) == 'Abrir':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni')
                print('laData*************')
                print(laData)
                #rp.paData = laData
                print("#######padataaaa")
                print(laData)
                codpy=request.form.get("codpy")
                datos=list({dni,codpy})
                #d=list(datos)
                #d = d.split(']')
                #d = d.replace('}', ' ')
                print("tipo")
                print(type(datos))
                rp.paData=datos           
                #rp.paproy = request.form.get("codpy") 
                print('**********datoss')
                print(datos)
                print(rp.paData[0])
                print(rp.paData[1])
                datos_f=(rp.paData[0],rp.paData[1])
                rp.paData=datos_f
                print("datosss finales")
                print(rp.paData)
                descri= request.form.get("py")
                print('**********')
                #au.paData=laData
                llOk = rp.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_2.html',nombre=nombre, paDatos=rp.paDatos, desproy= descri)  
            elif request.form.get("button3", False) == 'Abrir_req':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni')
                print('laData*************')
                print(laData)
                #rp.paData = laData
                print("#######padataaaa")
                print(laData)
                codpy=request.form.get("codpy")
                #datos=list({codpy,dni})
                rp.paData=codpy           
                #rp.paproy = request.form.get("codpy") 
                #datos_f=(rp.paData[0],rp.paData[1])
                #rp.paData=datos_f
                print("datosss finales")
                print(rp.paData)
                descri= request.form.get("py")
                print('**********')
                #au.paData=laData
                llOk = rp.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120.html',nombre=nombre, paDatos=rp.paDatos, py= descri,cIdProy=codpy)  
            if  request.form.get("button2", False) == 'Cancelar':
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html', paDatos=rp.paDatos, nombre=nombre)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                dni = request.cookies.get('dni')
                print('laData*************')
                print(laData)
                #rp.paData = laData
                print("#######padataaaa")
                print(laData)
                codpy=request.form.get("paData[CIDPROY]")
                #datos=list({codpy,dni})
                rp.paData=codpy           
                #rp.paproy = request.form.get("codpy") 
                #datos_f=(rp.paData[0],rp.paData[1])
                #rp.paData=datos_f
                print("datosss finales")
                print(rp.paData)
                descri= request.form.get("paData[CDESCRI]")
                print('**********')
                #au.paData=laData
                llOk = rp.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120.html',nombre=nombre, paDatos=rp.paDatos, py= descri,cIdProy=codpy)
            elif  request.form.get("button0", False) == 'abrir_req':
                print('ssssssssssssssssssssssssssssssssss editar')
                print(request.form)
                print("prueba")
                print(rp.paDatos)
                #llOk = rp.omMostrarEstados()
                llOk = rp.omDevolverDatos()
                codigo = request.form['button0'] == 'abrir_req' and '*' or 'None' or request.form['key']
                nrodni= request.form['button0'] == 'Nuevo' and request.form['dnii']
                if request.form['button0'] == 'Nuevo':
                        dni = request.cookies.get('dni')
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        return render_template('Ind1140_1.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, paPersonas=rp.paPersonas)
                #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
                if request.form['button0'] == 'abrir_req' or request.form['key']:
                    #a= rp.omDevolverProyecto()
                    if request.form['key'] =='None':
                            codigo = '*'
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            id_project = request.form['key']
                            codpy= request.args.get('codpy',False)
                            py=request.form['py']
                            codreq= request.form['codreq']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni =  request.args.get('auditor',False)
                            estado = request.form.get("estado", False)
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)
                    else:
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            codigo= request.form['key']
                            id_project = request.form['key']
                            codpy= request.args.get('codpy',False)
                            py=request.form['py']
                            codreq= request.form['codreq']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni =  request.args.get('auditor',False)
                            estado = request.form.get("estado", False)
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)
            if  request.form.get("button5", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1120.html', pcError=rp.pcError)
                else:
                    return render_template('Ind1120.html', paDatos=rp.paDatos, nombre=nombre)
            elif request.form.get("button1", False) == 'Nuevo' :
                print('ssssssssssssssssssssssssssssssssss editar')
                print(request.form)
                print("prueba")
                print(rp.paDatos)
                #llOk = rp.omMostrarEstados()
                llOk = rp.omDevolverDatos()
                codigo = request.form['button1'] == 'Nuevo' and '*' or 'None' or request.form['key']
                nrodni= request.form['button1'] == 'Nuevo' and request.form['dnii']
                if request.form['button1'] == 'Nuevo':
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    return render_template('Ind1140_5.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, paPersonas=rp.paPersonas)

            if request.form.get("button0", False) == 'Eliminar':
                print("datos")
                x = request.form.to_dict()
                print(x)
                laData = f_GetDict(x, 'paData')
                rp.paData = laData
                print(laData)
                '''codpy= request.form.get('codpy')
                cod=request.form['key']
                codreq= request.form['codreq']'''
               
                llOk = rp.omEliminarReq()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #dni = request.cookies.get('dni')
                #rp.paData = dni
                codpy=request.form.get("codpy")
                descri= request.form.get("py")
                #datos=list({codpy,dni})
                rp.paData=codpy       
                #llOk = rp.onMostraRequisitos()
                llOk = rp.omMostrarResponsable1()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html',nombre=nombre,  success=rp.paDatos, paDatos=rp.paDatos, py= descri,cIdProy=codpy)
    else:
        dni = request.cookies.get('dni')
        nombre = request.cookies.get('nombre')
        nombre = nombre.replace('/', ' ')
        return render_template('Mnu1000.html',nombre=nombre)

@app.route('/revisar', methods=['GET', 'POST'])
def f_Revisar():
    au = CAuditoria()
    dni = request.cookies.get('dni')
    nombre = request.cookies.get('nombre')
    nombre = nombre.replace('/', ' ')
    tipo=request.cookies.get('tipo')
    if tipo!='S':
        if request.method == 'POST':
            if request.form.get("button0", False) == 'Revisar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1150_1.html', pcError=au.pcError)
                else:
                    return render_template('Ind1150.html', paDatos=au.paDatos, nombre=nombre)
            elif request.form.get("button0", False) == 'Cancelar':
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Mnu1000.html', nombre=nombre)
            #abre requisitos
            if request.form.get("button0", False) == 'Abrir_detalle':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                codpy=request.form.get("paData[CIDPROY]").strip()
                dni = request.cookies.get('dni').strip()
                datos=list({codpy,dni})
                au.paData=datos   
                datos_f=(au.paData[1],au.paData[0])
                au.paData=datos_f
                descri= request.form.get("paData[CDESCRI]")
                llOk = au.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150_1.html',nombre=nombre,  paDatos=au.paDatos, desproy= descri, success=au.paDatos)  
            elif request.form.get("button1", False) == 'Abrir_Requisito':
                llOk = au.onMostradetallereq()
                if request.form.get("button1", False) == 'Abrir_Requisito':
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
                    cidproy=request.form.get("cidproy", False)
                    proy=request.form.get("proy", False)
                    resp = request.form.get("responsable", False)
                    archivo= request.form.get("archivo", False).strip()
                    extension= request.form.get("extension", False)
                    estado = request.form.get("estado", False)
                    return render_template('Ind1150_2.html', archivo = archivo, extension = extension,  nserial=serial,codreq = cCodReq , ccodaud=codaud,fecha=fecha,dni=nrodni, descri=descri,resp=resp, estado=estado ,nombre=nombre,paDatos=au.paDatos, proy=proy,cidproy=cidproy)
                #return render_template('Ind1150_2.html', paDatos=au.paDatos, dni=dni)
            if request.form.get("button1", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150.html', paDatos=au.paDatos, nombre=nombre)

            elif request.form.get("button2", False) == 'Aprobar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                au.paData = laData
                llOk = au.onAprobarReq()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                '''if not llOk:
                    return render_template('Ind1150_1.html', pcError=au.pcError)
                else:
                    x = request.form.to_dict()
                    laData = f_GetDict(x, 'paData')
                    print('laData*************')
                    print(laData)
                    dni = request.cookies.get('dni')
                    au.paData = dni
                    llOk = au.onMostraProyectos()
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    return render_template('Ind1150.html',paDatos=au.paDatos, nombre=nombre, success=au.paDatos)'''
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                return render_template('Ind1150.html',paDatos=au.paDatos, nombre=nombre,success=au.paDatos)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                codpy=request.form.get("paData[CIDPROY]").strip()
                dni = request.cookies.get('dni').strip()
                datos=list({codpy,dni})
                au.paData=datos   
                datos_f=(au.paData[1],au.paData[0])
                au.paData=datos_f
                descri= request.form.get("paData[CDESCRI]")
                llOk = au.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150_1.html',nombre=nombre,  paDatos=au.paDatos, desproy= descri, success=au.paDatos)  
            if request.form.get("button2", False) == 'Observar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                au.paData = laData
                print('================')
                print(laData)
                llOk = au.onObservarReq()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                '''if not llOk:
                    #llOk = au.onMostraProyectos()
                    return render_template('Ind1150_1.html', pcError=au.pcError)
                else:'''
                    #llOk = au.onMostradetallereq()
                #lleva a tabla de revision py
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                return render_template('Ind1150.html',paDatos=au.paDatos, nombre=nombre)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                codpy=request.form.get("paData[CIDPROY]").strip()
                dni = request.cookies.get('dni').strip()
                datos=list({codpy,dni})
                au.paData=datos   
                datos_f=(au.paData[1],au.paData[0])
                au.paData=datos_f
                descri= request.form.get("paData[CDESCRI]")
                llOk = au.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150_1.html',nombre=nombre,  paDatos=au.paDatos, desproy= descri, success=au.paDatos)  
            elif request.form.get("button2", False) == 'Cancelar':
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150.html',  nombre=nombre, paDatos=au.paDatos)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                codpy=request.form.get("paData[CIDPROY]").strip()
                dni = request.cookies.get('dni').strip()
                datos=list({codpy,dni})
                au.paData=datos   
                datos_f=(au.paData[1],au.paData[0])
                au.paData=datos_f
                descri= request.form.get("paData[CDESCRI]")
                llOk = au.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150_1.html',nombre=nombre,  paDatos=au.paDatos, desproy= descri, success=au.paDatos)  
            if request.form.get("button0", False) == 'Auditado':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                au.paData =laData
                dni = request.cookies.get('dni')
                id=request.form['paData[CCODIGO]']
                idproy=request.form['paData[CIDPROY]']
                descri= request.form.get("paData[CDESCRI]")
                idreq=request.form['paData[CCODREQ]']
                dnii=request.form['paData[CNRODNI]']
                llOk = au.onAuditarProy()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                '''if not llOk:
                    return render_template('Ind1140_2.html', pcError=au.pcError)
                else:'''
                '''x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                au.paData = dni
                llOk = au.onMostraProyectos()
                return render_template('Ind1150.html', paDatos=au.paDatos,nombre=nombre,dnii=dnii)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                codpy=request.form.get("paData[CIDPROY]").strip()
                dni = request.cookies.get('dni').strip()
                datos=list({codpy,dni})
                au.paData=datos   
                datos_f=(au.paData[1],au.paData[0])
                au.paData=datos_f
                descri= request.form.get("paData[CDESCRI]")
                llOk = au.onMostraRequisitos()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1150_1.html',nombre=nombre,  paDatos=au.paDatos, desproy= descri, success=au.paDatos,dnii=dnii)  
    else:
        dni = request.cookies.get('dni')
        nombre = request.cookies.get('nombre')
        nombre = nombre.replace('/', ' ')
        return render_template('Mnu1000.html',nombre=nombre)
#subir requisitos
@app.route('/subir', methods=['GET', 'POST'])
def f_Responsable_subir():
    rp = CResponsables()
    ''' GET == RETORNA INFORMACION '''
    if request.method == 'GET':
        if request.form.get("autocomplete", False) == 'Responsable':
            name = request.args['responsable'] 
            rp.paData = name 
            llOk = rp.onListarResponsables()
            print('===============')
            print(rp.paDatos)
            return jsonify({'data':  rp.paDatos})
    dni = request.cookies.get('dni')
    nombre = request.cookies.get('nombre')
    nombre = nombre.replace('/', ' ')
    tipo=request.cookies.get('tipo')
    if tipo!='S':
        ''' POST === RETORNA VISTA '''
        if request.method == 'POST':      
            if request.form.get("button0", False) == 'Subir':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsableArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1120_3.html', pcError=rp.pcError)
                else:
                    return render_template('Ind1120_3.html', paDatos=rp.paDatos, nombre=nombre)
            elif request.form.get("button0", False) == 'Nuevo' or request.form.get("button0", False) == 'Editar' :
                print('ssssssssssssssssssssssssssssssssss editar')
                print(request.form)
                print("prueba")
                print(rp.paDatos)
                #llOk = rp.omMostrarEstados()
                llOk = rp.omDevolverDatos()
                codigo = request.form['button0'] == 'Nuevo' and '*' or 'None' or request.form['key']
                nrodni= request.form['button0'] == 'Nuevo' and request.form['dnii']
                if request.form['button0'] == 'Nuevo':
                        dni = request.cookies.get('dni')
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        return render_template('Ind1140_1.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, paPersonas=rp.paPersonas)
                #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
                if request.form['button0'] == 'Editar' or request.form['key']:
                    #a= rp.omDevolverProyecto()
                    if request.form['key'] =='None':
                            codigo = '*'
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            id_project = request.form['key']
                            codpy= request.args.get('codpy',False)
                            py=request.form['py']
                            codreq= request.form['codreq']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni =  request.args.get('auditor',False)
                            estado = request.form.get("estado", False)
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)
                    else:
                            dni = request.cookies.get('dni')
                            nombre = request.cookies.get('nombre')
                            nombre = nombre.replace('/', ' ')
                            codigo= request.form['key']
                            id_project = request.form['key']
                            codpy= request.args.get('codpy',False)
                            py=request.form['py']
                            codreq= request.form['codreq']
                            #nrodni = request.form.get("dnii", False)
                            cnrodni =  request.args.get('auditor',False)
                            estado = request.form.get("estado", False)
                            date = request.form.get("paData[TFECSUB]")
                            info= request.form.get("paData[MINFOAD]")
                            return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)

                return render_template('Ind1140_1.html', cCodigo = codigo, paDatos=rp.paDatos, cnrodni=nrodni, nombre=nombre)

            if request.form.get("button1", False) == 'Cancelar':
               x = request.form.to_dict()
               laData = f_GetDict(x, 'paData')
               #laData =('paData')
               print('laData*************')
               print(laData)
               #rp.paData = laData
               print("#######padataaaa")
               print(laData)
               codpy=request.form.get("paData[CIDPROY]")
               dni = request.cookies.get('dni')
               datos=list({codpy,dni})
               print("tipo")
               print(type(datos))
               rp.paData=datos           
               print('**********datoss')
               print(datos)
               print(rp.paData[0])
               print(rp.paData[1])
               datos_f=(rp.paData[1],rp.paData[0])
               rp.paData=datos_f
               print("datosss finales")
               print(rp.paData)
               descri= request.form.get('paData[CDESCRI]')
               observ =request.form.get('observ')
               print('**********')
               print(observ)
               #au.paData=laData
               llOk = rp.onMostraRequisitosArchi()
               nombre = request.cookies.get('nombre')
               nombre = nombre.replace('/', ' ')
               return render_template('Ind1120_2.html',nombre=nombre, paDatos=rp.paDatos, py=descri,cidproy=codpy, observ=observ) 
            elif request.form.get("button5", False) == 'Salir':
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Mnu1000.html',nombre=nombre) 
            if request.form.get("button0", False) == 'Salir':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsableArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_3.html', paDatos=rp.paDatos, nombre=nombre)     
            elif request.form.get("button0", False) =='Subir':
                '''cCodReq = request.form['button0'] == 'Subir' and request.form['codreq']
                nrodni= request.form['button0'] == 'Subir' and request.form['dnii']
                #request.form['button0'] == 'Subir' or request.form['codreq']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                cidproy=request.form['codpy']
                py=request.form['py']
                cCodReq = request.form['codreq']
                req= request.form['req']
                nrodni = request.form.get("dnii", False)
                resp = request.form.get("resp", False)
                estado = request.form.get("estado", False)
                cod = request.form.get("key", False)
                return render_template('Ind1130.html', cCodReq = cCodReq , cdescri=req, cnrodni=nrodni,cresp=resp, estado=estado, codigo=cod , cidproy=cidproy, nombre=nombre, paDatos=rp.paDatos,py=py)'''
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsableArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_1.html',nombre=nombre,  paDatos=rp.paDatos)  
            #return render_template('Ind1130.html', cCodReq = cCodReq ,paDatos=rp.paDatos, cnrodni=nrodni)

            if request.form.get("button0", False) =='subir_Requisitos':
                cCodReq = request.form['button0'] == 'subir_Requisitos' and request.form['codreq']
                #nrodni= request.form['button4'] == 'subir_Requisitos' and request.form['dnii']
                #request.form['button0'] == 'Subir' or request.form['codreq']:
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                #cidproy=request.form['codpy']
                #py=request.form['py']
                cCodReq = request.form['codreq']
                cidpy= request.form.get("codpy", False)
                py= request.form.get("py", False)
                req= request.form['req']
                nrodni = request.form.get("dnii", False)
                resp = request.form.get("resp", False)
                estado = request.form.get("estado", False)
                cod = request.form.get("key", False)
                fecha=time.strftime("%d/%m/%y")
                return render_template('Ind1130.html', cCodReq = cCodReq , cdescri=req,cresp=resp, estado=estado, codigo=cod , nombre=nombre, paDatos=rp.paDatos, cnrodni=nrodni,py=py,cidproy=cidpy,fecha=fecha)
            elif request.form.get("button1", False) =='Cargar':
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
                            'C:/tesis/visual/bd/local/git-proyecto/static/archivos', file.filename))
                        flash('Se subío con éxito el archivo')
                        x = request.form.to_dict()
                        laData = f_GetDict(x, 'paData')
                        #laData =('paData')
                        print('laData*************')
                        print(laData)
                        #rp.paData = laData
                        print("#######padataaaa")
                        print(laData)
                        codpy=request.form.get("paData[CIDPROY]")
                        dni = request.cookies.get('dni')
                        datos=list({codpy,dni})
                        #d=list(datos)
                        #d = d.split(']')
                        #d = d.replace('}', ' ')
                        print("tipo")
                        print(type(datos))
                        rp.paData=datos           
                        #rp.paproy = request.form.get("codpy") 
                        print('**********datoss')
                        print(datos)
                        print(rp.paData[0])
                        print(rp.paData[1])
                        datos_f=(rp.paData[1],rp.paData[0])
                        rp.paData=datos_f
                        print("datosss finales")
                        print(rp.paData)
                        descri= request.form.get('paData[CDESCRI]')
                        observ =request.form.get('observ')
                        #observ = observ.replace(',', '\n ')
                        print('**********')
                        print(observ)
                        #au.paData=laData
                        llOk = rp.onMostraRequisitosArchi()
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        return render_template('Ind1120_2.html',nombre=nombre, paDatos=rp.paDatos, py= descri, observ=observ) 
                else:
                    flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                    return redirect('Ind1130.html')  
            if request.form.get("button3", False) == 'Abrir_req':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                #laData =('paData')
                print('laData*************')
                print(laData)
                #rp.paData = laData
                print("#######padataaaa")
                print(laData)
                codpy=request.form.get("codpy")
                dni = request.cookies.get('dni')
                datos=list({codpy,dni})
                #d=list(datos)
                #d = d.split(']')
                #d = d.replace('}', ' ')
                print("tipo")
                print(type(datos))
                rp.paData=datos           
                #rp.paproy = request.form.get("codpy") 
                print('**********datoss')
                print(datos)
                print(rp.paData[0])
                print(rp.paData[1])
                datos_f=(rp.paData[1],rp.paData[0])
                rp.paData=datos_f
                print("datosss finales")
                print(rp.paData)
                descri= request.form.get('py')
                observ =request.form.get('observ')
                #observ = observ.replace(',', '\n ')
                print('**********')
                print(observ)
                #au.paData=laData
                llOk = rp.onMostraRequisitosArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120_2.html',nombre=nombre, paDatos=rp.paDatos, py= descri, observ=observ)  
            elif  request.form.get("button2", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                print('laData*************')
                print(laData)
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsableArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                return render_template('Ind1120.html', paDatos=rp.paDatos, nombre=nombre)
            '''if  request.form.get("button0", False) == 'abrir_req':
            print('ssssssssssssssssssssssssssssssssss editar')
            print(request.form)
            print("prueba")
            print(rp.paDatos)
            #llOk = rp.omMostrarEstados()
            llOk = rp.omDevolverDatos()
            codigo = request.form['button0'] == 'abrir_req' and '*' or 'None' or request.form['key']
            nrodni= request.form['button0'] == 'Nuevo' and request.form['dnii']
            if request.form['button0'] == 'Nuevo':
                    dni = request.cookies.get('dni')
                    nombre = request.cookies.get('nombre')
                    nombre = nombre.replace('/', ' ')
                    return render_template('Ind1140_1.html', cCodigo = codigo ,nombre=nombre, paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, paPersonas=rp.paPersonas)
            #respon = request.form['button0'] == 'Nuevo' and 'dni' or request.form['responsable']
            if request.form['button0'] == 'abrir_req' or request.form['key']:
                #a= rp.omDevolverProyecto()
                if request.form['key'] =='None':
                        codigo = '*'
                        dni = request.cookies.get('dni')
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        id_project = request.form['key']
                        codpy= request.args.get('codpy',False)
                        py=request.form['py']
                        codreq= request.form['codreq']
                        #nrodni = request.form.get("dnii", False)
                        cnrodni =  request.args.get('auditor',False)
                        estado = request.form.get("estado", False)
                        date = request.form.get("paData[TFECSUB]")
                        info= request.form.get("paData[MINFOAD]")
                        return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)
                else:
                        dni = request.cookies.get('dni')
                        nombre = request.cookies.get('nombre')
                        nombre = nombre.replace('/', ' ')
                        codigo= request.form['key']
                        id_project = request.form['key']
                        codpy= request.args.get('codpy',False)
                        py=request.form['py']
                        codreq= request.form['codreq']
                        #nrodni = request.form.get("dnii", False)
                        cnrodni =  request.args.get('auditor',False)
                        estado = request.form.get("estado", False)
                        date = request.form.get("paData[TFECSUB]")
                        info= request.form.get("paData[MINFOAD]")
                        return render_template('Ind1140_1.html', cCodigo = codigo , cIdProy=codpy,cCodReq=codreq,estado=estado, nombre=nombre,paDatos=rp.paDatos, paProyecto=rp.paProyecto, paRequisito=rp.paRequisito , paEstadoPuenteProyectos=rp.paEstadoPuenteProyectos, cnrodni =cnrodni,py=py)
            '''
            if  request.form.get("button5", False) == 'Cancelar':
                x = request.form.to_dict()
                laData = f_GetDict(x, 'paData')
                dni = request.cookies.get('dni')
                rp.paData = dni
                llOk = rp.omMostrarResponsableArchi()
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                if not llOk:
                    return render_template('Ind1120.html', pcError=rp.pcError)
                else:
                    return render_template('Ind1120.html', paDatos=rp.paDatos, nombre=nombre)
    else:
        dni = request.cookies.get('dni')
        nombre = request.cookies.get('nombre')
        nombre = nombre.replace('/', ' ')
        return render_template('Mnu1000.html',nombre=nombre)
#reportesss
@app.route('/reporte', methods=['GET', 'POST'])
def f_Reportes():
    rep = CReportes()
    if request.method == 'POST':
        if request.form.get("button0", False) == 'Reportes':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            print('laData*************')
            print(laData)
            dni = request.cookies.get('dni')
            rep.paData = dni
            llOk = rep.onMostraProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1610_2.html', pcError=rep.pcError)
            else:
                print('salida================')
                print(rep.paDatos)
                return render_template('Ind1610_2.html', paDatos=rep.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Cancelar':
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Mnu1000.html', nombre=nombre)

        if request.form.get("button0", False) == 'Abrir_detalles':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            #laData =('paData')
            dni = request.cookies.get('dni').strip()
            print('laData*************')
            print(laData)
            codpy=request.form.get("paData[CIDPROY]").strip()
            datos=list({dni,codpy})
            rep.paData=datos   
            datos_f=(rep.paData[0],rep.paData[1])
            rep.paData=datos_f
            descri= request.form.get("paData[CDESCRI]")
            llOk = rep.onMostraRequisitos()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1610.html', nombre=nombre, paDatos=rep.paDatos)
        
        elif request.form.get("button1", False) == 'Abrir_Requisitos':
            llOk = rep.onMostradetallereq()
            if request.form.get("button1", False) == 'Abrir_Requisitos':
                llOk = rep.omDevolverDatos()
                dni = request.cookies.get('dni')
                nombre = request.cookies.get('nombre')
                nombre = nombre.replace('/', ' ')
                serial = request.form['button1'] == 'Abrir_Requisitos' and request.form['key']
                nrodni= request.form['button1'] == 'Abrir_Requisitos' and  request.cookies.get('dni') or request.form['dnii']
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
                return render_template('Ind1610_1.html', archivo = archivo, extension = extension,  nserial=serial,codreq = cCodReq , ccodaud=codaud,fecha=fecha,dni=nrodni, descri=descri,resp=resp, estado=estado ,nombre=nombre,paDatos=rep.paDatos, paEstadoDetalleProyectos=rep.paEstadoDetalleProyectos)
            #return render_template('Ind1150_2.html', paDatos=au.paDatos, dni=dni)
        elif request.form.get("button0", False) == 'Cancelar':
            rep.paData = request.form.get("paData[CIDPROY]")
            llOk = rep.onMostraProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1610_2.html', paDatos=rep.paDatos, nombre=nombre)
        elif request.form.get("button0", False) == 'Reporte':
            llok = rep.onMostraProyectosPDF()
            try:
                return send_file(path + 'proyectos.pdf', attachment_filename='proyectos.pdf')
            except Exception as e:
                return str(e)
        if request.form.get("button1", False) == 'Reporte':
            llok = rep.onMostraRequisitosPDF()
            try:
                return send_file(path + 'requisitos.pdf', attachment_filename='requisitos.pdf')
            except Exception as e:
                return str(e)    
        elif request.form.get("button2", False) == 'Reporte':
            llok = rep.onMostradetallereqPDF()
            try:
                return send_file(path + 'avance.pdf', attachment_filename='avance.pdf')
            except Exception as e:
                return str(e)

        if request.form.get("button0", False) == 'Reporte Porcentaje':
            llok = rep.onMostraEstadosTotalPDF()
            try:
                return send_file(path + 'estados.pdf', attachment_filename='estados.pdf')
            except Exception as e:
                return str(e)

        elif request.form.get("button2", False) == 'Cancelar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            rep.paData = laData
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            llOk = rep.onMostraProyectos()
            return render_template('Ind1610_2.html',  nombre=nombre, paDatos=rep.paDatos)
    
        if request.form.get("button1", False) == 'Cancelar':
            rep.paData = request.form.get("paData[CIDPROY]")
            llOk = rep.onMostraProyectos()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1610_2.html', paDatos=rep.paDatos, nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)

