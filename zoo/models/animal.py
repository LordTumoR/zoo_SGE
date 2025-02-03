from odoo.exceptions import ValidationError
from odoo import fields,models,api



class Animal(models.Model):
    _name = 'animal'
    _description = 'Animal Model'
    
    raza = fields.Char(string= 'raza')
    name = fields.Char(required=True)
    continent_origen = fields.Selection([
    ('africa', 'Àfrica'),
    ('antartida', 'Antàrtida'),
    ('asia', 'Àsia'),
    ('europa', 'Europa'),
    ('america', 'Amèrica'),
    ('oceania', 'Oceania')
    ], string="Continent")
    data_naix = fields.Date(string="Data de naixement", required=True)
    dieta = fields.Char()
    habitat = fields.Char()
    vidamedia = fields.Char()
    #obtindre els paisos
    pais_origen = fields.Many2one('res.country',  string="País d'origen",  required=True)
    Genere = fields.Selection([
    ('masculi', 'Masculi'),
    ('femeni', 'Femeni')], string="Sexe")
    #relaio
    especie = fields.Many2one('especie', string="Especie", required=True)
    zoo = fields.Many2one('zoo', string="Zoo")
    tag_ids = fields.Many2many('animal.tag', string="Tags", help="Etiquetes per a classificar els animals")
    image_1920 = fields.Image(string="Animal Photo")
    state = fields.Selection([
        ('salvaje', 'Salvaje'),
        ('domesticado', 'Domesticado'),
        ('enpeligro', 'Enpeligro')
    ], string="Estado", default='salvaje', tracking=True)
    def marcar_protejido(self):
        self.state = 'enpeligro'
    def marcar_salvaje(self):
        self.state = 'salvaje'
    @api.constrains('data_naix')
    def _check_date_field(self):
        for record in self:
            if record.data_naix >= fields.Date.today():
                raise ValidationError("La Data ingresa te que ser menor a la de hui.")