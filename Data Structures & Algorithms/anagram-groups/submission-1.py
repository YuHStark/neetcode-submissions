class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for item in strs:
            sortedS = ''.join(sorted(item))
            result[sortedS].append(item)
        return list(result.values())




        