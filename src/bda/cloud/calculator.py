# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public License Version 2

from zope import interface
from zope import component
import interfaces
import math

class LinearCloud(object):
    """a cloud where the weight is linear."""

    interface.implements(interfaces.ICloudCalculator)
    component.adapts(interfaces.ICloudData)

    def __init__(self, data):
        self.data = data

        min = self.data.minAmount()
        max = self.data.maxAmount()
        self.rangemax = float(max-min)+1

    @property
    def keys(self):
        return self.data.keys()

    def weightOf(self, key):
        amount = self.data.amountOf(key)
        base = float(amount - min + 1)
        weight = base / self.rangemax
        return weight


class LogarithmicCloud(LinearCloud):
    """a cloud with logarithmic weigthing.

    thx to Anders Pearson for his article at
    http://thraxil.org/users/anders/posts/2005/12/13/scaling-tag-clouds/
    """

    interface.implements(interfaces.ICloudCalculator)
    component.adapts(interfaces.ICloudData)

    def __init__(self, data):
        super(LogarithmicCloud, self).__init__(data)
        self.levels = 10
        self.thresholds = self.calculate_thresholds()

    def calculate_thresholds(self):
        return [math.pow(self.rangemax, float(i) / float(self.levels))
                for i in range(0,self.levels)]

    def setLevels(self, levels):
        self.levels = levels
        self.thresholds = self.calculate_thresholds()

    def weightOf(self, key):
        amount = self.data.amountOf(key)
        i = 0
        for t in self.thresholds:
            i += 1
            if amount <= t:
                return float(i) / float(self.levels)
        return float(i) / float(self.levels)
