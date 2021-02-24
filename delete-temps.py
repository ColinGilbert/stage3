#!/usr/bin/env python3

import os

from tags import get_tags

tags = get_tags()

os.system('git checkout master')

for t in tags:
    os.system('git checkout ' + t)
    os.system('rm Dockerfile')
    os.system('rm Dockerfile.in')
    os.system('rm *~')
    os.system('rm .*.sw*')
    os.system('rm -rf __pycache__')
    os.system('git add . && git commit -m "Cleanup"')

os.system('git checkout master')
