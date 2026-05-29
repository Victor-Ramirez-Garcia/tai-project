from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Count available letter frequencies
        letter_counts = Counter(letters)
        
        # Precompute the word counts and their potential individual scores
        word_data = []
        for word in words:
            word_count = Counter(word)
            
            # Check if the word is even possible to form with total available letters
            possible = True
            word_score = 0
            for char, count in word_count.items():
                if count > letter_counts[char]:
                    possible = False
                    break
                word_score += score[ord(char) - ord('a')] * count
            
            if possible:
                word_data.append((word_count, word_score))
                
        num_words = len(word_data)
        self.max_score = 0
        
        # Backtracking function to explore subsets of valid words
        def backtrack(index: int, current_score: int, available_letters: Counter):
            # Update global maximum score found so far
            if current_score > self.max_score:
                self.max_score = current_score
                
            # Base case: explored all valid words
            if index == num_words:
                return
            
            # Option 1: Skip the current word
            backtrack(index + 1, current_score, available_letters)
            
            # Option 2: Try to include the current word
            word_count, word_score = word_data[index]
            can_form = True
            
            # Verify if the word can be formed with the CURRENT available letters
            for char, count in word_count.items():
                if available_letters[char] < count:
                    can_form = False
                    break
                    
            if can_form:
                # Deduct letters used by the current word
                for char, count in word_count.items():
                    available_letters[char] -= count
                    
                # Recurse with the word included
                backtrack(index + 1, current_score + word_score, available_letters)
                
                # Backtrack: restore the deducted letters
                for char, count in word_count.items():
                    available_letters[char] += count

        backtrack(0, 0, letter_counts)
        return self.max_score