#!/usr/bin/env python3

import os
import fileinput

from tags import get_tags

tags = get_tags()

os.system('git checkout master')
for t in tags:
    os.system('git checkout ' + t)
    with open('Dockerfile.in') as infile:
        lines = infile.readlines()
    head_line = lines[0].strip() + ":" + t + '\n'
    lines[0] = head_line
    os.system('rm Dockerfile')
    with open('Dockerfile', 'w') as outfile:
        outfile.writelines(lines)
    os.system('git add .')
    os.system('git commit -m "' + t + '"')

os.system('git checkout master')
