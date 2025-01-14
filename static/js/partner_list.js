/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";

patch(PartnerListScreen.prototype, {
    /**
     * Función personalizada para manejar el botón `PENDIENTES`.
     * Este método se llamará cuando se haga clic en el botón.
     * @param {Object} partner - El socio seleccionado para mostrar las deudas.
     */
    async showDebt(partner) {
    console.log(`Cargando deudas para el socio: ${partner.name}`);

    try {
        const invoices = await this.orm.call(
            "pos.pending.invoices",
            "get_pending_invoices",
            [partner.id]
        );

        console.log("Facturas pendientes:", invoices);

        if (invoices.length > 0) {
            this.showPopup("PendingInvoicesPopup", { invoices });
        } else {
            this.notification.add(`El cliente ${partner.name} no tiene facturas pendientes.`, 3000);
        }
    } catch (error) {
        console.error("Error al obtener facturas del cliente:", error);
        this.notification.add("No se pudieron cargar las facturas. Intente de nuevo.", 3000);
    }
    },
});