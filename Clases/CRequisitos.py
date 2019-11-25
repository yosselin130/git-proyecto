import os
from flask import render_template, redirect, url_for, request , flash
from werkzeug.utils import secure_filename
import urllib.request
""" from contants import SUCCESS_FILE_MESSAGE """

class CRequisitos:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.cNombre = None

   def onCrearReq(self):
      return render_template('Ind1160.html')
   def onDescargarReq(self):
      return render_template('requisitos.html')
   def onSubirReq(self):
      if request.method == 'POST':
         if 'file' not in request.files:
               flash('No file part')
               return redirect(request.url)
         file = request.files['file']
         if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
         if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('C:/tesis/visual/SGRSIA/archivos', filename))
            flash('Se subío con éxito el archivo')
            return redirect('/subirreq')
         else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
      return render_template('subirarchivo.html')


   def onProgReq(self):
      return render_template('progresoreq.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)