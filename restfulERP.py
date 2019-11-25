#!/usr/bin/env python
# encoding=utf8  
import json
import sys
sys.path.append('/var/www/html/UCSMASBANC/Jobs')
#sys.path.append('/Applications/XAMPP/xamppfiles/htdocs/UCSMERP/UCSMASBANC/Jobs')
from flask import Flask, request, jsonify
from datetime import datetime
#from CPagosASBANC import *
from Clases.CProveedor import *
from Clases.CMtoPersonal import *
from Clases.CSignature import *
from Clases.CTramites import *
from Clases.CPagosOCRRII import *
#from flask_cors import CORS

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)
#CORS(app)
# ------------------------------------------------
# WS Controlador de errores
# 2019-01-16 JLF Creacion
# ------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    print e
    return '{"ERROR":"SOLICITUD INVALIDA"}'

# ------------------------------------------------
# WS inicio de sesion de Proveedor
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsLoginProveedor', methods=['POST'])
def f_LoginProveeodor():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omLoginProveedor()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS REGISTRO DE PROVEEDOR
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsRegistroProveedor', methods=['POST'])
def f_RegistroProveedor():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omRegistrarProveedor()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS CONSULTA DE TIPO DE RUBROS
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaTipRubro', methods=['POST'])
def f_ConsultaTipoRubro():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultarTipoRubros()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS CONSULTA RUBROS POR TIPO
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaRubros', methods=['POST'])
def f_ConsultaRubros():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultarRubros()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS CONSULTA RUBROS POR PROVEEDOR
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaRubrosxProvedoor', methods=['POST'])
def f_ConsultaRubrosxProveedor():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultaRubrosXProveedor()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS GRABA O EDITA LOS  RUBROS DE UN  PROVEEDOR
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsRegistroRubroProveedor', methods=['POST'])
def f_RegistroRubrosProveedor():
    data = request.get_data()
    lo = CProveedor()
    lo.pcParam = data
    llOk = lo.omRegistroRubrosProveedor()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# gestiona los WS de proveedores
# 2018-06-18 FRL CREACION
# ------------------------------------------------
@app.route('/wsRegistroProveedorParcial', methods=['POST'])
def f_RegistroProveedorParcial():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omRegistrarProveedorParcial()
    if not llOk:
       return lo.pcError
    return lo.pcData


# ------------------------------------------------
# WS CONSULTAR PROVEEDOR
# 2018-06-18 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaProveedor', methods=['POST'])
def f_ConsultaProveedor():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultaProveedor()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS CONSULTA TIPO DE CUENTA BANCARIA
# 2018-07-02 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaTipoCuentaBancaria', methods=['POST'])
def f_ConsultaTipoCuentaBancaria():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultaTipoCuentaBancaria()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS CONSULTA DE COTIZACIONES
# 2018-07-05 FER  FRL Creacion
# ------------------------------------------------
@app.route('/wsConsultaCotizacion', methods=['POST'])
def f_ConsultaCotizacion():
    lo = CProveedor()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultaCotizaciones()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS para calcular mora de deuda
# 2019-01-04 FPM Creacion
# ------------------------------------------------
@app.route('/wsCalcularMoraDeuda', methods=['POST'])
def f_CalcularMoraDeuda():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosASBANC()
    lo.paParam = laParam
    llOk = lo.omCalcularMoraDeuda()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

# ------------------------------------------------
# WS para calcular mora de deuda EN BLOQUE
# 2019-02-28 JLF Creacion
# ------------------------------------------------
@app.route('/wsCalcularMoraDeudaTodos', methods=['POST'])
def f_CalcularMoraDeudaTodos():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosASBANC()
    lo.paParam = laParam
    llOk = lo.omCalcularMoraDeudaTodos()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

# ------------------------------------------------
# WS consulta DNI para Usuario Mesa de Partes
# 2018-01-16 FPM Creacion
# ------------------------------------------------
@app.route('/wsConsultarDNIMesaPartes', methods=['POST'])
def f_ConsultarDNIMesaPartes():
    lo = CMtoPersonal()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultarDNIMesaPartes()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS activa Usuario Mesa de Partes
