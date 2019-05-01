# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'LaboratorioHN.Paciente'
    _description = "Paciente del Laboratorio"

    name = fields.Char(string="Paciente", required= True)
    description = fields.Text()


# class laboratorio_hn(models.Model):
#     _name = 'laboratorio_hn.laboratorio_hn'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100