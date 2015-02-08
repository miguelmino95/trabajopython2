'''
Created on 1/2/2015

@author: Miguelm
'''

from ec.edu.itsae.conec import DBconec
import json

class Accionlabcon(DBconec.DBcon):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def validarUsuario(self, usuario, clave):
        con=self.conexion().connect().cursor()
        con.execute("""select * from usuarios where nombre_usuario='%s' and clave='%s'""" % (usuario, clave))
        reporte=con.fetchall()
        return reporte
    
    
    def reportarActivo(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from activos")
        reporte=con.fetchall()
        return reporte
    
    def insertarActivo(self, nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo, descripcion, persona, area):
        con=self.conexion().connect()
        sql=""" insert into activos (nombre, fech_compra, estado, num_factura, modelo_serie, marca_hardware, codigo, descripcion, persona_idpersona, area_depart_idarea_depart) 
        values('%s', '%s', '&s' , %i, '%s', '%s', %i , '%s') """ % (nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo, descripcion, persona, area)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
      
    def selectPersonaArea(self):
        con=self.conexion().connect().cursor()
        con.execute("select persona.nombre, area_depart.nombre_area from persona, area_depart ")
        reporte=con.fetchall()
        return reporte      
            
            
    def EliminarActivo(self, nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo, descripcion):
        con=self.conexion().connect()
        sql=""" delete from activos where (nombre, fech_compra, estado, num_factura, modelo_serie, marca_hardware, codigo, descripcion) 
        values('%s', '%s', '&s' , %i, '%s', '%s', %i , '%s') """ % (nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo, descripcion)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
    def buscarActivoDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from activos where upper(CONCAT(nombre,' ', num_factura,' ', modelo_serie)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        return reporte
    
    def buscarActivoAuto(self, datobuscado):
        con=self.conexion().connect().cursor()
        con.execute(""" select CONCAT(nombre, ' ', num_factura, ' ', modelo_serie) as value, idpersona as id from persona where upper (CONCAT(nombre, ' ', num_factura, ' ', modelo)) like upper('%s')""" % ("%"+datobuscado+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna, row)))
        return json.dumps(lista, indent=2)
    
    def reportarPersona(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from persona")
        reporte=con.fetchall()
        return reporte
    
    def insertarPersona(self, nombre, apaterno, amaterno, cedula, telefono, email, fnacimiento, edad, estado):
        con=self.conexion().connect()
        sql=""" insert into persona(nombre, apell_paterno, apell_materno, cedula, telefono, email, fech_nacimiento, edad, estado) 
        values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i) """ % (nombre, apaterno, amaterno, cedula, telefono, email, fnacimiento, edad, estado)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
    def buscarPersonaDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from persona where upper(CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        return reporte
    
    def buscarPersonaAuto(self, datobuscado):
        con=self.conexion().connect().cursor()
        con.execute(""" select CONCAT(nombre, ' ', apell_paterno, ' ', apell_materno) as value, idpersona as id from persona where upper (CONCAT(nombre, ' ', apell_paterno, ' ', apell_materno)) like upper('%s')""" % ("%"+datobuscado+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna, row)))
        return json.dumps(lista, indent=2)
    
    
            
    