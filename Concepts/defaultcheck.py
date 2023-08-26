# from collections import defaultdict,Counter
#
# d = defaultdict(Counter)
#
# print(d['Arlene']['asa'])
#
# p = Counter()
# print(p['a'])

from collections import defaultdict

# Create a defaultdict of defaultdicts
v = defaultdict(lambda: defaultdict(int))

v = defaultdict(lambda: defaultdict(int))
# Increment counts in the nested defaultdict
v['A']['apple'] += 2
v['A']['banana'] += 3
v['B']['apple'] += 1
v['B']['orange'] += 4

print(v)
k = defaultdict()
print(k)

#enumerate should not be used when want to modify the list
'''
for i,l in enumerate(l):
    l[j] = val
    val will remain the same
'''