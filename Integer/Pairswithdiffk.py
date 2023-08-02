def pairs(l,k):
    s = list(set(l))
    s.sort()
    left = 0
    right = len(s)-1
    while(left < right and right < len(s)):
        if(abs(s[right]-s[left]))>3:
            right-=1
        elif(abs(s[right]-s[left]))<3:
            right+=1
        if(right < len(s) and left < right and abs(s[right]-s[left]))==3:
            print(s[left],s[right])
        left+=1
            
    
pairs([1,5,2,2,2,5,5,4],3)
