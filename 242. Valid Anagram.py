class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams contain the same amount of letters.
        # Could just sort and compare the two, which would be O(nlogn)
        # OR we could just do two scans, O(n)
        
        if len(s) != len(t):
            return False
        
        
        chars = [0 for _ in range(26)]
        
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            chars[ord('a') - ord(a)] += 1
            chars[ord('a') - ord(b)] -= 1
            
        for c in chars:
            if c != 0:
                return False
            
        return True
    
        '''
        mp = {}
        for i in range(len(s)):
            
            if s[i] in mp:
                mp[s[i]] += 1
            else:
                mp[s[i]] = 1
            
            if t[i] in mp:
                mp[t[i]] -= 1
            else:
                mp[t[i]] = -1
            
            
        for value in mp.values():
            if value != 0:
                return False
            
        return True
        '''
            
        
