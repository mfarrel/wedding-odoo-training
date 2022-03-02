from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Table panggung'

    name = fields.Char(string='Name', required=True)
    pelaminan = fields.Many2one(comodel_name= "wedding.pelaminan", string='Tipe Pelaminan')
    kursi = fields.Many2one(comodel_name='wedding.kursi', string='Tipe Kursi')
    bunga = fields.Selection(string='Tipe Bunga', 
            selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup')])
    accesories = fields.Char(string='Accesories Pelaminan')
    harga = fields.Integer(compute="_compute_harga", string='Harga')
    
    @api.depends('pelaminan','kursi')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan.harga + record.kursi.harga

    # oofcompute 
    # field_name = fields.Char(compute='_compute_field_name', string='field_name')
    
    # @api.depends('')
    # def _compute_field_name(self):
    #     pass