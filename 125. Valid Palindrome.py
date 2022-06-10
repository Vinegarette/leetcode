class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        if len(s) < 1:
            return True
        
        # O(n): n/2 operations where n is length of word
        # Total operation is half of the length of 
        while l < r:
            
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
