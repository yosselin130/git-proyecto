from flask import render_template, redirect, url_for, request

class CResponsables:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def onAsignacionRes(self):
      return render_template('Ind1140.html')
   def onMantRes(self):
      return render_template('mantresponsables.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)