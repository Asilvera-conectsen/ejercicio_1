from odoo import models, fields, api

class alumnos(models.Model):
    _name = 'alumnos.alumnos'

    name = fields.Many2one('res.partner', string='Alumno')
    dni  = fields.Char(string='DNI', related='name.vat')
    clases = fields.Many2many('clases.clases', string='Clases')

class profesor(models.Model):
    _name = 'profesor.profesor'

    name = fields.Many2one('res.partner', string='Profesor')
    dni  = fields.Char(string='DNI', related='name.vat')


class clase(models.Model):
    _name = 'clases.clases'

    name = fields.Char(string='Nombre de la clase')
    profesor = fields.Many2one('profesor.profesor', string='Profesor')
    max_alumnos = fields.Integer(string='Maximo de alumnos')


#class respartneredit(models.Models):
#    _inherit = 'res.partner'
#
#    tipo = fields.Selection([(1, 'profesor'), (2, 'alumno')])

# class ejercicio_1(models.Model):
#     _name = 'ejercicio_1.ejercicio_1'
#     _description = 'ejercicio_1.ejercicio_1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
