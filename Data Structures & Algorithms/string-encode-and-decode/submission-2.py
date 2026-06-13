class Solution:
    def encode(self, strs: List[str]) -> str:

        solution = ""
        for word in strs:
            solution += str(len(word))
            solution += "#"
            solution += word

        print(solution)

        return solution

    def decode(self, s: str) -> List[str]:
        
        solution = []
        count = ""

        i = 0
        while i < len(s):
            if s[i] != "#":
                count += s[i]
                i += 1

            elif s[i] == "#":
                count = int(count)
                i += 1
                splice = s[i:i+count]
                print(splice)
                solution.append(splice)
                i += count
                count = ""

        print(solution)

        return solution
