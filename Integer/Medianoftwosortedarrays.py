def findMedianSortedArrays(nums1, nums2):

    nums3 = nums1 + nums2
    nums3.sort()
    print(len(nums3)//2)
    print(nums3[len(nums3)//2]+nums3[(len(nums3)//2)-1])
    if len(nums3)%2 == 0:
        return ((nums3[len(nums3)//2]+nums3[(len(nums3)//2)-1])/2.0)
    else:
        return nums3[len(nums3)//2]

print findMedianSortedArrays([1,2],[3,4])
