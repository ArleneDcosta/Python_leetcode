class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

        
class Solution:
    def largestNumber(self,nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        print(sorted(map(str, nums), key=LargerNumKey))
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
    
   

s = Solution()
print(s.largestNumber([3,30,34,5,9]))
