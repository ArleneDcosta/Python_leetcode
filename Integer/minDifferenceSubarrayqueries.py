import sys
import time

def minDifference(nums,queries):
    start = time.time()
    maxNum = max(nums)
    n = len(nums)
    preSum = [[0] * (maxNum+1)]
    #print(preSum)

    for num in nums:
        currSum = preSum[-1][:]
        currSum[num] += 1
        preSum.append(currSum)
    #print(preSum)
    ans = []
    start = time.time()
    for l,r in queries:
        mmin = sys.maxsize
        pre = -1
        for num in range(1,maxNum + 1):
            #print((r+1,num),(l,num))
            cnt = preSum[r+1][num]  - preSum[l][num]
            #print(cnt,num)
            if(cnt > 0):
                if pre != -1:
                    mmin = min(mmin,num - pre)
                    #print('min',mmin)
                pre = num
        ans.append(mmin if mmin < sys.maxsize else -1 )
    end = time.time()
    print('*************',end - start)
    #return ans

def minDifference1(nums, queries) :
        start = time.time()
        result = []
        for l, r in queries:
            temp = sorted(list(set(nums[l:r + 1])))
            if len(temp) == 1:
                result.append(-1)
            else:
                minvalue = sys.maxsize
                for i in range(1, len(temp)):
                    minvalue = min(minvalue, abs(temp[i] - temp[i - 1]))
                result.append(minvalue)
        end = time.time()
        print('***********************',end - start)
        #return result
#print(minDifference([11,1,4,5,3,4],[[0,1],[1,3],[2,4]]))
#print(minDifference([12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,2,2,2,2],[[0,12],[2,3],[1,9],[0,17]]))
