# -*- coding: utf-8 -*-
from odoo import http

# class LaboratorioHn(http.Controller):
#     @http.route('/laboratorio_hn/laboratorio_hn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laboratorio_hn/laboratorio_hn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('laboratorio_hn.listing', {
#             'root': '/laboratorio_hn/laboratorio_hn',
#             'objects': http.request.env['laboratorio_hn.laboratorio_hn'].search([]),
#         })

#     @http.route('/laboratorio_hn/laboratorio_hn/objects/<model("laboratorio_hn.laboratorio_hn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laboratorio_hn.object', {
#             'object': obj
#         })