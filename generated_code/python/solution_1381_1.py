from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Count available letter frequencies
        avail_counts = [0] * 26
        for char in letters:
            avail_counts[ord(char) - ord('a')] += 1
            
        # Precompute the score and letter counts for each word.
        # If a word requires more letters than available in total, it cannot be formed.
        word_data = []
        for word in words:
            word_counts = [0] * 26
            word_score = 0
            possible = True
            for char in word:
                idx = ord(char) - ord('a')
                word_counts[idx] += 1
                word_score += score[idx]
                if word_counts[idx] > avail_counts[idx]:
                    possible = False
            if possible:
                word_data.append((word_counts, word_score))
                
        # Since words.length <= 14, we can use backtracking to explore all combinations.
        # Time Complexity: O(2^N * 26) where N is the number of valid words (N <= 14).
        # Space Complexity: O(N) for the recursion stack.
        self.max_score = 0
        n = len(word_data)
        
        def backtrack(index: int, current_score: int) -> None:
            if current_score > self.max_score:
                self.max_score = current_score
                
            if index == n:
                return
                
            # Option 1: Skip the current word
            backtrack(index + 1, current_score)
            
            # Option 2: Try to include the current word
            word_counts, word_score = word_data[index]
            can_form = True
            
            # Check if we have enough letters left
            for i in range(26):
                if avail_counts[i] < word_counts[i]:
                    can_form = False
                    break
                    
            if can_form:
                # Deduct letters used by the current word
                for i in range(26):
                    avail_counts[i] -= word_counts[i]
                    
                # Recurse with the word included
                backtrack(index + 1, current_score + word_score)
                
                # Backtrack: Restore letter counts
                for i in range(26):
                    avail_counts[i] += word_counts[i]

        backtrack(0, 0)
        return self.max_score