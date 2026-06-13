class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ptr1 = 0
        ptr2 = 0
        counts = {}

        while ptr2 < len(s):
            counts[s[ptr2]] = counts.get(s[ptr2], 0) + 1

            max_freq = max(counts.values())
            not_matching = sum(counts.values()) - max_freq

            if not_matching <= k:
                max_len = sum(counts.values())
            elif not_matching > k:
                counts[s[ptr1]] -= 1
                ptr1 += 1

            ptr2 += 1

        return max(max_len, sum(counts.values()))