class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for char in s:
            if sMap.get(char) is None:
                sMap[char] = 1
            else:
                sMap[char] += 1
        
        tMap = {}
        for char in t:
            if tMap.get(char) is None:
                tMap[char] = 1
            else:
                tMap[char] += 1

        if len(sMap.keys()) == len(tMap.keys()):
            for k, v in sMap.items():
                if tMap.get(k) != v or tMap.get(k) == 0:
                    return False
        else:
            return False

        return True