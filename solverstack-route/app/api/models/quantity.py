# coding: utf-8

from __future__ import absolute_import

from app import util
from app.api.models.base_model_ import Model


class Quantity(Model):
    """NOTE: This class is auto generated by the swagger code generator
    program.

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """Quantity - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "Quantity":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Quantity of this Quantity.  # noqa: E501
        :rtype: Quantity
        """
        return util.deserialize_model(dikt, cls)
