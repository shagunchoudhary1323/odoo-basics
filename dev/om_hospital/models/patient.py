# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True, track_visibility="always")
    patient_age = fields.Integer('Age', track_visibility="always", group_operator=False)
    email_id = fields.Char(track_visibility="True", string="Email")
    notes = fields.Text(track_visibility="True", string="Registration Note")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', track_visibility="True", string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", store=True)
    is_child = fields.Boolean(track_visibility="True", string='Is Child?')
    active = fields.Boolean(track_visibility="True", string="Active", default=True)
    capitalized_name = fields.Char(string="Capitalized Name", compute="_compute_capitalized_name", store=True,
                                   track_visibility="always")
    ref = fields.Char('Reference', default=lambda self: ('New'))
    patient_image = fields.Binary(string="Image")

    @api.model
    def create(self, vals):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient') or ('New')
            return super(HospitalPatient, self).create(vals)


    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    @api.depends('patient_name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.patient_name:
                rec.capitalized_name = rec.patient_name.upper()
            else:
                rec.capitalized_name = ""

    def act_confirm(self):
        return


