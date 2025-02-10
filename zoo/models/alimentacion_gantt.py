from datetime import timedelta
from odoo import models, fields,api

class AlimentacionGantt(models.Model):
    _name = 'alimentacion.gantt'
    _description = 'Alimentacion Animales'
    
    name = fields.Char(string="Nombre Zona")
    start_time = fields.Datetime(string="Hora y dia de la comida")
    duration = fields.Integer(string="Duracion (minutos)")
    stop_time = fields.Datetime(string="Tiempo fin", compute="_compute_stop_time", store=True)
    zoo_id = fields.Many2one('zoo', string="Zoológico",required=True)
    zona_id = fields.Many2one('zoo.zona', string='Zona', help='Zona on viu el animal')



@api.depends('start_time', 'duration')
def _compute_stop_time(self):
    for record in self:
        if record.start_time and record.duration:
            record.stop_time = record.start_time + timedelta(minutes=record.duration)
        else:
            record.stop_time = False