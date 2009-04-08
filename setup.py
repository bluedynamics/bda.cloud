# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public License Version 2

from setuptools import setup, find_packages

version = '2.0'
shortdesc = 'Genric Tag-Cloud for Plone'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='bda.cloud',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='http://svn.plone.org/svn/collective/bda.cloud',
      license='GPL',    
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda',],            
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'cornerstone.browser',
          'cornerstone.ui.spinner',
          'cornerstone.plone.profiles',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
