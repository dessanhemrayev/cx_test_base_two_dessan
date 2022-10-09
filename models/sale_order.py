from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sequence = fields.Integer(
                            default=9999,
                            string="Sequence",
                            )

    line_number = fields.Integer(
        related="sequence",
        string="Line Number",
        readonly=True,
    )


    @api.model
    def create(self, values):
        line = super(SaleOrderLine, self).create(values)
        if self.env.context.get("keep_line_sequence"):
            line.order_id._reset_sequence()
        return line

    def write(self, line_values):
        res = super(SaleOrderLine, self).write(line_values)
        if 'sequence' in line_values.keys():
            for item in self:
                item.order_id._reset_sequence()
        return res

    def unlink(self):
        order_ids = self.mapped('order_id')
        super(SaleOrderLine, self).unlink()
        for item in order_ids:
            item._reset_sequence()
        return True


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends("order_line")
    def _compute_max_line_sequence(self):
        for sale in self:
            sale.max_line_sequence = max(sale.mapped("order_line.sequence") or [0]) + 1

    max_line_sequence = fields.Integer(
                                        string="Max sequence in lines", 
                                        compute="_compute_max_line_sequence", 
                                        store=True
                                        )


    def _reset_sequence(self):
        for rec in self:
            current_sequence = 1
            for line in sorted(rec.order_line, key=lambda x: (x.sequence, x.id)):
                if line.sequence != current_sequence:
                    line.sequence = current_sequence
                current_sequence += 1


    def write(self, line_values):
        res = super(SaleOrder, self).write(line_values)
        if 'order_line' in line_values.keys():
            for item in self:
                item._reset_sequence()
        return res


    def copy(self, default=None):
        return super(SaleOrder, self.with_context(keep_line_sequence=True)).copy(
            default
        )


