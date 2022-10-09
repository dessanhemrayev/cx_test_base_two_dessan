from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    sale = env["sale.order"].search([])
    sale._reset_sequence()
