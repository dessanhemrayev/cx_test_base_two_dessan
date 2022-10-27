from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    
    line_number = fields.Integer(
        string="Line Number",
        readonly=True,
        compute = 'compute_line_number',
        # store = True
    )

    def compute_line_number(self):
        for order in self.mapped('order_id'):
            count = 1
            for line in order.order_line:
                line.line_number = count
                line.sequence = count
                count += 1

    

