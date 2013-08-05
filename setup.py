# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='lx.oju.skin',
      version=version,
      description="Tema Plone 4 OJU",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme skin',
      author='Lucas Aquino',
      author_email='contato@lucasaquino.com.br',
      url='http://www.lucasaquino.com.br',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lx', 'lx.oju'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
