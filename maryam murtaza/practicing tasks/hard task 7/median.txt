class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
            list=nums1+nums2
            list.sort()
            length=len(list)
            if length%2==0:
                value1=length/2
                value2=value1-1
                mid=list[value1]+list[value2]
                median=mid/2.0
                return median
            else:
                midvalue=list[length/2]
                return midvalue
nums1=[1,3]
nums2=[2]
x=Solution()
x.findMedianSortedArrays(nums1,nums2)