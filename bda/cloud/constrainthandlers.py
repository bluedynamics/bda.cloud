# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public License Version 2

import types
from zope.interface import implements
from interfaces import ICloudConstraintHandler
from cornerstone.browser.base import RequestMixin

from plone.memoize import view

_marker = dict()

class CookieConstraintHandler(RequestMixin):

    implements(ICloudConstraintHandler)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self._constraints = _marker

    @property
    @view.memoize
    def constraints(self):
        if self._constraints is _marker:
            self.initialize()
        return self._constraints

    def initialize(self):
        """handles constraints given by request or cookies"""

        reset = self.requestvalue('cloudreset')
        key = 'CLOUD' # here we would need a namespace

        # RequestMixin uses _cookiename and adds name of login-user to key
        fullkey = self._cookiename(key, False)
        if reset is not None and fullkey in self.request.cookies:
            self.cookieset(key,'')
            self._constraints = []
            return

        constraints = self.requestvalue(key, [])
        if type(constraints) in types.StringTypes:
            constraints = [c.strip() for c in constraints.split('/') if c.strip()]
        newconstraints = self.requestvalue('cloudconstraint', [])
        if type(newconstraints) in types.StringTypes:
            newconstraints = [newconstraints]
        unconstrain = self.requestvalue('cloudunconstraint', [])
        if type(unconstrain) in types.StringTypes:
            unconstrain = [unconstrain]
        if not newconstraints and not unconstrain:
            self._constraints = constraints
        dummy = [constraints.append(nc)
                 for nc in newconstraints if nc not in constraints]
        dummy = [constraints.remove(uc)
                 for uc in unconstrain if uc in constraints]
        cookievalue = '/'.join(constraints)

        self.cookieset(key,cookievalue)
        self._constraints = constraints