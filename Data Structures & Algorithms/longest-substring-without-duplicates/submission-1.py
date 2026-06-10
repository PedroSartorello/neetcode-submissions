class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        janela = {} # char: indice
        maxLen = 0
        for right in range(len(s)):
            if s[right] in janela:
                if janela[s[right]] >= left:
                    left = janela[s[right]]+1
            janela[s[right]] = right
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
        
