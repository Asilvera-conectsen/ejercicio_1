# -*- coding: utf-8 -*-
# from odoo import http


# class Ejercicio1(http.Controller):
#     @http.route('/ejercicio_1/ejercicio_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejercicio_1/ejercicio_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejercicio_1.listing', {
#             'root': '/ejercicio_1/ejercicio_1',
#             'objects': http.request.env['ejercicio_1.ejercicio_1'].search([]),
#         })

#     @http.route('/ejercicio_1/ejercicio_1/objects/<model("ejercicio_1.ejercicio_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejercicio_1.object', {
#             'object': obj
#         })
