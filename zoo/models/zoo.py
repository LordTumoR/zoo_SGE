from odoo.exceptions import ValidationError
from odoo import fields,models,api

class Zoo(models.Model):
    _name = 'zoo'
    _description = 'Zoo Animal'
    
    grandaria = fields.Integer(string="Superficie en (m2)",)
    name = fields.Char(string="Name", required=True)
    ciutat = fields.Char(string="Ciutat")
    pais = fields.Many2one('res.country',  string="País on s'ubica",  required=True)
    #relacio
    animal = fields.One2many('animal','zoo',string = "animal del zoo")
    total_animals = fields.Integer(
        string="Total de Animals",
        compute="_compute_total_animals",
        store=True
    )
    @api.depends("animal")
    def _compute_total_animals(self):
        for record in self:
            record.total_animals = len(record.animal)
    @api.constrains('grandaria')
    def _check_grandaria_positive(self):
        for record in self:
            if record.grandaria < 0:
                raise ValidationError("La grandaria no pot ser negativa")