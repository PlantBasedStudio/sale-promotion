# Copyright 2022 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class CouponRule(models.Model):
    _inherit = "coupon.rule"

    strict_per_product_limit = fields.Boolean(
        help="In a discount on selected products reward for every product meeting the "
        "product domain condition, the minimum quantity/amount will be computed "
        "separately",
    )
