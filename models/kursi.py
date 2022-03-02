from odoo import api, fields, models


class Pelaminan(models.Model):
    _name = 'wedding.kursi'
    _description = 'Daftar Kursi'

    name = fields.Char(string='Nama')
    harga = fields.Integer(string='Harga')
    deskripsi = fields.Char(string='Deskripsi')
    
    