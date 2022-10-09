from odoo.tests import tagged
from .common import SaleOrderTransactionCase


@tagged("post_install", "-at_install","standard")
class TestSaleOrderLineSequence(SaleOrderTransactionCase):
    def test_create_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        self.check_assertEqual(line_1)
    
    def test_move_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        line_1[0].sequence = 2
        line_1[1].sequence = 3
        line_1[2].sequence = 1
        self.check_assertEqual(line_1)
        
    def test_delete_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        line_1[0].unlink()
        self.check_assertEqual(line_1)
    
    def test_delete_line(self):
        line = self.sale_order_line[0]
        line.unlink()
        order = self.sale_order_form1
        line_1 = order.order_line
        self.check_assertEqual(line_1)
        
    def check_assertEqual(self,lines):
        counter = 1
        for line in lines:
            self.assertEqual(
                line.sequence,
                counter,
                msg=f"Sequence must be equal {counter}",
            )
            counter += 1
    