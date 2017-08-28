#!/usr/bin/env python
# Encoding: utf-8
# See: <http://docs.python.org/distutils/introduction.html>
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("src/cuisine.py") as f:
    fff = f.readlines()
    VERSION = list(filter(lambda _:_.startswith("VERSION"),
                          fff))[0].split("=")[1].strip().strip('"')

setup(
    name             = "cuisine",
    version          = VERSION,
    description      = "Chef-like functionality for Fabric",
    author           = "Sébastien Pierre",
    author_email     = "sebastien.pierre@gmail.com",
    url              = "http://github.com/sebastien/cuisine",
    download_url     = "https://github.com/sebastien/cuisine/tarball/%s" % (VERSION),
    keywords         = ["fabric", "chef", "ssh",],
    install_requires = ["fabric3", "six"],
    package_dir      = {"":"src"},
    py_modules       = ["cuisine"],
    license          = "License :: OSI Approved :: BSD License",
    classifiers      = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
)
# EOF - vim: ts=4 sw=4 noet
