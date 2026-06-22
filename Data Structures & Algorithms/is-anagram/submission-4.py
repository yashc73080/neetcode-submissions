class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # store letter counts in dict and compare counts afterwards

        smap = {}
        tmap = {}
        for char in s:
            smap[char] = smap.get(char, 0) + 1
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        
        if smap == tmap:
            return True
        
        return False