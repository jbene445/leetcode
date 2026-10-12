class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(min(len(word1), len(word2))):
            merged = merged + word1[i] + word2[i] 
        merged = merged + word1[i + 1:] if len(word1) >= len(word2) else merged + word2[i + 1:]
        return merged
