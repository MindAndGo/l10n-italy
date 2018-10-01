///*
//Copyright (C) 2017-Today: La Louve (<http://www.lalouve.net/>)
//@author: Sylvain LE GAL (https://twitter.com/legalsylvain)
//License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
//*/

odoo.define('l10n_it_pos_fiscal_print', function(require) {
	use strict";

	var models = require('point_of_sale.models');
	var _super_PosModel = models.PosModel.prototype;
	models.load_fields("pos.order", "ip_printer");
}