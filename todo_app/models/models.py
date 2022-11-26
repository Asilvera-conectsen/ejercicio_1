# -*- coding: utf-8 -*-
from odoo import models, fields

class ToDo(models.Model):
    _name = "todo.app" #nombre de la base de datos : todo_app
    _descripcion = "Lista de Tareas"
    _rec_name = "description"

    name = fields.Char(string="Nombre")
    state = fields.Char(string="Estado")
    description = fields.Char(string="Descripcion")
    #title = fields.Char(string="Titulo")
    #price = fields.Float(string="Precio")
    #cost = fields.Float(string="Costo")