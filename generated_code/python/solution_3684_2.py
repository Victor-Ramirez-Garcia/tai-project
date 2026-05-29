class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Since p contains exactly one '*', we can split it into a prefix and a suffix.
        # The '*' can match any sequence of zero or more characters.
        # Thus, p can match a substring of s if and only if we can find the prefix in s,
        # and then find the suffix in the remaining part of s after the prefix's match.
        prefix, suffix = p.split('*')
        
        # Find the first occurrence of the prefix in s
        prefix_idx = s.find(prefix)
        if prefix_idx == -1:
            return False
            
        # Find the suffix in the portion of s that comes after the end of the matched prefix
        # s.find(suffix, start_pos) searches for suffix starting from index start_pos
        suffix_idx = s.find(suffix, prefix_idx + len(prefix))
        
        return suffix_idx != -1