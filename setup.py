# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public License Version 2

from setuptools import setup, find_packages

version = '2.0'

setup(name='bda.cloud',
      version=version,
      description="",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url='http://svn.bluedynamics.net/svn/internal',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bda'],
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
