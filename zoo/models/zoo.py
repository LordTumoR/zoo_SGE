from odoo.exceptions import ValidationError
from odoo import fields,models,api

class Zoo(models.Model):
    _name = 'zoo'
    _description = 'Zoo Animal'
    
    grandaria = fields.Integer(string="Superficie en (m2)",)
    nom = fields.Char(string="Name", required=True)
    #ciutat = fields.Many2one('res.city',  string="Ciutat on s'ubica",  required=True)
    pais = fields.Many2one('res.country',  string="País on s'ubica",  required=True)
    #relacio
    #zoo = fields.One2many('animal', string = "animal del zoo")
    @api.constrains('grandaria')
    def _check_grandaria_positive(self):
        for record in self:
            if record.grandaria < 0:
                raise ValidationError("La grandaria no pot ser negativa")