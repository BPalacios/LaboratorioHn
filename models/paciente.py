# -*- coding: utf-8 -*-

from odoo import models, fields

class Paciente(models.Model):
	_name = 'paciente.paciente'

	pnombrePaciente = fields.Char(string='Primer Nombre', required=True)
	snombrePaciente = fields.Char(string='SeWgundo Nombre', required=False)
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