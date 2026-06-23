class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        counts = {}
        max_substring = 0

        left = 0
        right = 1

        counts[s[left]] = 1

        while right < len(s):
            freq = counts.get(s[right], 0)
            if freq == 0:
                counts[s[right]] = 1
                max_substring = max(max_substring, right - left + 1)
                right += 1
            else:
                counts[s[left]] = 0
                left += 1
        
        return max_substring
            