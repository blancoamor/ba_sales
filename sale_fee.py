# -*- coding: utf-8 -*-
from openerp import models, fields, api


class sale_fee(models.Model):
    _name = 'sale.fee'
    _description = 'Permite indicar que monto agregar por cobro en cuotas'
    _order = "journal_id , bank_id , fee asc"

    @api.one
    @api.depends('journal_id','bank_id','fee')
    def _compute_name(self):
        if self.journal_id and self.bank_id and self.fee:
            self.name = self.journal_id.name + ' - ' + self.bank_id.bic + ' - ' + str(self.fee)
        elif self.journal_id  and self.fee:
            self.name = self.journal_id.name + ' - ' + str(self.fee)
        else :
            self.name = 'N/A'


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            name = name.replace(' ', '%')
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return recs.name_get()

    
    name = fields.Char('Nombre',compute=_compute_name,store=True)

    bank_id = fields.Many2one('res.bank',string='Banco')
    journal_id = fields.Many2one('account.journal',string='Diario',domain=[('type','=','banks')])
    fee = fields.Integer(string='Cuotas',help='Cantidad de cuotas, debe ser menor a 36')
    product_id = fields.Many2one('product.product',string='Producto')
    amount = fields.Float(string='Monto')
    coefficient = fields.Float(string='Coeficiente',help='Porcentaje de coeficiente, debe ser un valor entre 0 y 5')

    sale_order_default = fields.Boolean('Disponible por defecto en presupuestos')
    payment_type = fields.Selection([('credito', 'Credito'),('debito', 'Debito')],default='credito')
    active = fields.Boolean('Activo',default=True)
    fantasy_name = fields.Char('Nombre fantasia')
    ctf = fields.Float(string='C.T.F.',help='Costo total financiado')
    tea = fields.Float(string='TEA',help='Taza Anual')


