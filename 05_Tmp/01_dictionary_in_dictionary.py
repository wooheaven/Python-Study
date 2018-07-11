from collections import defaultdict

d = defaultdict(lambda: defaultdict(int))
d[0][0] = 1.0
d[0][1] = 2
d[0][2] = 'Name'
print(d)

# defaultdict(<function <lambda> at 0x7f596b1d60d0>, {0: defaultdict(<class 'int'>, {0: 1.0, 1: 2, 2: 'Name'})})

