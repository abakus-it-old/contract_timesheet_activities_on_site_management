{
    'name': "AbAKUS OS/SD contract improvements",
    'version': '1.0',
    'depends': ['website_contract',
                'hr_timesheet_sheet',
                'project_issue',
                'project_issue_sheet'],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Contract',
    'description': """This modules the on site management for contract timesheets activities for AbAKUS.
    
This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.""",
    'data': ['view/account_analytic_account_view.xml',
             'view/hr_analytic_timesheet_view.xml',
             'view/project_issue_view.xml',
             'view/account_analytic_line.xml',
             'view/hr_timesheet_sheet_view.xml',
             'view/project_task_view.xml',
    ],
}
