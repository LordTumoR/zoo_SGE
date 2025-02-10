from odoo import models, fields, api

class ZonaZoologico(models.Model):
    _name = 'zoo.zona'
    _description = 'Zonas del Zoologic'

    name = fields.Char(string='Nom de la Zona', required=True)
    capacitat_maxima = fields.Integer(string='Capacitat Máxima')
    animals_ids = fields.One2many('animal', 'zona_id', string='Animals')  
    zoo_id = fields.Many2one('zoo', string="Zoológico")
    alimentacion_ids = fields.One2many('alimentacion.gantt', 'zona_id', string="Horarios de Alimentación")
    total_animals_per_zona = fields.Integer(
        string="Total de Animales",
        compute="_compute_total_animals_per_zona",
        store=True
    )

    @api.depends('animals_ids')
    def _compute_total_animals_per_zona(self):
        for record in self:
            record.total_animals_per_zona = len(record.animals_ids)
