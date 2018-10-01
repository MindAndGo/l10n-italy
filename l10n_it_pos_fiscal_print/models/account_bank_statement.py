from odoo import models, fields

class AccountJournal(models.Model):

    _inherit = 'account.journal'
#     _columns = {
#         'fiscalprinter_payment_type': fields.selection(
#             (('0', 'Cash'), ('1', 'Cheque'), ('2', 'Credit/Credit Card'), ('3', 'Ticket')),
#             'Payment type',
#             help='The payment type to send to the Fiscal Printer.'
#         ),
#     }
#     _defaults = {
#         'fiscalprinter_payment_type': '0',
#     }
