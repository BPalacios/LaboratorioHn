# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, exceptions, models, fields, _

class Paciente(models.Model):
    _name = "paciente.paciente"
    _description = 'Modelo para agregar pacientes'
    
    pnombrePaciente = fields.Char(string='Primer Nombre', required=True)
    name = fields.Char(string='Segundo Nombre')
    papellidoPaciente = fields.Char(string='Primer Apellido', required=True)
    sapellidoPaciente = fields.Char(string='Segundo Apellido')
    fechaNaciemiento = fields.Date(string="Fecha de Nacimiento")
    genero = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], string='Genero')
    edad = fields.Integer(string='Edad')
    foto = fields.Binary(string='Foto')
    direccionPaciente = fields.Char(string='Direccion')
    tipodeSangre = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Grupo Sanguineo')
    
    nacionalidadPaciente = fields.Many2one('res.country', string='Nacionalidad')
    #ordenPaciente = fields.Many2one('paciente.orden', string='Orden')
    
    #name = fields.Char(string='Nombre', computed = '_getname')

    


class Orden(models.Model):
    _name = "paciente.orden"
    _description= "una orden determina que examen se hara"
    
    fechaIngreso = fields.Date(string='Fecha Ingreso', default=datetime.today().date(), required=True)
    fechaImpresion = fields.Date(string='Fecha Impresion')
    examenesOrden = fields.One2many('paciente.examen', inverse_name='orden', string='Examenes')
    pacienteOrden = fields.Many2one(comodel_name='paciente.paciente', string='Paciente')
    



    


    
    
    
    
    
    
    
