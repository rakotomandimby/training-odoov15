# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visit(models.Model):
    _name = 'kasia_training.visit'
    _description = 'Ship owner of the Kasia training module'
    name = fields.Char()
    type = fields.Selection([
        ('random', 'Random'),
        ('planned', 'Planned'),
        ('oncomplaint', 'On complaint')])
    occurDate = fields.Date()
    endValidityDate = fields.Date()
    about=fields.Html(string='About')
