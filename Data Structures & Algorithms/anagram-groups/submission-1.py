class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupedDict = {}
        for i in strs:
            index = tuple(sorted(i))
            if index not in groupedDict:
                groupedDict[index] = []
            groupedDict[index].append(i)

        grouped = []
        for k, v in groupedDict.items():
            grouped.append(v)

        return grouped
