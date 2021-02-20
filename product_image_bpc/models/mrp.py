# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import models, fields, api


class MrpBOMLine(models.Model):

    _inherit = 'mrp.bom.line'

    product_image = fields.Binary(string="Image", related="product_id.image_1920")


class MRPProduction(models.Model):

    _inherit = 'mrp.production'

    product_image = fields.Binary(string="Image", related="product_id.image_1920")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: