import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), errors='replace') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-persiandate-widget',
    version='1.0b1',
    keywords='widgets persian',
    packages=['persiandate'],
    install_requires=['django'],
    include_package_data=True,
    license='BSD 3-Clause License', 
    description='ویدجتی برای نمایش تاریخ به فرمت جلالی به همراه یک تقویم برای ورود آسان داده',
    long_description=README,
    url='http://www.example.com/',
    author='Your Name',
    author_email='lkn2993@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
    ],
)

