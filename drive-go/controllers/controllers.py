# -*- coding: utf-8 -*-
# from odoo import http


# class Drive-go(http.Controller):
#     @http.route('/drive-go/drive-go', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drive-go/drive-go/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('drive-go.listing', {
#             'root': '/drive-go/drive-go',
#             'objects': http.request.env['drive-go.drive-go'].search([]),
#         })

#     @http.route('/drive-go/drive-go/objects/<model("drive-go.drive-go"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drive-go.object', {
#             'object': obj
#         })

