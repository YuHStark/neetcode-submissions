class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for item in nums:
            if item in result:
                return True;
            else:
                result.add(item)
        return False
        