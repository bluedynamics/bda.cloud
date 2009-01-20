#
# Copyright 2007 by Blue Dynamics Alliance, Klein & Partner KEG, Austria
#
# GNU General Public License (GPL)
#

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'
__version__ = 1.0

from zope.interface import implements
from interfaces import ICloudData

class BaseData(object):
    """abstract base class for lazy programmers."""

    implements(ICloudData)

    def __init__(self, context):
        self.context = context
        self.data = None

    def querydata(self):
        """query data from catalog"""
        raise NotImplementedError, "querydata must be implemented in subclass."

    def keys(self):
        """returns all keys in data"""
        self.querydata()
        return self.data.keys()

    def amountOf(self, key):
        """the amount of a key in data"""
        self.querydata()
        return self.data[key]

    def minAmount(self):
        """the lowest amount"""
        self.querydata()
        ams = [self.data[key] for key in self.data.keys()]
        ams.sort()
        if ams:
            return ams[0]
        else:
            return 0

    def maxAmount(self):
        """the largest amount"""
        ams = [self.data[key] for key in self.data.keys()]
        ams.sort(reverse=True)
        if ams:
            return ams[0]
        else:
            return 0
