'''
Created on 1/2/2015

@author: Miguelm

'''

from control import control
from ec.edu.itsae.labcon import Accionlabcon
from flask import render_template, request, redirect, url_for



@control.route("/inicio")
def inicio(): 
    return render_template("inicio.html")

@control.route("/activos")
def reportarActivo():
    objr=Accionlabcon.Accionlabcon().reportarActivo()    
    return render_template("formRegistroActivos.html", data=objr)

@control.route("/addActivos", methods=['POST'])
def addActivos():
    nombre=request.form.get('nombre', type=str)
    fcompra=request.form.get('fech_compra', type=str)
    estado=request.form.get('estado', type=str)
    nfactura=request.form.get('num_factura', type=int)
    modelo_serie=request.form.get('modelo_serie', type=str)
    marca_hardware=request.form.get('marca_hardware', type=str)
    codigo=request.form.get('codigo', type=str)
    descripcion=request.form.get('descripcion', type=str)
    responsable=request.form.get('responsable', type=str)
    area=request.form.get('area', type=str)

    Accionlabcon.Accionlabcon().insertarActivo(nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo,descripcion, responsable, area)
    return redirect(url_for('reportarActivo'))

@control.route("/delActivos")
def delActivos():
    
    nombre=request.form.get('nombre', type=str)
    fcompra=request.form.get('fech_compra', type=str)
    estado=request.form.get('estado', type=int)
    nfactura=request.form.get('num_factura', type=str)
    modelo_serie=request.form.get('modelo_serie', type=str)
    marca_hardware=request.form.get('marca_hardware', type=str)
    codigo=request.form.get('codigo', type=str)
    descripcion=request.form.get('descripcion', type=str)
    responsable=request.form.get('responsable', type=str)
    area=request.form.get('area', type=str)


    Accionlabcon.Accionlabcon().EliminarActivo(nombre, fcompra, estado, nfactura, modelo_serie, marca_hardware, codigo,descripcion, responsable, area)
    return redirect(url_for('reportarActivo'))

@control.route("/buscarActivo")
def buscarActivoDato():
    nombre=str(request.args.get('Anombre'))
    objr=Accionlabcon.Accionlabcon().buscarActivoDato(nombre) 
    return render_template("formRegistroActivos.html", data=objr)

@control.route("/buscaractauto")
def buscarActivoAuto():
    nombre=str(request.args.get('term'))
    objr=Accionlabcon.Accionlabcon().buscarActivoAuto(nombre) 
    print objr
    return objr

'''@control.route("/personas")
def reportarPersona():
    objr=Accionlabcon.Accionlabcon().reportarPersona()  
    return render_template("formRegistroPersonas.html", data=objr)

@control.route("/addPersona", methods=['POST'])
def addPersona():
    nombre=request.form.get('nombre', type=str)
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    telefono=request.form.get('telefono', type=str)
    email=request.form.get('email', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)    
    edad=request.form.get('edad', type=str)    
    estado=request.form.get('estado', type=int)


    Accionlabcon.Accionlabcon().insertarPersona(nombre, apaterno, amaterno, cedula, telefono, email, fnacimiento, edad, estado)
    return redirect(url_for('reportarPersona'))

@control.route("/buscarPersona")
def buscarPersonaDato():
    nombre=str(request.args.get('Pnombre'))
    objr=Accionlabcon.Accionlabcon().buscarPersonaDato(nombre) 
    return render_template("formRegistroPersonas.html", data=objr)

@control.route("/buscarperauto")
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objr=Accionlabcon.Accionlabcon().buscarPersonaAuto(nombre) 
    print objr
    return objr'''