# 2018-01-16 FPM Creacion
# ------------------------------------------------
@app.route('/wsActivarDNIMesaPartes', methods=['POST'])
def f_ActivarDNIMesaPartes():
    lo = CMtoPersonal()
    lo.pcParam = request.get_data()
    llOk = lo.omActivarDNIMesaPartes()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS desactiva Usuario Mesa de Partes
# 2018-01-16 FPM Creacion
# ------------------------------------------------
@app.route('/wsDesactivarDNIMesaPartes', methods=['POST'])
def f_DesactivarDNIMesaPartes():
    lo = CMtoPersonal()
    lo.pcParam = request.get_data()
    llOk = lo.omDesactivarDNIMesaPartes()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS consulta Maestro de Personas por Nombre
# 2018-01-16 FPM Creacion
# ------------------------------------------------
@app.route('/wsConsultarPersonalNombre', methods=['POST'])
def f_ConsultarPersonalNombre():
    lo = CMtoPersonal()
    lo.pcParam = request.get_data()
    llOk = lo.omConsultarPersonalNombre()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# WS agrupa DNIs para reducir duplicados
# 2018-01-16 FPM Creacion
# ------------------------------------------------
@app.route('/wsAgruparDNIs', methods=['POST'])
def f_AgruparDNIs():
    lo = CMtoPersonal()
    lo.pcParam = request.get_data()
    llOk = lo.omAgruparDNIs()
    if not llOk:
       return lo.pcError
    return lo.pcData

#FIRMAR DOCUMENTO DIGITALMENTE
@app.route('/wsFirmarDocumento', methods=['POST'])
def f_firmarDocumento():
    try:
        laParam = json.loads(request.get_data())
    except:
        return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CSignature()
    lo.pcParam = request.get_data()
    llOk = lo.omFirmarDocumento()
    if not llOk:
        lcError = '{"ERROR": "%s"}'%(lo.pcError)
        return lcError
    return lo.pcData

#VERIFICAR DOCUMENTO FIRMADO DIGITALMENTE
@app.route('/wsVerificarDocumento', methods=['POST'])
def f_verificarDocumento():
    try:
        laParam = json.loads(request.get_data())
    except:
        return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CSignature()
    lo.pcParam = request.get_data()
    llOk = lo.omVerificarDocumento()
    if not llOk:
        lcError = '{"ERROR": "%s"}'%(lo.pcError)
        return lcError
    return lo.pcData

# ------------------------------------------------
# Revisar Fotos del Alumno en Sistema Academico
# 2019-02-28 JLF Creacion
# ------------------------------------------------
@app.route('/wsRevisarFotoAlumno', methods=['POST'])
def f_RevisarFotoAlumno():
    lo = CTramites()
    lo.pcParam = request.get_data()
    llOk = lo.omRevisarFotoAlumno()
    if not llOk:
       return lo.pcError
    return lo.pcData

# ------------------------------------------------
# Revisar Cursos de un Alumno para tramitar Jurado
# 2019-06-21 JLF Creacion
# ------------------------------------------------
@app.route('/wsRevisarCursosJurado', methods=['POST'])
def f_RevisarCursosJurado():
    lo = CTramites()
    lo.pcParam = request.get_data()
    llOk = lo.omRevisarCursosJurado()
    if not llOk:
       return lo.pcError
    return lo.pcData

# -----------------------------------------------------------
# WS para init de validacion de pagos OCRRII en contabilidad
# 2019-04-23 FPM Creacion
# -----------------------------------------------------------
@app.route('/wsInitValPagosOCRRII', methods=['POST'])
def f_InitPagosOcrrii():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omInitPagosOcrrii()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData

# -----------------------------------------------------------------------
# WS Bandeja de entrada para validacion de pagos OCRRII en contabilidad
# 2019-04-23 FPM Creacion
# -----------------------------------------------------------------------
@app.route('/wsBandejaContabPagosOCRRII', methods=['POST'])
def f_BandejaContabilidadPagosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omBandejaContabPagosOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData

# -----------------------------------------------------------------------
# WS Bandeja de entrada para validacion de pagos OCRRII en contabilidad
# 2019-04-23 FPM Creacion
# -----------------------------------------------------------------------
@app.route('/wsCargarRevisionContabPagosOCRRII', methods=['POST'])
def f_CargarRevisionContabPagosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omCargarRevisionContabPagosOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

