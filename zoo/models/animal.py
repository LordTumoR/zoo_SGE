from odoo import fields,models



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
    Sexe = fields.Selection([
    ('masculi', 'Masculi'),
    ('femeni', 'Femeni')], string="Sexe")
    #relaio
    #especie = fields.Many2one('especie', string="Especie", required=True)