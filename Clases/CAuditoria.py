from flask import render_template, redirect, url_for, request

class CAuditoria:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def onRevisarAuditoria(self):
      return render_template('revisarauditoria.html')
   
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

   

