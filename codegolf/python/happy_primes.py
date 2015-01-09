# Read one positive integer from stdin, then output 'happy' or 'sad' and then 'prime' or 'non-prime' depending on
# whether the number is 'happy' and 'prime' or not. For this problem a 'happy' number is a number if, by repeating the
# process of squaring each of the digits of the number and then summing the results to get a new value, eventually a 
# value of 1 can be reached. All non-happy numbers will eventually enter a loop.
# This solution: 198 characters
import sys
n=p=int(sys.stdin.next())
s={}
while n not in s:s[n]=1;n=sum(map(lambda x:int(x)**2, str(n)))
o='sad 'if n-1 else'happy '
if not all([p%i for i in range(2,p-1)]):o+='not '
print o+'prime'