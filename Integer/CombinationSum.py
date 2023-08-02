def combinationSum(candidates,target):
    def func(nums,list1,target,sum1,index,greater,result):
        if sum1 == target:
            list2 = list1[:]
            if(list2 not in result):
                result.append(list2)
            return result,greater
        elif sum1 > target:
            greater = 1
            return result,greater
        for i in range(index,len(nums)):
            sum1 += nums[i]
            print(nums,list1+ [nums[i]],target,sum1,i,greater,result)
            result,greater = func(nums,list1+ [nums[i]],target,sum1,i,greater,result)
            sum1 -= nums[i]
            if greater!=0:
                greater = 0
                break
        return result,greater
            
    result = []
    greater = 1
    candidates.sort()
    sum1 = 0
    result,greater = func(candidates,[],target,sum1,0,greater,result)
    return result

print combinationSum([2,3,6,7],7)
