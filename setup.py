#!/usr/bin/env python
# Copyright (C) 2015, Alibaba Cloud Computing

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
import mns.pkg_info

if sys.version_info <= (2, 5):
    sys.stderr.write("ERROR: mns python sdk requires Python Version 2.5 or above.\n")
    sys.stderr.write("Your Python version is %s.%s.%s.\n" % sys.version_info[:3])
    sys.exit(1)

setup( name = mns.pkg_info.name,
       version = mns.pkg_info.version,
       author = "Aliyun MNS",
       author_email = "",
       url = mns.pkg_info.url,
       packages = ["mns"],
       scripts = ["bin/mnscmd"],
       license = mns.pkg_info.license,
       description = mns.pkg_info.short_description,
       long_description = mns.pkg_info.long_description )
