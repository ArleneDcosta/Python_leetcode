# Python3 program to find the lexicographically 
# smallest string by removing at most one character 

# Function to return the smallest string 
def smallest(s): 

    l = len(s)
    flag=0
    ans = "" 

    # iterate the string 
    for i in range(l): 

        # first point where s[i]>s[i+1]
        if (i<l-1):
            if (s[i] > s[i + 1]):
                flag=1
                continue
        else:
            if (flag!=1):
                return s[0: l - 1]
        ans+=s[i]
        


    return ans
   


s = "abcda"

print (smallest(s))
print (smallest("acb"))
print (smallest("hot"))
print (smallest("aaaa"))

# This code is contributed by ita_c 
