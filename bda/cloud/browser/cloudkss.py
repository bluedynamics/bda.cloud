#
# Copyright 2008, BDA - Blue Dynamics Alliance, Austria - www.bluedynamics.com
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from urlparse import urlsplit

from zope.component import getMultiAdapter

from zope.viewlet.interfaces import IViewlet
from zope.viewlet.interfaces import IViewletManager

from kss.core import KSSView
from kss.core import kssaction

class CloudKSS(KSSView):
    
    @kssaction
    def renderCloudViewlet(self, managername, viewletname, href):
        href = href.replace('&#38;', '&') # safari stuff
        query = urlsplit(href)[3]
        parts = query.split('&')
        for part in parts:
            param, value = part.split('=')
            self.request.form[param] = value
        
        toadapt = (self.context, self.request, self)
        manager = getMultiAdapter(toadapt, IViewletManager, name=managername)
        toadapt = (self.context, self.request, self, manager)
        viewlet = getMultiAdapter(toadapt, IViewlet, name=viewletname)
        viewlet = viewlet.__of__(self.context)
        viewlet.update()
        ksscore = self.getCommandSet('core')
        ksscore.replaceHTML('#cloud', viewlet.render())
