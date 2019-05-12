from odoo import api, fields, models


class Examen(models.Model):
    _name = "paciente.examen"
    _description = "Examenes de cualquier indole"

    orden = fields.Many2one(comodel_name='paciente.orden', string='Orden')
    #tipoExamen = fields.Selection(string='', selection=[
    #    ('General', 'General'), ('Quimica General', 'Quimica General'),
    #    ('Quimica Especial','Quimica Especial')],
    #    string="Tipo Examen")
    nombre = fields.Char(string='Examen')
    resultado = fields.Char(string='Resultado')
    
    validacionExamen = fields.Boolean(string='Validado')
    realizadoPor = fields.Many2one(comodel_name='empleado.laboratorio', string='Realizado Por:')
    


class EmpleadoLaboratorio(models.Model):
    _name = 'empleado.laboratorio'
    _description = 'Empleado de Laboratorio que valida el examen'

    nombreCompleto = fields.Char(string='Nombre')
    cargo = fields.Char(string='Cargo')
    




class ExamenQuimico(models.Model):
    _inherit = 'paciente.examen'

    quimica = fields.Boolean(string='Quimica', default=False)
    

    #Clavarle el nobre de quimicas generales o especiales
    listaExamenesQuimicos = fields.Many2one(comodel_name='examen.examenes', string='Examen')
    #dentro de los valores de referencia van las unidades
    
class ListaExamenes(models.Model):
    _name= "examen.examenes"
    _description="Lista de todos los examenes habidos y por haber"

    nombreExamen = fields.Char(string='Examen', required=True)
    tipoExamen = fields.Selection(string='Tipo Examen', selection=[('general', 'General'), ('Quimica General', 'Quimica general'), 
            ('Parasitologia', 'Parasitologia'),('Uroanalisis', 'Uroanalisis'),
            ('Quimica Especial','Quimica Especial'), ('Bacteriologia','Baccteriologia')])
    valRef = fields.Many2one(comodel_name='examen.valoresunidades', string='Valor de Referencia')
    unidades = fields.Char(related='valRef.unidades')
    
    


class ValoresUnidades(models.Model):
    _name = 'examen.valoresunidades'
    _description = 'Son los valores de referencia y unidades de un examen'

    valorReferencia = fields.Char(string='Valor de Referencia')
    unidades = fields.Char(string='Unidades')
    @api.multi
    def name_get(self):
        data= []
        for s in self:
            name = s.valorReferencia
            data.append((s.id, name))
        return data

    
 
"""

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

    #en antibigrama, un antibiotico solo debe ir en un lado, o sencible o resistente
    
    antibiograma = fields.One2many(comodel_name='examen.antibiograma', inverse_name='examen', string='Antibioticos')
    

class Antibigrama(models.Model):
    _name = 'examen.antibiograma'
    _description = 'Los antibioticos sencibles o resistentes'
    examen = fields.Many2one(comodel_name='antibiograma', string='Examen')
    
    tipo = fields.Char(string='Sencible o resistente')


class Antibiotico(models.Model):
    _name = 'examen.antibiotico'
    _description = 'Antibioticos del Cultivo'

    nombre = fields.Char(string='Nombre Antibiotico')



class Citologia(models.Model):
    _inherit = 'paciente.examenes'

    calidadMuestra = fields.Char(string='Calidad de Muestra')
    inflamacion = fields.Char(string='Inflamacion')
    microorganismo = fields.Char(string='Microorganismo')
    cambioRepReac = fields.Char(string='Cambio Reparativo Reactivo')
    anormalidadesCelulares = fields.Char(string='Anormalidades Celulares')
    tratamiento = fields.Text(string='Tratamiento')
    observacion1 = fields.Text(string='Observacion 1')
    observacion2 = fields.Text(string='Observacion 2')



class Uroanalisis(models.Model):
    _inherit = 'paciente.examenes'

    color = fields.Char(string='Color')
    olor = fields.Char(string='Olor')
    aspecto = fields.Char(string='Aspecto')
    densidad = fields.Char(string='Densidad')
    ph = fields.Char(string='PH')
    glucosa = fields.Char(string='Glucosa')
    proteinas = fields.Char(string='Proteinas')
    sangre = fields.Char(string='Sangre')
    cetonas = fields.Char(string='Cetonas')
    urobil = fields.Char(string='Urobilinogeno')
    bilirrubina = fields.Char(string='Bilirrubina')
    nitritos = fields.Char(string='Nitritos')
    leucocitosQ = fields.Char(string='Leucocitos')
    celulasEpiteliales = fields.Char(string='Celulas Epiteliales')
    eritrocitos = fields.Char(string='Eritrocitos')
    leucocitos = fields.Char(string='Leucocitos')
    bacterias = fields.Char(string='Bacterias')
    levaduras = fields.Char(string='Levaduras')
    moco = fields.Char(string='Moco')
    cilindros = fields.Char(string='Cilindros')
    cristales = fields.Char(string='Cristales')
    parasitos = fields.Char(string='Parasitos')
    observacion1 = fields.Text(string='Observacion 1')
    observacion2 = fields.Text(string='Observacion 2')
    observacion3 = fields.Text(string='Observacion 3')
    

class Tiempos_Coagulacion(models.Model):
    _inherit = 'paciente.examenes'

    tpPaciente = fields.Char(string='TP Paciente')
    tpControl = fields.Char(string='TP Control')
    ttpPaciente = fields.Char(string='TTP Paciente')
    ttpControl = fields.Char(string='TTP Control')
    INR = fields.Char(string='INR')
    """
    