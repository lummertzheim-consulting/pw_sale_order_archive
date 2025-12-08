from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    active = fields.Boolean('Active', default=True)

    def write(self, values):
        if (values.get('active') or values.get('active') == False) and not self.env.user.has_group('pw_sale_order_archive.group_sale_archive'):
            raise ValidationError(_("You have no acesss to archive/unarchive records. Please contact your system administrator."))
        return super(SaleOrder, self).write(values)
