# 	 -*- coding: utf-8 -*-
from openerp import models, fields, api
import datetime


class sale_order(models.Model):
	_inherit = 'sale.order'



	@api.model
	def _cancel_sale_orders(self):
		orders = self.search([('state','=','draft')])
		for order in orders:
			order_date = fields.Datetime.from_string(order.date_order)
			today = datetime.now()
			difference = today - order_date 
			if (difference.seconds / 60) > 30:
				# Cancels order
				order.action_cancel()


class product_product(models.Model):
	_inherit = 'product.product'

	@api.one
	def _compute_supplier_id(self):
		if self.product_tmpl_id.seller_ids:
			self.supplier_id = self.product_tmpl_id.seller_ids[0].name.id

	supplier_id = fields.Many2one('res.partner',string='Proveedor Principal',compute=_compute_supplier_id)

class product_pricelist_item(models.Model):
	_inherit = 'product.pricelist.item'
	supplier_id = fields.Many2one('res.partner',string='Proveedor',domain=[('supplier','=',True)])

