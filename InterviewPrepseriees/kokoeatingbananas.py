

def minEatingSpeed(piles, h):
    def helper(bph):
        res = 0
        for ele in piles:
            if ele == bph:
                res += 1
            else:
                if ele % bph == 0:
                    res += int(ele / bph)
                else:
                    res += int(ele / bph) + 1

        if res <= h:
            return True
        return False

    left = min(piles)
    right = max(piles)
    while(left < right):
        mid = left + (right - left) // 2
        if helper(mid):
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == '__main__':
    print(minEatingSpeed(piles = [3,6,7,11], h = 8))
    print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))