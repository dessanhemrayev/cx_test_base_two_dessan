from odoo.tests import Form, TransactionCase


class SaleOrderTransactionCase(TransactionCase):
    def setUp(self):
        super(SaleOrderTransactionCase, self).setUp()
        self.sale_order = self.env["sale.order"]
        self.sale_order_line = self.env["sale.order.line"]
        self.partner = self.env.ref(
            "base.res_partner_1"
            )
        self.product_product_test_1 = self.env.ref(
            "product.product_product_1"
            )
        self.product_product_test_2 = self.env.ref(
            "product.product_product_2"
            )
        self.product_product_test_3 = self.env.ref(
            "product.product_product_3"
            )


        form = Form(self.sale_order)
        form.partner_id = self.partner
        with form.order_line.new() as line:
            line.product_id = self.product_product_test_1
            line.price_unit = 500
            line.product_qty = 5.0
        with form.order_line.new() as line:
            line.product_id = self.product_product_test_2
            line.price_unit = 100
            line.product_qty = 3.0
        with form.order_line.new() as line:
            line.product_id = self.product_product_test_3
            line.price_unit = 50
            line.product_qty = 1.0  
        self.sale_order_form1 = form.save()





        