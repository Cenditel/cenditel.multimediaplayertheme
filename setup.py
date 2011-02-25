from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='cenditel.multimediaplayertheme',
      version=version,
      description="It is a Content Type specific theme for html5 audio and video player of cenditel multimedia Plone products",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='plone, product, content type, audio, video, html5',
      author='Victor Terán',
      author_email='elalcon89@gmail.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://svn.plone.org/svn/collective/cenditel.multimediaplayertheme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cenditel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'cenditel.audio',
          'cenditel.video',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
