 # -*- coding: utf-8 -*-

from odoo import models, fields

class academy_teacher(models.Model):
     _name = 'newproject.teacher'
     _description='THe Instructor Osama '

     name = fields.Char(string='course name', required=True, help='name',index=True)
     #index help search faster

     active = fields.Boolean(default=True)

     completed = fields.Boolean()

     text = fields.Text()

     notes = fields.Text()

     expereience = fields.Text()

     gender = fields.Selection(string='gender type',selection=[('M','Male'),('F','Female')],required=False)
                                                             # database,#views

     price = fields.Float(digits=(5, 9))

     days = fields.Integer()

     icon = fields.Binary(attachment=True)

     image = fields.Image()

     description = fields.Text()

     date = fields.Date()

     start_time = fields.Datetime()

     end_time = fields.Datetime()

     Courses_ids = fields.One2many(
    comodel_name='newproject.instructor1',
    inverse_name='instructors_id',
    string='Courses_ids',
    )
#     inverse_name='', ده هضيف اسم الفيلد اللى منى تو وان مربوط بيه

     Course_id = fields.Many2many(comodel_name='newproject.instructor1')
# relationده اللى هو ربط بن المودولات


# class newproject(models.Model):
#     _name = 'newproject.newproject'
#     _description = 'newproject.newproject'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

