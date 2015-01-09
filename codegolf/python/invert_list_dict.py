# Just a compressed version of a function that take a dictionary that has iterables as its values and inverts it such that
# each item in each previous value points to the keys that pointed to the sequence that contained this item in the original
# dictionary.
def a(d):return{i:[k for k in d if i in d[k]]for v in d.values()for i in v}