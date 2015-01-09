# Prints a list of (same length) lists as a nicely formatted table using tabs. Code code be simplified by using spaces
# instead, and made more robust by handling lists with different lengths. 
# Assumes tab length of 8 spaces and that all table entries are strings.
def p(t):print'\n'.join('\t'.join(v+'\t'*([max(map(len,c))for c in zip(*t)][i]/8-len(v)/8)for i,v in enumerate(r))for r in t)

# consider the following input
table = [
  ["Buck", "Rogers", "In Space"],
  ["Bugs", "Bunny", "A hole"],
  ["Victor", "Frankenstein", "Switzerland"]
]
# so p(table) Will produce something like
# Buck    Rogers        In Space
# Bugs    Bunny         A hole
# Victor  Frankenstein  Switzerland