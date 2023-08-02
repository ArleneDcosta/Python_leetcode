import itertools
A='abc'
B='bca'
for a,b in itertools.izip(A, B):
    print a,b
