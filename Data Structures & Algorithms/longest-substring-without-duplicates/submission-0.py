class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr1, ptr2 = 0, 0
        chars = set()
        max_len = 0

        while ptr2 < len(s):
            if s[ptr2] not in chars:
                chars.add(s[ptr2])
                ptr2 += 1
                max_len = max(max_len, len(chars))
            else:
                chars.remove(s[ptr1])
                ptr1 += 1

        return max_len