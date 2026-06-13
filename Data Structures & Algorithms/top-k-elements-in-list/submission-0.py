class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        if len(set(nums)) <= k:
            out = list(set(nums))
            return out
        
        frequencies = {}
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)

        freqsList = list(frequencies.values())
        maxList = []
        while k > 0:
            maxList.append(max(freqsList))
            freqsList.remove(max(freqsList))
            k -= 1

        for k, v in frequencies.items():
            if v in maxList:
                out.append(k)

        return out
