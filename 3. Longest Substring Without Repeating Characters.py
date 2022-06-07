class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # Hashmap/Dict to store all chars encountered
        # O(n)
        seen_before = {}
        max_length = 0
        start = 0
        
        # Iterate thru the string:
        
        for i, c in enumerate(s):
            # If already seen before
            # And not exceeding index of char
            if s[i] in seen_before and start <= seen_before[c]:
                # Iterate start by value of seen_before
                start = seen_before[c] + 1
            else:
                # Select which is larger
                # Current max length
                # Or idx - start + 1 
                max_length = max(max_length, i - start + 1)
                
        
            # Add index to seen_before
            
            seen_before[c] = i 
            
            
        return max_length
