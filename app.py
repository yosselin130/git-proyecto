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
from os import path, walk
from datetime import timedelta
from flask import send_from_directory, app, make_response, request, render_template, redirect, url_for, request, flash, session, abort
UPLOAD_FOLDER = 'C:/tesis/visual/SGRSIA/archivos'


app = Flask(__name__, static_url_path='')
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
            resp = make_response(render_template(
                'index.html', pcError=lo.pcError))
            #print('cookie get error' + request.cookies.get('test'))
            return resp
        else:
            #session['']
            session["log"] = True
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=40)
            nombre = lo.paDatos['CNOMBRE'].replace('/', ' ')
            dni = lo.paDatos['CNRODNI']
            ''''session['dni'] = request.form["CNRODNI"]'''
            resp = make_response(render_template(
                'Mnu1000.html', nombre=nombre))
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


@app.route('/proyecto', methods=['GET', 'POST'])
def f_Proyecto():
    py = CProyecto()
    if request.method == 'POST':      
        if request.form['button0'] == 'Proyectos':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData = laData
            llOk = py.omMostrarProyectos()
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            if not llOk:
                return render_template('Ind1110.html', pcError=py.pcError)
            else:
                return render_template('Ind1110_1.html', paDatos=py.paDatos, nombre=nombre)
        elif request.form['button0'] == 'Nuevo':
           llOk = py.omMostrarEstados()
           dni = request.cookies.get('dni')
           nombre = request.cookies.get('nombre')
           nombre = nombre.replace('/', ' ')
           return render_template('Ind1110.html', paDatos=py.paDatos, dni=dni)
        if request.form['button0'] == 'Grabar':
            x = request.form.to_dict()
            laData = f_GetDict(x, 'paData')
            py.paData = laData
            llOk = py.omProyecto()
            if not llOk:
                return render_template('Ind1110.html', pcError=py.pcError)
            else:
                dni = request.cookies.get('dni')
                return render_template('Ind1110.html')

        elif request.form['button0'] == 'Cancelar':
            llOk = py.omMostrarProyectos()
            return render_template('Ind1110_1.html', paDatos=py.paDatos)

        elif request.form['button0'] == 'Salir':
            return render_template('Mnu1000.html')
        
        if request.form['button0'] == 'Editar':
            llOk = py.omMostrarEstados()
            dni = request.cookies.get('dni')
            nombre = request.cookies.get('nombre')
            nombre = nombre.replace('/', ' ')
            return render_template('Ind1110.html', paDatos=py.paDatos, dni=dni)
                    
                
                
                
            '''return render_template('Ind1110.html', paDatos=py.paDatos)
            return render_template('Ind1110_1.html')'''


@app.route('/crearproyecto', methods=['GET', 'POST'])
def f_Crearproyecto():
    py = CProyecto()
    '''if request.method == 'GET':
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
            return render_template('Ind1110.html', success=py.paDatos, dni=dni)

    ''' if request.method == 'POST':
      if request.form.get('Grabar') == 'Grabar':
         print("Grabar")
      elif request.form.get('Cancelar') == 'Cancelar':
         return  render_template('Ind1110.html')

   else:
      return render_template('Ind1110.html')'''

@app.route('/requisito', methods=['GET', 'POST'])
def f_Requisito():
    if request.method == 'GET':
        x = request.form.to_dict()
        laData = f_GetDict(x, 'paData')
        re = CRequisitos()
        re.paData = laData
        llOk = re.omMostrarRequisitos()
        print(re.paDatos)
        #nombre = request.cookies.get('nombre')
        #nombre = nombre.replace('/', ' ')
        if not llOk:
            return render_template('Ind1170.html', pcError=re.pcError)
        else:
            return render_template('Ind1130_1.html', paDatos=re.paDatos)
    else:
        '''if request.method =='POST':'''
        return render_template('Ind1130_1.html')

@app.route('/crearrequisito', methods=['GET', 'POST'])
def f_Crearrequisito():
    re = CRequisitos()
    if request.method == 'GET':
        llOk = re.omMostrarEstados()
        if not llOk :
            return render_template('Ind1170.html', pcError=re.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1170.html', paDatos=re.paDatos, dni=dni)
        llOk = re.omMostrarTipos()
        if not llOk :
            return render_template('Ind1170.html', pcError=re.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1170.html', paDatos=re.paDatos, dni=dni)
    else:
        x = request.form.to_dict()
        laData = f_GetDict(x, 'paData')
        re.paData = laData
        llOk = re.omRequisito()
        if not llOk:
            return render_template('Ind1170.html', pcError=re.pcError)
        else:
            dni = request.cookies.get('dni')
            return render_template('Ind1170.html', success=re.paDatos, dni=dni)
    ''' if request.method == 'POST':
      if request.form.get('Grabar') == 'Grabar':
         print("Grabar")
      elif request.form.get('Cancelar') == 'Cancelar':
         return  render_template('Ind1110.html')
   else:
      return render_template('Ind1110.html')'''

if __name__ == '__main__':
    app.run(debug=True)
