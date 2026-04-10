class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        k = 0
        j = 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        n = len(nums)
        while n > 0:
            if nums[k] != 0:
                temp=nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                j+=1
            k+=1
            n-=1
        return  nums