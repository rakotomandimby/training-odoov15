# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Owner(models.Model):
    _name = 'kasia_training.owner'
    _description = 'Ship owner of the Kasia training module'
    name = fields.Char(required=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('all', 'MaleFemale')])
    birthDate = fields.Date()
    about=fields.Html(string='About')
