from collections import defaultdict

def getMaxKnowledge(d,s,e,a,k):
    val = defaultdict(list)
    maxval = 0
    for i in range(1,d+1):
        for j in range(0,len(s)):
            if i in range(s[j],e[j]+1):
                val[i].append(a[j])
        val[i].sort(reverse=True)

    for ele in val:
        maxval = max(maxval,sum(val[ele][0:k+1]))
    return maxval


if __name__ == '__main__':
    print(getMaxKnowledge(10,[2,6,4,3],[8,9,7,5],[900,1600,2000,400],3))