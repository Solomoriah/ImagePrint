#!/usr/bin/env python
# Setup for ImagePrint
# Modified from samples by Alex Martelli.

from distutils.core import setup

longdesc  =  """
ImagePrint.py defines a class for generating images, using the same "printing"
interface as MSWinPrint.py.  Combined with MetaPrint.py, it can be used to
create print previews.

document is a class for creating and running print jobs.  Presently, the 
source is the only documentation for this class.

Development versions of this module may be found on **Github** at:

https://github.com/Solomoriah/ImagePrint
"""

setup(
    name = "ImagePrint",
    version = "1.0",
    description = "ImagePrint",
    long_description = longdesc,
    author = "Chris Gonnerman",
    author_email = "chris@gonnerman.org",
    py_modules = [ "ImagePrint" ],
    keywords = "windows printing",

    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Printing",
    ],
)

# end of file.
