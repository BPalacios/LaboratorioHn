from odoo import api, exceptions, models, fields, _
from datetime import datetime
from . import paciente

class Orden(models.Model):
    _name = "paciente.orden"
    _description= "una orden determina que examen se hara"
    
    fechaIngreso = fields.Date(string='Fecha Ingreso', default=datetime.today().date(), required=True)
    fechaImpresion = fields.Date(string='Fecha Impresion')
    examenesOrden = fields.One2many('paciente.examen', inverse_name='orden', string='Examenes')
    pacienteOrden = fields.Many2one(comodel_name='paciente.paciente', string='Paciente')
    
