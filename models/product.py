# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class is_fabricant(models.Model):
    _name = 'is.fabricant'
    _description = "Fabricant"

    name = fields.Char("Fabricant", required=True)


class is_marque(models.Model):
    _name = 'is.marque'
    _description = "Marque"

    name = fields.Char("Marque", required=True)


class is_gamme(models.Model):
    _name = 'is.gamme'
    _description = "Gamme"

    name = fields.Char("Gamme", required=True)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    fabricant_id = fields.Many2one('is.fabricant', "Fabricant")
    marque_id    = fields.Many2one('is.marque', "Marque")
    gamme_id     = fields.Many2one('is.gamme', "Gamme")



		
