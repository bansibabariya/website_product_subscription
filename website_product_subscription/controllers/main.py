# -*- coding: utf-8 -*-

from odoo import http, models, SUPERUSER_ID, fields, _
from odoo.http import request

class ProductSubscription(http.Controller):

    @http.route('/product_subscription_form_submit', auth='public', website=True, type='json', csrf=False)
    def product_subscription_form_submit(self, **post):
        if post.get('email') and post.get('product_id'):
            product = request.env['product.template'].sudo().search([('id', '=', int(post.get('product_id')))])
            user = request.env['subscribe.user'].search([('product_id', '=', product.id), ('state', '=', 'req'),('email', '=', post.get('email'))])
            if not user and product:
                product.sudo().write({
                    'subscribe_user_ids' : [(0,0,{ 'email':post.get('email'), 'state':'req'})]
                })
        return True
