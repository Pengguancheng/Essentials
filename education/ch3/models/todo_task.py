# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask (models.Model):
    _name = 'todo.task'
    _inherit = "todo.task"
    user_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=False, )
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")
    @api.multi
    def do_clear_done(self):
        domain = [('is_done','=',True),
                  '|', ('user_id','=',self.env.uid),
                  ('user_id','=',False)]
        done_recs = self.search(domain)
        done_recs.write({'active':False})
        return True
    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user :
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()

