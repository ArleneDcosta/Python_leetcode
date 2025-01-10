from typing import List

def findMaximalSweetness(sweetness : List[int],k : int) -> int :
    #Passing Sum to functions
    def getcutsCount(sweetness_sum):
        #Find min sum hence sweetness_sum = lowerbound
        cuts_count = 0
        cur_sweetness = 0
        for s in sweetness:
            cur_sweetness += s
            ##prev is greater or equal to hence the current value is considered to be a part of small
            if cur_sweetness >= sweetness_sum:
                cuts_count += 1
                cur_sweetness = 0
        return cuts_count

    left  = min(sweetness)
    right = sum(sweetness)
    print(right)

    while(left < right):
        mid = left + (right - left + 1) // 2
        cuts_count =  getcutsCount(mid)
        print(left,right,mid,cuts_count)
        #Find maximum min sweetness hence
        if cuts_count >= k+1:
            #MAXIMAL SWEETNESS hence + 1 inclined towards right[above function] [MIN of all total SUM] = left
            # Always check if 0 and 1 and mid is 1
            left = mid
        else:
            right = mid - 1

    return left
#maximul minimal sweetness
#maximul so will favour right element
if __name__ == '__main__':
    print(findMaximalSweetness([7,2,5,10,8],2))
    #print(findMaximalSweetness([1,2,3,4,5,6,7,8,9],5))