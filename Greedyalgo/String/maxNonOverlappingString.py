from typing import List
from collections import defaultdict

#All the letters should be contained between 2 letters and not half inside and half outside
def maxNumOfSubstrings(s: str) -> List[str]:
    letter_range = defaultdict(list)

    for i,c in enumerate(s):
        if c not in letter_range:
            letter_range[c].extend([i,i])
        else:
            letter_range[c][1] = i

    print(letter_range)
    #Try to expand the range for each letter
    for key in letter_range:
        start,end = letter_range[key]
        stack = [(start,end)]
        while stack:
            curr_s,curr_e = stack.pop()
            print(curr_s,curr_e,key)
            for i in range(curr_s,curr_e):
                new_s,new_e = letter_range[s[i]]
                print(new_s,new_e,key,s[i])
                #check if a current letter lies in the given range then update it to the outer range
                if new_s < start:
                    stack.append((new_s,start-1))
                    #element is aldready covered
                    start = new_s

                if new_e > end:
                    stack.append((end+1,new_e))
                    end = new_e
            letter_range[key] = [start,end]

    sorted_ranges = sorted(letter_range.values(),key= lambda x:x[1] - x[0])
    #print(sorted_ranges)
    # s1 ............ e1
    #        start...........end
    seen_ranges = []
    ans = []
    for start,end in sorted_ranges:
        if any( end >= s1 and e1 >= start for s1,e1 in seen_ranges):
            continue
        seen_ranges.append((start,end))
        ans.append(s[start:end+1])
    return ans

if __name__ == '__main__':
    #print(maxNumOfSubstrings("adefaddaccc"))
    print(maxNumOfSubstrings("adefaddadfccc"))
    # print(maxNumOfSubstrings("abbaccd"))