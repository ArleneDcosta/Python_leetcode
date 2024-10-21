def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n, m = len(nums1), len(nums2)
    imin, imax, half_len = 0, n, (n + m + 1) // 2
    print(f"imin {imin},imax {imax},half_len {half_len}")

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        print(i,j,(n+m) % 2)
        '''If any of the below conds are true the partition is not a valid partition'''
        if i < n and nums1[i] < nums2[j - 1]:
            # Increase i
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # Decrease i
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
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
