#
# Copyright 2008, Blue Dynamics Alliance, Austria - www.bluedynamics.com
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

import types
from zope.interface import implements
from interfaces import ICloudConstraintHandler

_marker = dict()

class CookieConstraintHandler(object):
    
    implements(ICloudConstraintHandler)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self._constraints = _marker
        
    @property 
    def constraints(self):
        if self._constraints is _marker:
            self.initialize()
        return self._constraints

    def initialize(self):
        """handles constraints given by request or cookies"""
        reset = self.request.form.get('cloudreset', None) # here we would need a namespace
        key = 'CLOUD' # here we would need a namespace      
        if reset is not None and key in self.request.cookies:            
            self.request.RESPONSE.setCookie(key, '', path='/')
            self._constraints = []
            return    
        constraints = self.request.cookies.get(key, []) or []
        if type(constraints) in types.StringTypes:
            constraints = [c.strip() for c in constraints.split('/') if c.strip()]
        newconstraints = self.request.form.get('cloudconstraint', [])
        if type(newconstraints) in types.StringTypes:
            newconstraints = [newconstraints]
        unconstrain = self.request.form.get('cloudunconstraint', [])
        if type(unconstrain) in types.StringTypes:
            unconstrain = [unconstrain]
        if not newconstraints and not unconstrain:
            self._constraints = constraints
        dummy = [constraints.append(nc) 
                 for nc in newconstraints if nc not in constraints]
        dummy = [constraints.remove(uc) 
                 for uc in unconstrain if uc in constraints]
        cookievalue = '/'.join(constraints)
        self.request.RESPONSE.setCookie(key, cookievalue, path='/')
        self._constraints = constraints
        