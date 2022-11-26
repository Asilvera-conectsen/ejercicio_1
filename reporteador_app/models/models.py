from odoo import fields, models

class Reporteador(models.Model):
    _name="reporteador_app" #nombre de la tabla
    _descripcion="base de datos de los sensores del Ruptela"

    date = fields.datetime("Fecha") #fecha de ocurrencia de la lectura
    nombre = fields.Char("Nombre") #nombre del Ruptela o del auto donde se lee
    sensor1 = fields.Float("Sensor 1") #los valores registrados por el sensor1

    
