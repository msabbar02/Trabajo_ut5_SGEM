# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class drive-go(models.Model):
#     _name = 'drive-go.drive-go'
#     _description = 'drive-go.drive-go'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

