#!/usr/bin/python
from util import rand, ls, load 

d  = load("/usr/share/dict/cracklib-small")
pw = ""
for i in range(4):
    pw = pw + d[rand(len(d))][:-1] + " "

print(pw)

