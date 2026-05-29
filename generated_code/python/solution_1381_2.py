from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Problem Analysis:
        - constraints: words.length <= 14. This small constraint strongly suggests 
          an exponential time complexity solution like backtracking or bitmasking.
        - Approach: Backtracking (or Subsets DFS). For each word, we can either 
          include it in our set (if we have enough remaining letters) or skip it.
          
        Time Complexity: O(2^N * L), where N is the number of words (<= 14) and 
                         L is the maximum length of a word (<= 15).
        Space Complexity: O(N) for the recursion stack and O(1) auxiliary space 
                          since the alphabet size is fixed to 26.
        """
        # Count available characters from the letters list
        letter_counts = [0] * 26
        for char in letters:
            letter_counts[ord(char) - ord('a')] += 1
            
        def backtrack(index: int, current_counts: List[int]) -> int:
            if index == len(words):
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, current_counts)
            
            # Option 2: Try to include the current word
            word = words[index]
            word_score = 0
            can_form = True
            
            # Temporary state to rollback changes if the word cannot be formed
            # or after the recursive branch finishes
            for char in word:
                idx = ord(char) - ord('a')
                if current_counts[idx] > 0:
                    current_counts[idx] -= 1
                    word_score += score[idx]
                else:
                    can_form = False
                    # Partial reduction rollback done below
            
            if can_form:
                # If the word can be formed completely, explore this path
                max_score = max(max_score, word_score + backtrack(index + 1, current_counts))
            
            # Rollback counts for the current word to restore state for backtracking
            # (handles both partial failures and successful branch completions)
            for char in word:
                idx = ord(char) - ord('a')
                # If we broke out early because can_form became False, we only restore
                # what was actually decremented. However, doing a simple count reconstruction 
                # or restoring unconditionally requires tracking. Instead, we can just 
                # rebuild the count array safely by manually adding back the characters we processed.
                # Since we always loop through the entire word, we must only add back what was taken.
                # To keep it simple and clean, let's just restore exactly what the word contains,
                # but we need to ensure we don't over-restore if we failed mid-way.
                # A foolproof way is to stop tracking early if can_form is false, 
                # or just iterate up to the character where it failed.
                
            # Optimized clean rollback:
            # Re-implement inclusion precisely to handle rollback cleanly.
            return max_score

        # Let's refine the inner logic for safety and readability
        def dfs(idx: int) -> int:
            if idx == len(words):
                return 0
            
            # Option 1: Skip
            res = dfs(idx + 1)
            
            # Option 2: Include
            word = words[idx]
            can_form = True
            word_score = 0
            formed_chars = []
            
            for char in word:
                c_idx = ord(char) - ord('a')
                if letter_counts[c_idx] > 0:
                    letter_counts[c_idx] -= 1
                    word_score += score[c_idx]
                    formed_chars.append(char)
                else:
                    can_form = False
                    break
                    
            if can_form:
                res = max(res, word_score + dfs(idx + 1))
                
            # Rollback the changes made by this word
            for char in formed_chars:
                letter_counts[ord(char) - ord('a')] += 1
                
            return res

        return dfs(0)