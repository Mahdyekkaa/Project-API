from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date, datetime


class inherit_doctrot(models.Model):
    _inherit = "doctor_doctor"

    def search_for2(self, args):
        self = self.sudo()
        if not args or not isinstance(args, int):
            return "Please Send num"
        num = args
        domian = [('age', '=', num)]
        search = self.env['doctor_doctor'].search(domian)
        if len(search) == 0:
            x = (f"Nobdy = {args}")
            return x
        else:
            return search


def create_partner(self, **kwargs):
    self = self.sudo()

    # parameters validations
    if not kwargs['name'] or not isinstance(kwargs['name'], str):
        return "not supported type for name"
    if not kwargs['age'] or not isinstance(kwargs['age'], str):
        return "not supported type for email"
    if not kwargs['gender'] or not isinstance(kwargs['gender'], str):
        return "not supported type for phone"

    # fill data
    vals = {}
    vals['name'] = kwargs['name']
    vals['age'] = kwargs['age']
    vals['gender'] = kwargs['gender']

    created = self.env['doctor_doctor'].create(vals)
    kwargs['id'] = created.id

    return kwargs
