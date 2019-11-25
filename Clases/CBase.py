# encoding=utf8  
import datetime
import random
import collections
import json
from datetime import timedelta
from werkzeug.datastructures import ImmutableMultiDict

class CBase:
   def __init__(self):
       self.pcError = None
       self.loSql   = None

class CDate(CBase):
   def __init__(self):
       self.pcClave = None
       self.dFecha = None
   
   def valDate(self, p_cFecha):
       llOk = True
       try:
          self.dFecha = datetime.datetime.strptime(p_cFecha, "%Y-%m-%d").date()
       except:
          llOk = False
       return llOk
  
   def add(self, p_cFecha, p_nDias):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       self.dFecha = self.dFecha + timedelta(days = p_nDias)
       self.dFecha = self.dFecha.strftime('%Y-%m-%d')
       return llOk
      
   def diff(self, p_cFecha1, p_cFecha2):
       llOk = self.valDate(p_cFecha1)
       if not llOk:
          return None
       llOk = self.valDate(p_cFecha2)
       if not llOk:
          return None
       ldFecha1 = self.mxValDate(p_cFecha1)
       ldFecha2 = self.mxValDate(p_cFecha2)
       d = ldFecha1 - ldFecha2
       return d.days

   def dow(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return ldFecha.weekday()

   def day(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return int(ldFecha.strftime('%d'))

   def month(self, p_cFecha):
       llOk = self.valDate(p_cFecha)
       if not llOk:
          return None
       ldFecha = self.mxValDate(p_cFecha)
       return int(ldFecha.strftime('%m'))


def fxFileRep():
    lcFile = str(random.random())
    lcFile = lcFile[-8:]
    lcFile = lcFile.replace('.', '')
    return 'R' + lcFile

def fxString(p_cLinea, p_nLenght):
    lcLinea = p_cLinea + ' ' * p_nLenght
    i = lcLinea.count('Ñ')
    i += lcLinea.count('Á')
    i += lcLinea.count('É')
    i += lcLinea.count('Í')
    i += lcLinea.count('Ó')
    i += lcLinea.count('Ú')
    lcLinea = lcLinea[:p_nLenght + i]
    return lcLinea

def fxNumber(p_nNumero, p_nLenght, p_nDec = 2):
    p_nNumero = float(p_nNumero) + 0.001
    #lcLinea = "{:12,.2f}".format(p_nNumero)
    lcFormat = "{:12,.%sf}"%(p_nDec) 
    lcLinea = lcFormat.format(p_nNumero)
    if p_nDec == 3:
       print (lcFormat, lcLinea)
    lcLinea = ' ' * p_nLenght + lcLinea 
    lcLinea = lcLinea[-p_nLenght:]
    return lcLinea

def fxInteger(p_nNumero, p_nLenght):
    p_nNumero = int(p_nNumero)
    lcLinea = str(p_nNumero)
    lcLinea = ' ' * p_nLenght + lcLinea 
    lcLinea = lcLinea[-p_nLenght:]
    return lcLinea

def f_GetDict(paData, p_key):
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