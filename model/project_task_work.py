from openerp import models, fields, api

class project_task_work_improvements(models.Model):
    _inherit = ['project.task.work']

    related_on_site = fields.Boolean(related='hr_analytic_timesheet_id.line_id.on_site', store=False)