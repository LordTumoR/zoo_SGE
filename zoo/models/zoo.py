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
    animal_ids = fields.One2many('animal', 'zoo_id', string="Animals del Zoo")
    zona_ids = fields.One2many('zoo.zona', 'zoo_id', string="Zonas del Zoológico")
    total_animals = fields.Integer(
        string="Total de Animals",
        compute="_compute_total_animals",
        store=True
    )
    map_foto_1920 = fields.Image(string="Mapa Photo")

    def action_open_calendar(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Horarios de Alimentación',
            'res_model': 'alimentacion.gantt',
            'view_mode': 'calendar',
            'domain': [('zoo_id', '=', self.id)],
            'target': 'new',
        }
    alimentacion_ids = fields.One2many('alimentacion.gantt', 'zoo_id', string="Horarios de Alimentación")
    @api.depends("animal_ids")
    def _compute_total_animals(self):
        for record in self:
            record.total_animals = len(record.animal_ids)
    @api.constrains('grandaria')
    def _check_grandaria_positive(self):
        for record in self:
            if record.grandaria < 0:
                raise ValidationError("La grandaria no pot ser negativa")