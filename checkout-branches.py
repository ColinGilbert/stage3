#!/usr/bin/env python3

import os
import fileinput

from tags import get_tags

tags = get_tags()

os.system('git checkout master')
os.system('rm Dockerfile')

with open('Dockerfile.in') as infile:
   lines = infile.readlines()
   first_line = lines[0].strip()

for t in tags:
    os.system('git checkout -b ' + t)
    head_line = first_line + ":" + t + '\n'
    lines[0] = head_line
    with open('Dockerfile', 'w') as outfile:
        outfile.writelines(lines)
    os.system('rm -rf __pycache__ & rm Dockerfile.in')
    os.system('git add . && git commit  -m "' + t + '"')

os.system('git checkout master && rm Dockerfile')
