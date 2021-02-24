#!/usr/bin/env python3

import os
import fileinput

from tags import get_tags

tags = get_tags()

code = os.system('git checkout master && rm Dockerfile')

with open('Dockerfile.in') as infile:
   lines = infile.readlines()
   first_line = lines[0].strip()

for t in tags:
    code = os.system('git checkout -b ' + t)
    head_line = first_line + ":" + t + '\n'
    lines[0] = head_line
    with open('Dockerfile', 'w') as outfile:
        outfile.writelines(lines)
    code = os.system('rm -rf __pycache__ & git add . && git commit  -m "' + t + '"')

code = os.system('git checkout master && rm Dockerfile')
