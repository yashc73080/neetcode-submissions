class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        solution = ""
        for i in range(len(reference)):

            for word in strs[1:]:
                if i >= len(word):
                    return solution
                if reference[i] != word[i]:
                    return solution
                
            solution += reference[i]

        return solution