from flask import render_template, redirect, url_for, request

class CRevisarReq:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def onRevisarReq(self):
      return render_template('revisarrequisitos.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)