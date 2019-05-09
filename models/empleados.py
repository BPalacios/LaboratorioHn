from odoo import api, fields, models


class EmpleadoLaboratorio(models.Model):
    _name = 'empleado.laboratorio'
    _description = 'Empleado de Laboratorio que valida el examen'

    nombreCompleto = fields.Char(string='Nombre')
    cargo = fields.Char(string='Cargo')
    