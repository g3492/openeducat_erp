# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields


class OpMarksheetRegister(models.Model):
    _name = 'op.marksheet.register'

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam', required=True)
    marksheet_line = fields.One2many(
        'op.marksheet.line', 'marksheet_reg_id', 'Marksheets')
    generated_date = fields.Date('Generated Date', required=True)
    generated_by = fields.Many2one(
        'res.users', 'Generated By', required=True)
    status = fields.Selection(
        [('d', 'Draft'), ('v', 'Validated'), ('c', 'Cancelled')],
        'Status', required=True)
    total_pass = fields.Float('Total Pass')
    total_failed = fields.Float('Total Fail')
    name = fields.Char('Marksheet Register', size=256, required=True)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
