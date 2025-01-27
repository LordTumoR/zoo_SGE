from odoo.exceptions import ValidationError
from odoo import fields,models,api



class Animal(models.Model):
    _name = 'animal'
    _description = 'Animal Model'
    
    raza = fields.Char()
    continent_origen = fields.Selection([
    ('africa', 'Àfrica'),
    ('antartida', 'Antàrtida'),
    ('asia', 'Àsia'),
    ('europa', 'Europa'),
    ('america', 'Amèrica'),
    ('oceania', 'Oceania')
    ], string="Continent")
    data_naix = fields.Date(string="Data de naixement", required=True)
    
    #obtindre els paisos
    pais_origen = fields.Many2one('res.country',  string="País d'origen",  required=True)
    Genere = fields.Selection([
    ('masculi', 'Masculi'),
    ('femeni', 'Femeni')], string="Sexe")
    #relaio
    #especie = fields.Many2one('especie', string="Especie", required=True)
    
    @api.constrains('data_naix')
    def _check_date_field(self):
        for record in self:
            if record.data_naix <= fields.Date.today():
                raise ValidationError("La fecha ingresada debe ser mayor a la fecha de hoy.")