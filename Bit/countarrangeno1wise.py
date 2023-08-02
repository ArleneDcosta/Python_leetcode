def getCount(no):
    count = 0
    while(no):
        if(no & 1):
            count+=1
        no = no >> 1

    return count

def getsortedlist(l):
    countarr = []
    resultarr = []
    for ele in l:
        countarr.append([getCount(ele),ele])
    countarr.sort(key = lambda x : (x[0],x[1]))
    for ele in countarr:
        resultarr.append(ele[1])
    return resultarr

if __name__ == '__main__':
    print(getCount(15))
    print(getsortedlist([15,7,2,3,1]))