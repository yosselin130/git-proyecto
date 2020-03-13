import hashlib
import psycopg2
#import pymssql
import json

class CSql():
    def __init__(self):
        self.h       = None
        self.plOk    = True
        self.pcError = None

    def omConnect(self, p_nDB = None):
        self.plOk = True
        lcConnect = "host=localhost dbname=UCSMERP2 user=postgres password=root port=5433" #mibd
        #lcConnect = "host=localhost dbname=UCSMERP user=postgres password=root port=5432" #mibdcasa
        #lcConnect = "host=localhost dbname=UCSMERP user=postgres password=postgres port=5432"  #bdcato
        if p_nDB == 1:
           lcConnect = "host=localhost dbname=UCSMListener user=postgres password=postgres port=5432"
        elif p_nDB == 2:
           lcConnect = "host=localhost dbname=UCSMINS user=postgres password=postgres port=5432"
        try:
           print('connection string ' + lcConnect)
           self.h = psycopg2.connect(lcConnect) 
        except psycopg2.Error as e:
           print("Unable to connect!")
           print(e)
           print(e.diag.message_detail)
           self.plOk = False
           self.pcError = 'ERROR AL CONECTAR CON LA BASE DE DATOS'
        return self.plOk

    def omExecRS(self, p_cSql):
        #print p_cSql
        self.plOk = True
        lcCursor = self.h.cursor()
        try:
           lcCursor.execute(p_cSql)
           RS = lcCursor.fetchall()
        except psycopg2.DatabaseError as e:
           self.plOk = False
           print (e.message)
           self.pcError = 'ERROR AL EJECUTAR COMANDO SELECT'
           self.pcError = 'Credenciales Invalidas, volver a ingresar por favor.'
           RS = None
        return RS

    def omExec(self, p_cSql):
        #print p_cSql
        self.plOk = True
        lcCursor = self.h.cursor()
        try:
           lcCursor.execute(p_cSql)
        except psycopg2.Error as e:
           self.plOk = False
           print (e.message)
           self.pcError = 'ERROR AL ACTUALIZAR LA BASE DE DATOS 1'
        except psycopg2.DatabaseError as e:
           self.plOk = False
           print (e.message)
           self.pcError = 'ERROR AL ACTUALIZAR LA BASE DE DATOS 2'
        except psycopg2.OperationalError as e:
           self.plOk = False
           print (e.message)
           self.pcError = 'ERROR AL ACTUALIZAR LA BASE DE DATOS 3'
        return self.plOk

    def omDisconnect(self):
        self.h.close()

    def omCommit(self):
        self.h.commit()

class CSqlServer():
   def __init__(self):
       self.h       = None
       self.plOk    = True
       self.pcError = None

   def omConnect(self, p_nFlag = 0):
       self.plOk = True
       try:
          # DB Matriculas
          self.h = pymssql.connect("10.0.2.61:1433\SVRDB01", "userAppUCSM", "4pp$UcSm", "UCSM")
       except:
          self.plOk = False
          self.pcError = 'ERROR AL CONECTAR CON SQL-SERVER'
       return self.plOk

   def omExecRS(self, p_cSql):
       #print p_cSql
       self.plOk = True
       lcCursor = self.h.cursor()
       try:
          lcCursor.execute(p_cSql)
          RS = lcCursor.fetchall()
       except pymssql.DatabaseError as e:
          print (e.message)
          self.plOk = False
          self.pcError = 'ERROR AL EJECUTAR COMANDO SQL'
          RS = None
       return RS

   def omExec(self, p_cSql):
       self.plOk = True
       lcCursor = self.h.cursor()
       try:
          lcCursor.execute(p_cSql)
       except pymssql.DatabaseError as e:
          self.plOk = False
          self.pcError = 'ERROR AL ACTUALIZAR BASE DE DATOS'
          print (e.message)
       return self.plOk

   def omDisconnect(self):
       self.h.close()

   def omCommit(self):
       self.h.commit()