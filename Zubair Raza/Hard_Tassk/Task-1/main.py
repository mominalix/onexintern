def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.
    """
    # Merge the two arrays and sort them
    nums = sorted(nums1 + nums2)
    
    # Get the length of the merged array
    n = len(nums)
    
    # If the length is odd, return the middle element
    if n % 2 == 1:
        return nums[n // 2]
    
    # If the length is even, return the average of the middle two elements
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
find_median_sorted_arrays([1, 3], [2])
find_median_sorted_arrays([1, 2], [3, 4])
find_median_sorted_arrays([0, 0], [0, 0])
find_median_sorted_arrays([], [1])
find_median_sorted_arrays([2], [])

