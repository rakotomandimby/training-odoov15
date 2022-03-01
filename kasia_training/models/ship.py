# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ship(models.Model):
    _name = 'kasia_training.ship'
    _description = 'Ship of the Kasia training module'
    name = fields.Char(required=True)
    type = fields.Selection([
        ('tanker', 'Tanker'),
        ('cargo', 'Cargo'),
        ('cruiser', 'Cruiser')])
    buildDate = fields.Date()
    length=fields.Integer()
    about=fields.Html(string='About')
