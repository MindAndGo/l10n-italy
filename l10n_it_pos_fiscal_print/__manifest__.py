# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Leonardo Donelli <learts92@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    
     "name": "Driver for ePOS-Print XML compatible fiscal printers",
    "summary": "ePOS-Print XML Fiscal Printer Driver",
    "version": "10.0.1.0.0",
    "development_status": "Alpha",
    "category": "POS, Fiscal, Hardware, Driver",
    "website": "https://github.com/OCA/l10n-italy",
    "author": "Leonardo Donelli,Guillaume Finaud, Abdel Ait Abdelloili, Odoo Community Association (OCA)",
    "maintainers": [],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
#     "pre_init_hook": "pre_init_hook",
#     "post_init_hook": "post_init_hook",
#     "post_load": "post_load",
#     "uninstall_hook": "uninstall_hook",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends":['point_of_sale'],
    "data": [
        "static/src/xml/option_ip_printer_view.xml"
#         "static/src/xml/account_statement_view.xml"
        ]
    
#     "demo": [
#     ],
#     "qweb": [
#      ]
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
