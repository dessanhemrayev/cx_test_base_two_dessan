{
    "name": "Sale orderline sequence",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "",
    "summary": """Добавить нумерацию строк Заказа Продаж (Sales Order).
                  Нумерация должна дополнять существующий""",
    "author": "Dessan Hemrayev",
    "website": "https://portal.mtarenda.ru",
    "depends": ["sale"],
    "data": [
        "views/sale_order_view.xml",
        "views/report_saleorder.xml"],
    "installable": True,
    "auto_install": False,
    "post_init_hook": "post_init_hook",
    "application": False,
}
