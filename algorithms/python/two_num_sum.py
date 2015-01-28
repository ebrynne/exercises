# Most basic two number sum solution
class TwoNumSumNaive(object):
  def __init__(self):
    self.numbers = []

  # Just append each inserted number to an unsorted list.
  # O(1)
  def insert(self, num):
    self.numbers.append(num)

  # Iterate over the list once and for each items iterate over the list again
  # from the next item forward and check if each pair sums to the requireed
  # value
  # O(n^2)
  def check(self, num):
    for index, n in enumerate(self.numbers):
      for n2 in self.numbers[index+1:]:
        if n + n2 == num:
          return True
    return False


# One of my favourite solutions, uses a dictionary to store all inserted values
# and the nuber of times they have been inserted.
class TwoNumSumMap(object):
  def __init__(self):
    self.numbers = {}

  # Either create an entry in the dictionary mapping the value to 1 or, if the
  # value is already a key in the dict, increment the associated value
  def insert(self, num):
    if num in self.numbers:
      self.numbers[num] += 1
    else:
      self.numbers[num] = 1

  # For each key in the dictionary, subtract that value from the requested
  # sum and check if it's in the map. If it is, make sure that the associated
  # count of occurences is >2 if the current key is exactly half the requested
  # sum (because we'll need to have inserted the same number twice to complete
  # the sum), otherwise the number of occurences just has to be 1
  def check(self, num):
    for n in self.numbers.keys():
      diff = num - n
      threshold = 2 if diff == n else 1
      if diff in self.numbers and self.numbers[diff] >= threshold:
        return True
    return False

# Maintains a set of all possible sums of the numbers inserted so far. Optimizes
# heavily in favour of the check method, at the expense of using O(n^2) memory
class TwoNumSumSet(object):
  def __init__(self):
    self.numbers = []
    self.sums = set()

  # Calculate the sum of the inserted number with every other previously
  # inserted number and add it to a set, then add the number to the internal
  # list of numbers
  # O(n)
  def insert(self, num):
    for n in self.numbers:
      self.sums.add(n + num)
    self.numbers.append(num)

  # Just check whether or not the provided value is in our set of sums
  def check(self, num):
    return num in self.sums

# This is more complicated than it needs to be, as I've implemented a binary
# search algorithm for illustrative purposes. Normally I'd suggest using the
# bisect module (as I do below). It's also less efficient than it looks because
# of all the list manipulation. But the point is to illustrate the concept
# rather than making things even more complicated with optimizations.
# This solution maintains a sorted list of values then, when checking, it checks
# the difference between each value and then does a binary search for that
# difference in the list
class TwoNumSumBinary(object):
  def __init__(self):
    self.numbers = []

  # A convenience method for getting the maximum index of the list
  def max_index(self):
    return max(len(self.numbers) - 1, 0)

  # Retrieve the insertion index using the binary search method, then insert the
  # new value at that index, maintaining the sort order.
  # O(log(n))
  def insert(self, num):
    if not self.numbers:
      self.numbers.append(num)
    else:
      insertion_index = self.binary_search(0, self.max_index(), num)
      print insertion_index
      if insertion_index == -1:
        self.numbers.append(num)
      else:
        self.numbers.insert(insertion_index, num)

  # Get the difference between each number and the requested value and then do a
  # binary search for the difference in the list. 
  # O(nlog(n))

  def check(self, num):
    for n in self.numbers:
      diff = num - n
      temp = self.binary_search(0, self.max_index(), diff)
      print "Searched: %s -- %s -- %s" % (diff, temp, self.numbers[temp])
      index = self.binary_search(0, self.max_index(), diff)
      # If the the other component of the sum is found and is a different value
      # than the first half OR if the two components are the same value, check
      # that there are at least two by checking the values to the left and right
      if self.numbers[index] == diff and (diff != n or (diff == n and
          (index - 1 >= 0 and self.numbers[index - 1] == n)
          (index + 1 <= self.max_index() and self.numbers[index + 1] == n))):
        return True
    return False

  # Slightly modified binary search - returns a list index that
  # represents either where the element is, or the index of the
  # element to the right of where the supplied value would be
  # inserted. In cases where the value is greater than any value
  # in the list, returns -1
  # O(log(n))
  def binary_search(self, start, end, val):
    print self.numbers, start, end, val
    if end - start <= 1:
      if val <= self.numbers[start]:
        return start
      elif val <= self.numbers[end]:
        return end
      else:
        return -1
    midpoint = (start + end) / 2
    if self.numbers[midpoint] == val:
      return midpoint
    elif val > self.numbers[midpoint]:
      return self.binary_search(midpoint, end, val)
    else:
      return self.binary_search(start, midpoint, val)

# Rather than using my own binary search, let's just use bisect to maintain the
# ordered list as we insert. Then we use a neat little trick using pointers to
# check for the sum in the sorted list.
import bisect
class TwoNumSumPointers(object):
  def __init__(self):
    self.numbers = []

  # Insert the value into the list while mainting sorted order
  # O(log(n))
  def insert(self, num):
    bisect.insort(self.numbers, num)

  # When checking whether we can sum to a value, v, start by looking at the
  # smallest and largest values. If the sum of these two is less than v try
  # again with the second smallest value summed with the largest, or if the sum
  # is greater than v, try again with the smallest value and the second largest.
  # Repeat this process until either the two examined values sum to v, or until
  # both the left and right pointers point at the same number (meaning we
  # couldn't find the sum)
  # O(n)
  def check(self, num):
    left = 0
    right = len(self.numbers) - 1
    while left < right:
      sum = self.numbers[left] + self.numbers[right]
      if sum == num:
        return True
      elif sum < num:
        left += 1
      else:
        right -= 1
    return False