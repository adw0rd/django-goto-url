from setuptools import setup, find_packages
from goto_url import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
finally:
    readme.close()

setup(
    name='django-goto-url',
    version=__version__,
    description="Wraps external links in base64 and relocate on the special View, later redirect to source URL",
    long_description=long_description,
    keywords='django, goto, url, redirect, relocation',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/django-goto-url',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', ],
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
