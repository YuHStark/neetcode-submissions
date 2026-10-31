class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for n in nums:
                if n in used:
                    continue

                path.append(n)
                used.add(n)

                backtrack()

                path.pop()
                used.remove(n)

        backtrack()
        return res