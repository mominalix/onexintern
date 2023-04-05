class Solution(object): # the main solution class
    def removeDuplicates(self, nums): # the removeDuplicates function
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)): # for loop which itterates with in list
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1