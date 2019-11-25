from flask import render_template, redirect, url_for, request

class CHome:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None


   def onHome(self):
      return render_template('index.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)
