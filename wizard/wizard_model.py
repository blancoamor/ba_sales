from openerp import models, fields, api, _
from openerp.exceptions import except_orm
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
	list_price_update = fields.Float('Porcentaje Precio Venta')
	cost_price_update = fields.Float('Porcentaje Precio Costo')

	@api.multi
	def update_costs(self):
		import pdb;pdb.set_trace()
		return None
