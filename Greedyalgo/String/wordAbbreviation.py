from typing import List

def wordsAbbreviation(dict:List[str]) -> List[str]:
    def abbr(s,index = 0):
        if len(s) - index <= 3:
            return s
        return s[:index + 1] + str(len(s)-index-2) + s[-1]
    ans = []
    n = len(dict)
    prefix = [0] * n
    for word in dict:
        ans.append(abbr(word))
    #enumerate keeps the original array and not the changed value at the position in the list
    for i in range(n):
    #for i,word in enumerate(ans) :
       # print(i,word)
        while True:
            dup_list  = []
            for j in range(i+1,n):
                if ans[j] == ans[i]:
                    dup_list.append(j)
            if not dup_list:
                break

            dup_list.append(i)
            for k in dup_list:
                prefix[k] += 1
                ans[k] = abbr(dict[k],prefix[k])
    return ans

if __name__ == '__main__':
    print(wordsAbbreviation(['like','god','internal','me','internet','interval','intension','face','intrusion']))