import collections

# Add to the right
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])

d.remove(d[0])
print('remove(d[0]):', d)







import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Right end:', d[-1])

d.remove(d[-1])
print('remove(d[-1]):', d)
