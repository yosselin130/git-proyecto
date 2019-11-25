from flask import render_template, redirect, url_for, request

class CRevisarProyecto:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def onRevisarProyecto(self):
      return render_template('revisarproyecto.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)