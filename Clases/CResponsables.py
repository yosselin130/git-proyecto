from flask import render_template, redirect, url_for, request

class CResponsables:
   def __init__(self):
      self.paData = []
      self.paDatos = []
      self.loSql = CSql()
      self.pcError = ''

   def onAsignacionRes(self):
      return render_template('Ind1140.html')
   def onMantRes(self):
      return render_template('mantresponsables.html')

   def omInit(self):
      error= None
      return render_template('proyecto.html', error=error)
   
   def omResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False
        llOk = self.__mxCrearResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk
   
   def omMostrarResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxMostrarResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk

   def omEditarResponsable(self):
        llOk = self.loSql.omConnect()
        if not llOk:
            self.pcError = self.loSql.pcError
            return False

        llOk = self.__mxEditarResp()
        if llOk:
            self.loSql.omCommit()
        self.loSql.omDisconnect()
        return llOk