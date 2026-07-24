from odoo import api, fields, models, _
from odoo.exceptions import UserError

class PurchaseOrderBulkConfirm(models.TransientModel):
    _name = 'purchase.order.bulk.confirm'
    _description = 'Purchase Order Bulk Confirm Wizard'

    purchase_order_ids = fields.Many2many(
        'purchase.order',
        string='Purchase Orders',
        readonly=True
    )
    confirmable_count = fields.Integer(
        string='Confirmable Orders Count',
        readonly=True
    )
    skipped_count = fields.Integer(
        string='Skipped Orders Count',
        readonly=True
    )

    @api.model
    def default_get(self, fields_list):
        res = super(PurchaseOrderBulkConfirm, self).default_get(fields_list)
        active_ids = self.env.context.get('active_ids')
        if not active_ids:
            raise UserError(_("Please select at least one purchase order."))

        purchase_orders = self.env['purchase.order'].browse(active_ids)
        confirmable_orders = purchase_orders.filtered(lambda po: po.state in ('draft', 'sent'))

        if not confirmable_orders:
            raise UserError(_("There are no draft or sent purchase orders to confirm."))

        confirmable_count = len(confirmable_orders)
        skipped_count = len(purchase_orders) - confirmable_count

        res.update({
            'purchase_order_ids': [(6, 0, confirmable_orders.ids)],
            'confirmable_count': confirmable_count,
            'skipped_count': skipped_count,
        })
        return res

    def action_confirm_orders(self):
        self.ensure_one()
        if not self.purchase_order_ids:
            raise UserError(_("There are no purchase orders to confirm."))
        self.purchase_order_ids.button_confirm()
        return {'type': 'ir.actions.act_window_close'}
