from odoo import fields,models


class Zoo(models.Model):
    _name = 'zoo'
    _description = 'Zoo Animal'
    
    grandaria = fields.Integer()
    nom = fields.Char(string="Name", required=True)
    #ciutat = fields.Many2one('res.city',  string="Ciutat on s'ubica",  required=True)
    pais = fields.Many2one('res.country',  string="País on s'ubica",  required=True)
    #relacio
    #zoo = fields.One2many('animal', string = "animal del zoo")