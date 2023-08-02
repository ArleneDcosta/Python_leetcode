def solve(w):
    m=-1
    count=0
    for ele in w:
        if ele.isupper():
            if ele.lower() in w:
                count+=1
                m=max(m,count)
            else:
                count=0
        elif ele.islower():
            if ele.upper() in w:
                count+=1
                m=max(m,count)
            else:
                count=0
    if m<=1:
        return -1
    return m

print solve("azABaabza")
print solve("TacoCat")
print solve("AcZCbaBz")
print solve("abcdefghijklmnopqrstuvwxyz")
