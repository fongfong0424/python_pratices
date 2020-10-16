import os

with open('/Users/tess/Documents/KFS', 'r')as r:
    lines = r.readlines()

with open('/Users/tess/Documents/KFS', 'w')as w:
    for i in lines:
        w.write(i.replace("-", "_"))