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
    
    
    def insertarActivo(self,nombre, fcompra, estado, numfactura, modelo, marca_hardware, codigo, descripcion, responsable, area):
        con=self.conexion().connect()
        sql=""" insert into activos(nombre, fech_compra, estado, num_factura, 
                        modelo_serie, marca_hardware, codigo, descripcion, responsable, area)
                         values('%s','%s','%s', %i ,'%s','%s','%s','%s','%s','%s')  """ % (nombre, fcompra, estado, numfactura, modelo, marca_hardware, codigo, descripcion, responsable, area)
        return sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)     
            
    def buscarActivoDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from activos where upper(CONCAT(nombre,' ', num_factura,' ', modelo_serie,' ', responsable,' ', area)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        return reporte
    
    def buscarActivoAuto(self, datobuscado):
        con=self.conexion().connect().cursor()
        con.execute(""" select CONCAT(nombre,' ', num_factura,' ', modelo_serie,' ', responsable,' ', area) as value, idpersona as id from persona where upper (CONCAT(nombre,' ', num_factura,' ', modelo_serie,' ', responsable,' ', area)) like upper('%s')""" % ("%"+datobuscado+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna, row)))
        return json.dumps(lista, indent=2)
    
    
    
            
    