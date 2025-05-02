from locale import currency  # -*- coding: utf-8 -*-

from odoo import models, fields
from requests import delete
from datetime import datetime , date , time

from odoo17.odoo.api import ondelete


class academy_instructor(models.Model):
     _name = 'newproject.instructor1'
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


     def get_date(self):
          return date.today()
     # if want date from week as exampl           return date.today()-timedelta(days=7)

     date = fields.Date(default=get_date)


     start_time = fields.Datetime()

     currency_id = fields.Many2one(comodel_name='res.currency')

     prices = fields.Monetary()

     end_time = fields.Datetime()

     instructors_id = fields.Many2one(comodel_name='newproject.teacher',ondelete='set null')
     # ondelete = 'cascade '
# std if delete will delete from src
     # ondelete = 'set null'
# if delete will  not delete from src

     # ondelete = 'restrict'
     # will not allow , must delete course first
     # comodel_name هربط مع الموديل اللى اسمه ايه
    # Courses_ids = fields.One2many(
    # comodel_name='newproject.instructor1',
    # inverse_name='instructors_id',
    # string='Courses_ids',
    # )
#     inverse_name='', ده هضيف اسم الفيلد اللى منى تو وان مربوط بيه




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

