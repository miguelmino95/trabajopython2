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
    numfactura=request.form.get('num_factura', type=int)
    modelo=request.form.get('modelo_serie', type=str)
    marca_hardware=request.form.get('marca_hardware', type=str)
    codigo=request.form.get('codigo', type=str)
    descripcion=request.form.get('descripcion', type=str)
    responsable=request.form.get('responsable', type=str)
    area=request.form.get('area', type=str)

    Accionlabcon.Accionlabcon().insertarActivo(nombre, fcompra, estado, numfactura, modelo, marca_hardware, codigo, descripcion, responsable, area)
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

