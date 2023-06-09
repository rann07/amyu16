from odoo import models, fields


class ClassOfShares(models.Model):
    _name = 'class.of.shares'
    _description = "Class of Shares"

    name = fields.Char(string="Class of Shares")
    par_value = fields.Integer(string="Par Value per Share", default='')
    column_3 = fields.Char(string="Authorized")
    authorized_no = fields.Integer(string="No.")
    authorized_amount = fields.Float(string="Amount")
    column_4 = fields.Char(string="Subscribed")
    subscribed_no = fields.Integer(string="No.")
    subscribed_amount = fields.Float(string="Amount")
    column_5 = fields.Char(string="Treasury")
    treasury_no = fields.Integer(string="No.")
    treasury_amount = fields.Float(string="Amount")
    column_6 = fields.Char(string="Paid-Up")
    paid_up_no = fields.Integer(string="No.")
    paid_up_amount = fields.Float(string="Amount")
    client_share_ids = fields.Many2one(comodel_name='client.profile', string="Class")
