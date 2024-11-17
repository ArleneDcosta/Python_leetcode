def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)
    imin, imax, half_len = 0, n, (n + m + 1) // 2
    print(f"imin {imin},imax {imax},half_len {half_len}")

    while imin <= imax:
        '''When i = 0 in the algorithm, it represents the situation where the partition in the first array (nums1) 
        is made at the very beginning of the array. 
        This means that no elements from nums1 are included in the left partition, 
        and all elements of the left partition must come from the second array (nums2). Let's break down the implications and how the algorithm handles this case.'''
        i = (imin + imax) // 2
        j = half_len - i  # To make sure there is a equal no of elements for [0:i] + [0:j] be in the first half of median
        print(i,j,(n+m) % 2)
        '''If any of the below conds are true the partition is not a valid partition'''
        if i < n and nums1[i] < nums2[j - 1]:
            # Increase i since all elements greater than or equal to i should be greater than elements j - 1
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # Decrease i[ i-1 is greater and should be reduced too right
            imax = i - 1
        else:
            # i is perfect (Above conditions are falsified abd thus it is a valid parition)
            '''
            i is the partition point in the smaller array (nums1), meaning all elements before i in nums1 go to the left partition,
             and all elements from i onward go to the right partition.
            j is the partition point in the larger array (nums2), meaning all elements before j in nums2 go to the left partition,
             and all elements from j onward go to the right partition.
            '''
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            '''IF odd numbers'''

            if (n + m) % 2 == 1:
                print("INISIDE")
                return max_of_left

            '''If even numbers in partition'''
            if i == n:
                min_of_right = nums2[j]
            elif j == m:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

if __name__ == '__main__':
    nums1 = [4,7]
    nums2 = [1,3,6]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
