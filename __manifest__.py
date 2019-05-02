# -*- coding: utf-8 -*-
{
    'name': "LaboratorioHn",

    'summary': """
       El siguiente modulo permite registrar los pacientes, registrar sus examenes e imprimirlos""",

    'description': """
        El siguiente modulo administra las dependencias de un laboratorio clinico
    """,

    'author': "Alex Palacios",
    'website': "http://www.LabChatoyer.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Prueba',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}