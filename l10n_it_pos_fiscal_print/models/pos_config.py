# -*- coding: utf-8 -*-
# Copyright (C) 2018 Mind And Go
# @author: Guillaume Finaud, Abdel Ait Abdelloili
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models

class PosConfig(models.Model):
      _inherit = 'pos.config'
      
      ip_printer = fields.Char(string="Adresse imprimante")
      ip_display = fields.Char(String= "Adresse afficheur")
      
