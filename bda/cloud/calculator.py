#
# Copyright 2007 by BlueDynamics Alliance, Klein & Partner KEG, Austria
#
# GNU General Public License (GPL)
#

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'
__version__ = 1.0

from zope import interface
from zope import component
import interfaces

class LinearCloud(object):
    """a cloud where the weight is linear."""
    
    interface.implements(interfaces.ICloudCalculator)
    component.adapts(interfaces.ICloudData)
    
    def __init__(self, data):
        self.data = data        
    
    @property
    def keys(self):
        return self.data.keys()
    
    def weightOf(self, key):
        min = self.data.minAmount()
        max = self.data.maxAmount()
        rangemax = float(max-min)+1        
        amount = self.data.amountOf(key)
        base = float(amount - min + 1)
        weight = base / rangemax
        return weight
    
    
class LogarithmicCloud(LinearCloud):
    """a cloud with logarithmic weigthing.
    
    thx to Mr.Anders for his article at 
    http://thraxil.com/users/anders/posts/2005/12/13/scaling-tag-clouds/
    """    
    
    interface.implements(interfaces.ICloudCalculator)
    component.adapts(interfaces.ICloudData)

    def __init__(self, data):
        self.data = data    
        self.levels = 10 
        
    def setLevels(self, levels):   
        self.levels = levels 
    
    def weightOf(self, key):
        min = self.data.minAmount()
        max = self.data.maxAmount()
        rangemax = float(max-min)+1        
        thresholds = [pow(rangemax, float(i) / float(self.levels)) 
                      for i in range(0, self.levels)]        
        amount = self.data.amountOf(key)
        if amount == 0:
            return 0        
        # XXX: somewhere in here is probably a bug
        for i in range(0, self.levels):            
            if amount <= thresholds:
                weight = i * ( 1.0 / self.levels)
                print weight
                return weight
        return 1.0 # maxweigth 
        
