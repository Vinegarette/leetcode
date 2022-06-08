class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use tuples of sorted strings as dictionary keys
        
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
            
         
