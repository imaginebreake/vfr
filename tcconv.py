#!/usr/bin/env python3.1

from sys import argv
try:
    from vfr import parse_tc
except ImportError:
    exit("tcconv requires vfr.py in order to work")

if len(argv) == 4:
    fps = argv[1]
    tc = argv[2]
    frames = int(argv[3])
    parse_tc(fps, frames, tc)
else:
    exit("tcconv.py <fps/v1 timecodes> <output v2 timecodes> <frames>")