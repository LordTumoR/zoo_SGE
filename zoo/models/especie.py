from odoo import fields, models



class Especie(models.Model):
    _name = "especie"
    _description = "Especie del Zoo"
    
    nom_vulgar = fields.Char(required = True)
    description = fields.Char()
    perill = fields.Selection([('alt', 'Alt'), ('baix', 'Baix'), ('mitja','Mitja'),('inofensiu','Inofensiu')])
    perill_extincio = fields.Boolean()
    nom_cientific = fields.Char()
    Familia = fields.Char()
    #camp a relacionar
    #animal = fields.One2many('animal', 'especie', string='Animal')