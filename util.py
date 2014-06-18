# List files in directory
def ls(directory):
    from os import listdir
    from os.path import isfile, join
    return [ f for f in listdir(directory) if isfile(join(directory,f)) ]

# Return a number between 0 and highest
def rand(highest):
    import random
    return int(random.random()*(highest+1))

# Open path and return every line in a list
def load(path, minln, maxln):
    with open(path) as f:
        val = [x for x in f.readlines() if x.isalpha and len(x)>minln and len(x)<maxln]
    return val

# Prompt int error if not.
def promptint(message):
    return int(input(message))

# Prompt str error if not.
def promptstr(message):
    return str(input(message))
