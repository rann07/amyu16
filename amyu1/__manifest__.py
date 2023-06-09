# -*- coding: utf-8 -*-
{
    'name': "A.M.Yu & ASSOCIATES",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Rann Aureada",
    'website': "https://www.amyucpas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cpms_groups.xml',
        'views/state_view.xml',
        'views/associates_profile_view.xml',
        'views/client_profile_view.xml',
        'views/supervisor_view.xml',
        'views/manager_view.xml',
        'views/corporate_officer_view.xml',
        'views/class_of_shares_view.xml',
        'views/escalation_contact.xml',
        'views/client_records_views.xml',
        'views/cmps_menu_view.xml',

    ],
    'application': True,
}
