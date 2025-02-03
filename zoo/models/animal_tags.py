from odoo.exceptions import ValidationError
from odoo import fields,models,api

class AnimalTag(models.Model):
    _name = 'animal.tag'
    _description = 'Animal Tag'

    name = fields.Char(string="Nom del tag", required=True)
    color = fields.Integer(string="Color")