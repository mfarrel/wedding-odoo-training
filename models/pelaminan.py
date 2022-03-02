from odoo import api, fields, models


class Pelaminan(models.Model):
    _name = 'wedding.pelaminan'
    _description = 'Daftar tip'

    name = fields.Char(string='Nama')
    harga = fields.Integer(string='Harga')
    deskripsi = fields.Char(string='Deskripsi')
    
    
