#!/usr/bin/python
from util import rand, ls, load, promptint, promptstr
print("XKCD Password Generator.")
dicts = ls("/usr/share/dict")

print("{:d} files found in /usr/share/dict".format(len(dicts)))
print("Choose which one to use 0-{:d}".format(len(dicts)))
for i in range(len(dicts)):
    print(str(i) + ": "+dicts[i].split("/")[-1])

d  = load("/usr/share/dict/"+dicts[promptint("Choice (0-{:d}) :".format(len(dicts)))], 
        promptint("Minimum word length: "), 
        promptint("Maximum word length: "))

pw = ""
for i in range(promptint("Number of words: ")):
    pw = pw + d[rand(len(d))][:-1] + " "

print(pw)

