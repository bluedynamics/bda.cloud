#
# Copyright 2008, Blue Dynamics Alliance, Austria - www.bluedynamics.com
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.interface import Attribute
from zope import schema

from Products.CMFPlone import PloneMessageFactory as _


class ICloudData(Interface):
    """a generic interface for data used as base for a cloud"""

    keys = Attribute(u"returns all keys in data")

    minAmount = Attribute(u"the lowest amount")

    maxAmount = Attribute(u"the largest amount")

    def amountOf(key):
        """the amount of a key in data"""


class ICloudCalculator(Interface):
    """calculates the cloud itself """

    keys = Attribute("returns a list keys for the cloud.")

    def weightOfKey(key):
        """returns the weight of a given key as floot value between 0 and 1."""


class ICloudConstraintHandler(Interface):
    """general handler for constraints"""

    constraints = Attribute(u"constraints as a dict")

    def initialize(self):
        """processes the constraints from the feeding sources"""


class ICloudVocabulary(Interface):

    vocabulary = Attribute(u'keys and values of the vocabulary to show')


class ICloudConfig(Interface):
    """Interface for the cloud displaying configuration.
    """

    minsize = schema.Int(
            title=_(u'Miminum font size'),
            description=_(u'Smallest font used'),
            required=True,
            default=4)

    maxsize = schema.Int(
            title=_(u'Maximum font size'),
            description=_(u'Biggest font used'),
            required=True,
            default=35)

    resetlabel = schema.TextLine(
            title=_(u"Reset"),
            description=_(u"The label-text of the reset search link."),
            default=u"Reset",
            required=True)

    resetsize = schema.Int(
            title=_(u'Reset label font size'),
            description=_(u'Font size of reset link'),
            required=True,
            default=15)

    rendertype = schema.Choice(
            ('linear', 'logarithmic'),
            title=_(u'Method of Calculation'),
            description=_(u'Choose of the method to caculate the sizes of the font based the subjects weigth.'),
            required=True,
            default='linear')

    display = Attribute(u'Bool wether to show the viewlet or not')


class ICloudLayer(Interface):
    """A Layer for bda.cloud."""
