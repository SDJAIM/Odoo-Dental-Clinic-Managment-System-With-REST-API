from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

from datetime import date, timedelta

class ClinicDoctor(models.Model):
    _name = "clinic.doctor"
    _rec_name = "doctor_name"
    _description = "Clinic Doctor"

    doctor_name = fields.Char("Doctor Name", required=True)
    is_available = fields.Boolean("Available for Appointments", default=True, tracking=True)
    email = fields.Char("Email")
    phone = fields.Char("Phone Number")
    appointment_id = fields.One2many('patient.appointment', 'doctor_id', string="Appointments")

