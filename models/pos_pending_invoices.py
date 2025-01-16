from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)
class PosPendingInvoices(models.TransientModel):
    _name = 'pos.pending.invoices'
    _description = 'Facturas sin pagar de un cliente'

    @api.model
    def get_pending_invoices(self, partner_id):
        _logger.info(partner_id)
        if not partner_id:
            return []
        
        # Forzamos modo superusuario y añadimos TODAS las compañías al contexto:
        all_company_ids = self.env['res.company'].sudo().search([]).ids
        ctx = dict(self.env.context, allowed_company_ids=all_company_ids)
    
        # Obtenemos el partner (sin restricción de compañía)
        partner = self.env['res.partner'].sudo().with_context(ctx).browse(partner_id)
        if not partner:
            return []
    
        # Buscar todas las líneas contables de este partner, “posted” y con balance ≠ 0,
        # ignorando restricción de compañía.
        unreconciled_lines = self.env['account.move.line'].sudo().search([
            ('reconciled', '=', False),
            ('account_id.deprecated', '=', False),
            ('account_id.account_type', '=', 'asset_receivable'),
            ('parent_state', '=', 'posted'),
            ('partner_id', '=', partner.id),
            ('balance', '!=', 0),
        ])
        _logger.info(f"Unreconciled Lines: {unreconciled_lines}")
    
        # Obtenemos la información relevante
        return unreconciled_lines.read(['name', 'debit', 'credit', 'balance', 'move_id', 'date', 'currency_id','company_id'])