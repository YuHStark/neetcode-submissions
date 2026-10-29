class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        result=nums[0]
        for item in range(1,len(nums)):
            current=max(nums[item],current+nums[item])
            result=max(current,result)
        return result



        