MAX_CHAR = [26]  
    
def minChanges(str): 
  
    n = len(str ) 
  
    # If length is more than maximum  
    # allowed characters, we cannot  
    # get the required string.  
    if (n > MAX_CHAR[0]):  
        return -1
  
    # Variable to store count of  
    # distinct characters  
    dist_count = 0
      
    # To store counts of different  
    # characters  
    count = [0] * MAX_CHAR[0]  
    rep=""
    for i in range(n):  
        if (count[ord(str[i]) - ord('a')] == 0) : 
            dist_count += 1
        else:
            if str[i] not in rep:
                rep+=str[i]
        count[(ord(str[i]) - ord('a'))] += 1
    if rep in str and (dist_count>len(rep) or dist_count==1):
        #print 'inside'
        dist_count-=1
    # Answer is, n - number of distinct char  
    return (n - dist_count)
def solution(s):
    ctr=1
    abc=set()
    for i in s:
        if i in abc:
            ctr=ctr+1
            abc.clear()
            abc.add(i)
        else:
            abc.add(i)
    return ctr
 
print minChanges("abacdec")
#print minChanges("abba")
#print minChanges("dddd")
print solution("world")
print minChanges("world")
