class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_num= nums1+nums2
        new_num.sort()
        median=float('inf')
        
        if len(new_num)%2==0:
            median = (new_num[(len(new_num)//2)-1] +new_num[(len(new_num)//2)])/2
        else: median=new_num[(len(new_num)//2)]


        return median