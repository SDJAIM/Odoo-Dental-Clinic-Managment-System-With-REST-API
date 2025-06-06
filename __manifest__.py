# -*- coding: utf-8 -*-
{
    'name': 'Dental Clinic Management System',
    'version': '18.0.1.0.0',
    'sequence': -101,
    'category': 'Healthcare',
    'summary': 'Manage dental clinic appointment, patient, and prescription.',
    'description': """Comprehensive dental practice management system for Odoo 18
    - Patient records
    - Appointment scheduling
    - Treatment planning
    - Prescription management""",
    'depends': ['base', 'account', 'calendar', 'mail', 'portal', 'website', 'sale'],
    'data': [
        # 'security/security.xml',
        #'security/ir.model.access.csv',
        'data/data.xml',
        'views/appointment_view.xml',
        'views/patient_view.xml',
        'views/Patient_Appointment_Form_view_customization.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dental_clinic/static/src/js/ToothChart.js',
            'dental_clinic/static/src/scss/toothChart.scss',
        ],
        'web.qweb': [
            'dental_clinic/static/src/xml/toothChart.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
