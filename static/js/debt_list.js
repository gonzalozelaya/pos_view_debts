/** @odoo-module **/

import { useState } from "@odoo/owl";
import { Component } from "@odoo/owl";
import { Registries } from "@web/core/registry";

class PendingInvoicesPopup extends Component {
    setup() {
        this.state = useState({
            invoices: this.props.invoices || [],
        });
    }

    closePopup() {
        this.trigger("close-popup");
    }
}

PendingInvoicesPopup.template = "PendingInvoicesPopup";
Registries.Component.add("PendingInvoicesPopup", PendingInvoicesPopup);

export default PendingInvoicesPopup;