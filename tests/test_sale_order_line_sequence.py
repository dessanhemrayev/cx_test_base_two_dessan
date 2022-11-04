from odoo.tests import tagged

from .common import SaleOrderTransactionCase


@tagged("post_install", "-at_install")
class TestSaleOrderLineSequence(SaleOrderTransactionCase):
    def test_create_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        line_1.compute_line_number()
        self.assertEqual(line_1[0].sequence, 1, msg="Sequence must be equal 1")
        self.assertEqual(line_1[1].sequence, 2, msg="Sequence must be equal 2")
        self.assertEqual(line_1[2].sequence, 3, msg="Sequence must be equal 3")

    def test_move_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        line_1[0].line_number = 2
        line_1[1].line_number = 3
        line_1[2].line_number = 1
        line_1.compute_line_number()
        self.assertEqual(line_1[0].sequence, 1, msg="Sequence must be equal 1")
        self.assertEqual(line_1[1].sequence, 2, msg="Sequence must be equal 2")
        self.assertEqual(line_1[2].sequence, 3, msg="Sequence must be equal 3")

    def test_delete_order_line_sequence(self):
        order = self.sale_order_form1
        line_1 = order.order_line
        order_line = line_1[1]
        order_line.unlink()
        line_1.compute_line_number()
        self.assertEqual(line_1[0].sequence, 1, msg="Sequence must be equal 1")
        self.assertEqual(line_1[1].sequence, 2, msg="Sequence must be equal 2")
