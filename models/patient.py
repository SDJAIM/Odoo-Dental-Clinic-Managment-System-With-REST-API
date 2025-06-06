from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import date


class Patient(models.Model):
    _name = "patient.patient"
    _inherit = ['mail.thread']
    _rec_name = "patient_name"

    patient_serial = fields.Char(string="Patient Serial", required=True, copy=False, readonly=True, index=True, default=lambda self: _("New Patient"))
    patient_name = fields.Char('Patient Name')
    contact_number = fields.Char('Contact Number', tracking=True)
    appointment_id = fields.One2many('patient.appointment', 'patient_id')
    date_of_birth = fields.Date(string='Date Of Birth', default=date.today())
    age = fields.Char(string='Age In Years', compute="compute_age", store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=False, string="Gender", tracking=True)
    occupation = fields.Char('Occupation')
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
    ], required=False, string="Marital Status", tracking=True)
    blood_type = fields.Selection([
        ('a-', 'A without Rh-factor'),
        ('a+', 'A with Rh-factor'),
        ('b-', 'B without Rh-factor'),
        ('b+', 'B with Rh-factor'),
    ], required=False, string="Blood Typing", tracking=True)

    qstn_1 = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),], required=False)
    qstn_1_note = fields.Char()
    qstn_2 = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),], required=False)
    qstn_2_note = fields.Char()

    patient_prescriptions = fields.One2many('patient.prescription', 'patient_id')



    @api.depends('date_of_birth')
    def compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                delta = today - record.date_of_birth
                years = delta.days // 365
                record.age = f"{years} Years"
            else:
                record.age = False
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('patient_serial', _('New Patient')) == _('New Patient'):
                vals['patient_serial'] = self.env['ir.sequence'].next_by_code('patient.sequence') or _('New Patient')
        return super().create(vals_list)