# -----------------------------------------------------------------------
# WS Grabacion de la revisi[on de comprobantes contabilidad
# 2019-04-25 MMH Creacion
# -----------------------------------------------------------------------
@app.route('/wsGrabarRevisionOCRRII', methods=['POST'])
def f_GrabarRevisionOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam['paData']
    lo.paDatos = laParam['paDatos']
    llOk = lo.omGrabarRevisionOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

@app.route('/wsReporteAsientosOCRRII', methods=['POST'])
def f_ReporteAsientosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omReporteAsientosOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

# -----------------------------------------------------------------------
# WS Inicio Reportes de Comprobantes pagos OCRRII en contabilidad
# 2019-04-23 FPM Creacion
# -----------------------------------------------------------------------
@app.route('/wsInitReporteContabPagosOCRRII', methods=['POST'])
def f_InitReporteContabPagosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omInitReporteContabPagosOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData

# -----------------------------------------------------------------------
# WS Reportes de Comprobantes pagos OCRRII en contabilidad
# 2019-04-23 FPM Creacion
# -----------------------------------------------------------------------    
@app.route('/wsReportComprobantesOcrrii', methods=['POST'])
def f_ReporteContabPagosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omReportComprobantesOcrrii()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData
# -----------------------------------------------------------------------
# WS Inicio de Comprobantes OCRII
# 2019-04-30 FPM Creacion
# -----------------------------------------------------------------------    
@app.route('/wsInitComprobantesOCRRII', methods=['POST'])
def f_InitComprobantesOcrrii():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omInitComprobantesOcrrii()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData
# -----------------------------------------------------------------------
# WS Comprobantes OCRII
# 2019-04-30 FPM Creacion
# -----------------------------------------------------------------------    
@app.route('/wsCargarComprobantesOCRRII', methods=['POST'])
def f_CargarComprobantesOcrrii():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omCargarComprobantesOcrrii()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData
# -----------------------------------------------------------------------
# WS Grabar Comprobantes OCRII
# 2019-04-30 FPM Creacion
# -----------------------------------------------------------------------    
@app.route('/wsGrabarComprobantesOCRRII', methods=['POST'])
def f_GrabarComprobantesOcrrii():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam['paData']
    lo.paDatos = laParam['paDatos']
    llOk = lo.omGrabarComprobantesOcrrii()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData
# -----------------------------------------------------------------------
# WS Contabilizar OCRII
# 2019-04-30 FPM Creacion
# -----------------------------------------------------------------------    
@app.route('/wsContabilizarPagosOCRRII', methods=['POST'])
def f_ContabilizarPagosOCRRII():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omContabilizarPagosOCRRII()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData

# -----------------------------------------------------------------------
# WS Contabilizar OCRII
# 2019-05-14 FLC Creacion
# -----------------------------------------------------------------------    
@app.route('/wsConsultarCxP', methods=['POST'])
def f_ConsultarCxP():
    try:
       laParam = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laParam
    llOk = lo.omConsultarCxP()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paDatos)
    return lcData

# -----------------------------------------------------------------------
# WS Consulta pagos OCRRII
# 2019-05-07 FPM Creacion
# -----------------------------------------------------------------------
@app.route('/wsSeguimientoComprobantesOCRRII', methods=['POST'])
def f_SeguimientoComprobantes():
    try:
       laData = json.loads(request.get_data())
    except:
       return '{"ERROR": "PARAMETRO DE ENTRADA NO ES JSON"}'
    lo = CPagosOCRRII()
    lo.paData = laData
    llOk = lo.omSeguimientoComprobantes()
    if not llOk:
       lcError = '{"ERROR": "%s"}'%(lo.pcError)
       return lcError
    lcData = json.dumps(lo.paData)
    return lcData

if __name__ == '__main__':
   #app.run(host='localhost', debug=True, port=8080)
   app.run(host='0.0.0.0', debug=True, port=8082, threaded=True)
   #app.run(host='192.168.0.3', debug=True, port=8080)