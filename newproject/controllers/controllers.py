# -*- coding: utf-8 -*-
# from odoo import http


# class Newproject(http.Controller):
#     @http.route('/newproject/newproject', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newproject/newproject/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('newproject.listing', {
#             'root': '/newproject/newproject',
#             'objects': http.request.env['newproject.newproject'].search([]),
#         })

#     @http.route('/newproject/newproject/objects/<model("newproject.newproject"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newproject.object', {
#             'object': obj
#         })

