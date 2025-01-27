from odoo import fields, models



class Especie(models.Model):
    _name = "especie"
    _description = "Especie del Zoo"
    
    nom_vulgar = fields.Char(required = True)
    descripcio = fields.Char()
    perill = fields.Selection([('alt', 'Alt'), ('baix', 'Baix'), ('mitja','Mitja'),('inofensiu','Inofensiu')])
    perill_extincio = fields.Boolean(default = False)
    nom_cientific = fields.Char(required = True)
    Familia = fields.Char(required = True)
    #camp a relacionar
    #animal = fields.One2many('animal', 'especie', string='Animal')