#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as file:
    c_code_lines = file.read().split("\n")
    c_code_lines = map(str.strip, c_code_lines)
    c_code_lines = filter(lambda s: s, c_code_lines)
    c_code_lines = map(lambda s: s.replace("\\", "\\\\"), c_code_lines)
    c_code_lines = map(lambda s: s.replace("\"", "\\\""), c_code_lines)
    c_code_lines = map(lambda s: s.replace("\'", "\\\'"), c_code_lines)
    c_code_lines = map(lambda s: s + '\\', c_code_lines)

print("\n".join(c_code_lines))
    
    
