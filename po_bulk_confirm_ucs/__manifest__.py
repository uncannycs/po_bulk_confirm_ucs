{
    'name': 'Purchase Order Bulk Confirm Ucs',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Purchase',
    'summary': 'Confirm multiple RFQs/Purchase Orders in one click from list view',
    'description': """
Purchase Order Bulk Confirm
===========================
This module allows users to select multiple Purchase Orders or Request for Quotations (RFQs) 
from the list view and confirm them all at once using a bulk confirm wizard.

Key Features:
-------------
* **Bulk confirm in one action**: Select multiple purchase orders and confirm all eligible records in one step.
* **State-based filtering**: Only purchase orders in 'Draft' or 'RFQ Sent' state are confirmed; other states are automatically skipped.
* **Confirmable preview**: The wizard displays a clear list of all eligible purchase orders that will be confirmed.
* **Dynamic counters**: Displays live counts of confirmable and skipped purchase orders before execution.
* **Safety validation**: Prevents empty operations by raising a warning if no selected purchase orders are eligible for confirmation.
* **Uses standard Odoo behavior**: Uses standard `button_confirm()` method for each order.
    """,
    'website': 'https://uncannycs.com',
    'author': 'Uncanny Consulting Services LLP',
    'maintainer': 'Uncanny Consulting Services LLP',
    'license': 'Other proprietary',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_order_bulk_confirm_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    "images": ['static/description/banner.gif'],
    "price": 20,
    "currency": "USD"
}
