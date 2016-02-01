"""
A Counter is a container that keeps track of how many times equivalent values are added.
It can be used to implement the same algorithms for which bag or multiset data structures
are commonly used in other languages.

Counter does not raise KeyError for unknown items.
If a value has not been seen in the input (as with e in this example), its count is 0.
"""

##### Initializing #######

import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)


##### Updating ########

import collections

c = collections.Counter()
print 'Initial :', c

c.update('abcdaab')
print 'Sequence:', c

c.update({'a':1, 'd':5})
print 'Dict    :', c


##### Accessing ########
"""
Once a Counter is populated, its values can be retrieved using the dictionary API.
"""

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])


##### elements() method ######

"""
The elements() method returns an iterator that produces all of the items known to the Counter.
"""
c = collections.Counter('extremely')
c['z'] = 0
print c
print list(c.elements())

##### most_common() method #######

"""
produce a sequence of the n most frequently encountered input values and their respective counts
"""

# Most Popular words in a file

import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)

##### Arithemetic #######

import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print 'C1:', c1
print 'C2:', c2

print '\nCombined counts:'
print c1 + c2

print '\nSubtraction:'
print c1 - c2

print '\nIntersection (taking positive minimums):'
print c1 & c2

print '\nUnion (taking maximums):'
print c1 | c2

