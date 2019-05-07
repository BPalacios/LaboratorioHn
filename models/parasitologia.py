from odoo import api, fields, models


class ExamenParasitologia(models.Model):
    _name = 'examen.parasitologia'
    _description = 'Aqui se detalla todo un general de heces'

    color = fields.Char(string='Color')
    consistencia = fields.Char(string='Consistencia')
    moco = fields.Char(string='Moco')
    sangre = fields.Char(string='Sangre')
    observacion1 = fields.Char(string='Observacion 1')
    observacion2 = fields.Char(string='Observacion 2')
    observacion3 = fields.Char(string='Observacion 3')
    validacionExamen = fields.Boolean(string='Validaddo')
    #Ojo podria ser una clase heredada de Examen al compartir id y el campo de validacion
    #Ademas los resultados podrian ser enviados para examenes comunes
    #Aqui queda la idea, se detalla mas halla



class ParasitosXExamen(models.Model):
    _name = 'parasitologia.pexamen'
    _description = 'Los parasitos habidos y por haber de los examnes de parasitologia'

    #esta tabla relaciona los parasitos y el nivel de incidencia (las cruces ), de cada parasito
    #lo que se manejaba a nivel relacional es agregar 

    #relacion de uno a muchos con parasitologia
    #realcion de muchos a 1 con parasitos

    cruces = fields.Char(string='Cruces')



class Parasito(models.Model):
    _name = 'parasitologia.parasito'
    _description = 'Los parasitos, nombre y descripcion'


    nombreParasito = fields.Char(string='Nombre')
    descripcionParasito = fields.Char(string='Descripcion')
    


class FrotisSangrePeriferica(models.Model):
    _inherit = 'paciente.examen'


    frotisSangre = fields.Boolean(string='FSP', default=True)
    
    plaquetas = fields.Char(string='Plaquetas')
    neutrofilos = fields.Char(string='Neutrofilos')
    linfositos = fields.Char(string='Linfositos')
    eosinofilos = fields.Char(string='Eosinofilos')
    basofilos = fields.Char(string='Basofilos')
    monositos = fields.Char(string='Monositos')
    linfoblastos = fields.Char(string='Linfoblastos')

    alteraciones = fields.One2many(comodel_name='examen.altxfrotis', inverse_name='fsPeriferica', string='Alteraciones')
    


class Alteraciones(models.Model):
    _name = 'examen.altxfrotis'
    _description = 'Alteraciones correspondientes a cada frotis'

    fsPeriferica = fields.Many2one(comodel_name='paciente.examen', string='Frotis de Sangre')
    
    alteracion = fields.Many2one(comodel_name='examen.alteracion', string='Alteracion')
    cruz = fields.Char(string='Cruces')



class Alteracion(models.Model):
    _name = 'examen.alteracion'
    _description = 'Alteracion existente'

    alteracion = fields.Char(string='Alteracion')
    tipoAlteracion = fields.Char(string='Tipo Alteracion')
    
    

    
    
    
    
    
    
