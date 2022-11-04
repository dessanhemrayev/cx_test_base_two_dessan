from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    
    line_number = fields.Integer(
        string="Line Number",
        readonly=True,
        compute = 'compute_line_number',
        # store = True
    )
    
    @api.depends('order_id.order_line')
    def _compute_line_number(self):
        order_ids = self.mapped('order_id')
        for order in order_ids:
            count = 1
            for line in order.order_line:
                line.line_number = count
                line.sequence = count
                count += 1
