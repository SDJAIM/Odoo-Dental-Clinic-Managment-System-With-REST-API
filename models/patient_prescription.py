from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import date, timedelta


class PatientPrescription(models.Model):
    _name = "patient.prescription"
    _description = "Patient Prescription"
    _order = "prescription_date desc"

    prescription_serial = fields.Char(
        string="Prescription Serial",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("New Prescription")
    )
    prescription_date = fields.Date(
        'Date of Formulation',
        default=fields.Date.context_today
    )
    patient_id = fields.Many2one(
        'patient.patient',
        string="Patient",
        related="appointment_id.patient_id",
        store=True,
        readonly=True
    )
    appointment_id = fields.Many2one('patient.appointment', string="Appointment", ondelete='cascade')
    appointment_id_name = fields.Char(
        'Appointment Serial',
        related='appointment_id.appointment_serial',
        readonly=True
    )
    prescription_line_id = fields.One2many(
        "patient.prescription.line",
        "prescription_id",
        string="Medicines"
    )
    notes = fields.Text("Notes")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('prescription_serial', _('New Prescription')) == _('New Prescription'):
                vals['prescription_serial'] = self.env['ir.sequence'].next_by_code(
                    'patient.appointment.prescription.sequence'
                ) or _('New Prescription')
        return super().create(vals_list)


class PatientPrescriptionLine(models.Model):
    _name = "patient.prescription.line"
    _description = "Patient Prescription Line"

    prescription_id = fields.Many2one(
        'patient.prescription',
        string="Prescription",
        ondelete='cascade',
        index=True
    )
    prescription_id_name = fields.Char(
        related='prescription_id.prescription_serial',
        string='Prescription Serial',
        readonly=True
    )
    medicine_trade_name = fields.Char("Trade Name", required=True)
    therapeutic_regimen = fields.Char("Therapeutic Regimen", required=True)

