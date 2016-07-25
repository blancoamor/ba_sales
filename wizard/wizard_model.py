from openerp import models, fields, api, _
from openerp.exceptions import except_orm, ValidationError
from openerp.osv import osv
import urllib2, httplib, urlparse, gzip, requests, json
from StringIO import StringIO
import openerp.addons.decimal_precision as dp
import logging
import ast
#Get the logger
_logger = logging.getLogger(__name__)

class product_update_prices(models.TransientModel):
	_name = 'product.update.prices'

	categ_id = fields.Many2one('product.category',string='Categoria')
	product_id = fields.Many2one('product.product',string='Producto')
	supplier_id = fields.Many2one('res.partner',string='Proveedor',domain=[('supplier','=',True)])
	list_price_update = fields.Float('Porcentaje Precio Venta',default=0)
	cost_price_update = fields.Float('Porcentaje Precio Costo',default=0)

	@api.multi
	def update_costs(self):
		import pdb;pdb.set_trace()
		if not self.categ_id and not self.supplier_id and not product_id:
			raise ValidationError("Debe ingresar al menos un parametro de actualizacion")
		if self.list_price_update < 0 or self.list_price_update > 100:
			raise ValidationError("El precio de venta a ingresar solo puede ser aumentando entre un 0% y 100%")
		if self.cost_price_update < 0 or self.cost_price_update > 100:
			raise ValidationError("El costo a ingresar solo puede ser aumentando entre un 0% y 100%")
		domain = []
		if self.categ_id:
			domain.append(('categ_id','=',self.categ_id.id))
		if self.supplier_id:
			domain.append(('supplier_id','=',self.supplier_id.id))
		if self.product_id:
			domain.append(('id','=',self.product_id.id))
		products = self.env['product.product'].search(domain)
		for product in products:
			cost = product.standard_price
			lst_price = product.list_price
			vals = {}
			if self.list_price_update > 0:
				vals['lst_price'] = lst_price * ( 1 + self.list_price_update )
			if self.cost_price_update > 0:
				vals['standard_price'] = cost * ( 1 + self.cost_price_update )
			product.write(vals)
		return None
