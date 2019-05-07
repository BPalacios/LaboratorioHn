from odoo import api, fields, models


class Examen(models.Model):
    _name = "paciente.examen"
    _description = "Examenes de cualquier indole"

    orden = fields.Many2one(comodel_name='paciente.orden', string='Orden')
    #tipoExamen = fields.Selection(string='', selection=[
    #    ('General', 'General'), ('Quimica General', 'Quimica General'),
    #    ('Quimica Especial','Quimica Especial')],
    #    string="Tipo Examen")
    nombre = fields.Char(string='Examenen')
    resultado = fields.Char(string='Resultado')
    

    #resultadoExamen = fields.Char(string='Resultado')
    validacionExamen = fields.Boolean(string='Validado')
    #quien lo valida, agregar tecnico o doctor




class ExamenQuimico(models.Model):
    _inherit = 'paciente.examen'

    #Clavarle el nobre de quimicas generales o especiales
    listaExamenesQuimicos = fields.Many2one(comodel_name='examen.examenes', string='Examen')
    #dentro de los valores de referencia van las unidades
    
class ListaExamenes(models.Model):
    _name= "examen.examenes"
    _description="Lista de todos los examenes habidos y por haber"

    nombreExamen = fields.Char(string='Examen')
    valRef = fields.Many2one(comodel_name='examen.valoresunidades', string='Valor de Referencia')
    


class ValoresUnidades(models.Model):
    _name = 'examen.valoresunidades'
    _description = 'Son los valores de referencia y unidades de un examen'

    valorReferencia = fields.Char(string='Valor de Referencia')
    unidades = fields.Char(string='Unidades')
    
 


class ExamenParasitologia(models.Model):
    _inherit = 'paciente.examen'
    parasitologia = fields.Boolean(string='Parasitologia', default=True)
    
    color = fields.Char(string='Color')
    consistencia = fields.Char(string='Consistencia')
    moco = fields.Char(string='Moco')
    sangre = fields.Char(string='Sangre')
    observacion1 = fields.Char(string='Observacion 1')
    observacion2 = fields.Char(string='Observacion 2')
    observacion3 = fields.Char(string='Observacion 3')
    parasitos = fields.One2many(comodel_name='parsitologia.pexamen', inverse_name='examen', string='Parasitos')
    
    #Ojo podria ser una clase heredada de Examen al compartir id y el campo de validacion
    #Ademas los resultados podrian ser enviados para examenes comunes
    #Aqui queda la idea, se detalla mas halla



class ParasitosXExamen(models.Model):
    _name = 'parasitologia.pexamen'
    _description = 'Los parasitos habidos y por haber de los examnes de parasitologia'

    examen = fields.Many2one(comodel_name='paciente.examen', string='Examen Parasitologia')
    
    #esta tabla relaciona los parasitos y el nivel de incidencia (las cruces ), de cada parasito
    #lo que se manejaba a nivel relacional es agregar 

    #relacion de uno a muchos con parasitologia
    #realcion de muchos a 1 con parasitos

    parasito = fields.Many2one(comodel_name='parasitologia.parasito', string='Nombre Parasito')
    

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




class Bacteriologia(models.Model):
    _inherit = 'paciente.examenes'

    tipocultivo = fields.Char(string='Tipo Cultivo')
    nColonias = fields.Char(string='Numero de colonias')
    tipoBacteria = fields.Char(string='Tipo Bacteria')
    observacion1 = fields.Text(string='Observacion 1')
    observacion2 = fields.Text(string='Observacion 2')
    observacion3 = fields.Text(string='Observacion 3')
    
    
    
    
    
    

    name = fields.Char(string='Name')

    
    

    
    
    
    
    
    
