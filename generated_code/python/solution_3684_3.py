from typing import List

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Since p contains exactly one '*', we can split p into a prefix and a suffix
        prefix, suffix = p.split('*')
        
        # Find the first occurrence of the prefix in s
        prefix_idx = s.find(prefix)
        if prefix_idx == -1:
            return False
            
        # The suffix must appear in the remaining part of s after the prefix ends
        # prefix_idx + len(prefix) ensures that the prefix and suffix do not overlap
        suffix_idx = s.find(suffix, prefix_idx + len(prefix))
        
        return suffix_idx != -1