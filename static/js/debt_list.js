/** @odoo-module */

import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { usePos } from "@point_of_sale/app/store/pos_hook";

/**
 * Props:
 *  {
 *      info: {object of data}
 *  }
 */
export class PendingInvoicePopup extends AbstractAwaitablePopup {
    static template = "PendingInvoicesPopup";
    static defaultProps = { confirmKey: false };

    setup() {
        super.setup();
        this.pos = usePos();
        Object.assign(this, this.props.info);
        this.invoices = this.props.invoices
        console.log(this.invoices)
    }
    
}