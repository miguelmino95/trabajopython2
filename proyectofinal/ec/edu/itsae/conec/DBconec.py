from flaskext.mysql import MySQL
from flask import Flask

class DBcon():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def conexion(self):
        mysql = MySQL()
        control = Flask(__name__)
        control.config['MYSQL_DATABASE_USER'] = 'adminlab'
        control.config['MYSQL_DATABASE_PASSWORD'] = 'labo2015'
        control.config['MYSQL_DATABASE_DB'] = 'centro_de_computo'
        control.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(control)
        return mysql