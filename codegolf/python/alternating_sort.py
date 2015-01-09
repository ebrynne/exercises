# Read a file called 'in.txt' that contains a space delimeted list of non-unique integers. Sort and print them such that
# the smallest number is the leftmost value printed, the second smallest is the rightmost value, the third smallest is
# the second leftmost and so on, so that the largest value (or two values in the case of an even number of values) are
# in the middle of the printed list.
# ex. 4 6 3 5 8 7 9 1 2 -> 1 3 5 7 9 8 6 4 2
# This solution: 83 Characters
x=sorted(open('in.txt').read().split(),key=int)
print' '.join(x[::2]+x[1::2][::-1])

# Some alternate solutions:
# 101 Characters
x=iter(sorted(open('in.txt').read().split(),key=int))
a=zip(*zip(x,x))
print' '.join(a[0]+a[1][::-1])

# 90 Characters (only works for even length lists)
x=sorted(open('in.txt').read().split(),key=int)
print' '.join(x[::2]+x[:(-len(x)%2)*2:-2])

# Scratch pad
# Alternate file reads
x=sorted(map(int,open('in.txt').read().split()))
x=sorted(open('in.txt').read().split(),key=int)

# A little python3 experimentation
[print(i,end=' ')for i in x[::2]+x[1::2][::-1]]