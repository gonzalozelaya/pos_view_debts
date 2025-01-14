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
    
        # Obtiene el cliente
        partner = self.env['res.partner'].sudo().browse(partner_id)
        if not partner:
            return []

        # Obtiene las líneas no conciliadas
        unreconciled_lines = partner.unreconciled_aml_ids.filtered(lambda line: line.move_id.state == 'posted')

        # Retorna la información relevante de las líneas no conciliadas
        return unreconciled_lines.read(['name', 'debit', 'credit', 'balance', 'move_id', 'date', 'currency_id'])