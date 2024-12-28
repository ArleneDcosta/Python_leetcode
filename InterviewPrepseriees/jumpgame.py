
def canJump(nums):
    last = len(nums) -1
    i=last -1
    while(i>= 0) :
        if i+nums [i] >= last:
            last = i
        i-=1
    return last == 0

if __name__ == '__main__':
    print(canJump([2,5,0,0]))

