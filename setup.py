# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-gestion',
    version='1.0.0',
    description='Experiment based on django-oscar',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-gestio',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
#   package_data={'seoutils': [
#       'templates/*',
#       ]},
    install_requires = [
        'django>=1.5.4,<1.8',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
