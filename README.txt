bda.cloud
=========

bda.cloud provides a generic tag-cloud viewlet for Plone.

In order to use it you have to write a data provider adapter which implements
ICloudData from bda.cloud.interfaces, as documented in bda.cloud.basedata. The
data provider can provide any data and their frequency, for example Plone
keywords or categories. The vocabulary which is used to display in the cloud
comes from another adapter which implement ICloudVocabulary (have a look to
bda.cloud.browser.viewlet on how this vocabulary is used). The configuration
is done via an adapter which implements ICloudConfig from bda.cloud.interfaces.

It is currently used for the categories-cloud in http://bluedynamics.com/
