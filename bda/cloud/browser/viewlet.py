# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public License Version 2

from Products.Five import BrowserView

from zope import component
from zope.component import getMultiAdapter
from Acquisition import aq_inner

from bda.cloud.interfaces import ICloudConfig
from bda.cloud.interfaces import ICloudData
from bda.cloud.interfaces import ICloudCalculator
from bda.cloud.interfaces import ICloudConstraintHandler
from bda.cloud.interfaces import ICloudVocabulary


class CloudView(BrowserView):

    def __init__(self, context, request):
        super(CloudView, self).__init__(context, request)
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
