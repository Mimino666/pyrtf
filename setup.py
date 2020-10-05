from __future__ import absolute_import, unicode_literals, division, print_function

from distutils.core import setup

setup(
    name='PyRTF',
    version='0.45',
    author='Simon Cusack',
    author_email='scusack@sourceforge.net',
    url='http://pyrtf.sourceforge.net/',
    license='http://www.gnu.org/licenses/gpl.html',
    platforms=['Any'],
    description='PyRTF - Rich Text Format Document Generation',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
    long_description='''PyRTF is a pure python module for the efficient generation of rich text format
documents. Supports styles, tables, cell merging, jpg and png images and tries
to maintain compatibility with as many RTF readers as possible.''',
    keywords=(
        'RTF',
        'Rich Text',
        'Rich Text Format',
        'documentation',
        'reports'),
    packages=['PyRTF'],
    package_dir={'': '.'},
    install_requires=['six'],
)
