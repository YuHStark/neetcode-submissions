class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store=defaultdict(int)
        for item in nums:
            store[item] +=1
        
        bucket = [[] for i in range(len(nums)+1)]
        for num,freq in store.items():
            bucket[freq].append(num)
        
        result = []
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result


        