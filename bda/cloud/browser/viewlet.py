# -*- coding: utf-8 -*-
#
# Copyright 2007, 2008
# Squarewave Computing - Blue Dynamics Alliance, Austria

__author__ = """Jens Klein <jens@bluedynamics.com>
                Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from zope import component
from zope.component import getMultiAdapter

from Acquisition import aq_inner

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase

from bda.cloud.interfaces import ICloudConfig
from bda.cloud.interfaces import ICloudData
from bda.cloud.interfaces import ICloudCalculator
from bda.cloud.interfaces import ICloudConstraintHandler
from bda.cloud.interfaces import ICloudVocabulary

class CloudViewlet(ViewletBase):
    
    render = ViewPageTemplateFile('viewlet.pt')

    def update(self):
        self.config = ICloudConfig(self.context)
        
    def cloud(self):
        """build the cloud for display according to settings."""
        contentcontext = aq_inner(self.context)
        clouddata = ICloudData(contentcontext)
            
        calculator = component.queryAdapter(clouddata, 
                                            ICloudCalculator, 
                                            self.config.rendertype)        
        if calculator is None:
            return []
        constrainthandler = component.getMultiAdapter(
                                (self.context, self.request),
                                 ICloudConstraintHandler)
        constraints = constrainthandler.constraints
        vocab = ICloudVocabulary(self.context)
        result = []
        for key in calculator.keys:
            entry = {}
            entry['key'] = key
            if key in vocab.keys():
                entry['value'] = vocab[key]
            else:
                entry['value'] = key
            weight = calculator.weightOf(key)
            entry['fontsize'] = weight * (self.config.maxsize - \
                                          self.config.minsize) + \
                                         self.config.minsize
            entry['selected'] = key in constraints
            result.append( entry )
        result.sort(cmp=lambda x, y: cmp(x['value'].lower(), 
                                         y['value'].lower()))
        return result
    
    @property
    def kssattrs(self):
        """Return the managername and the viewletname as kssattrs.
        """
        viewletname = self.__name__
        managername = self.manager.__name__
        pattern = 'kssattr-%s-%s'
        return '%s %s' % (pattern % ('managername', managername),
                          pattern % ('viewletname', viewletname))

