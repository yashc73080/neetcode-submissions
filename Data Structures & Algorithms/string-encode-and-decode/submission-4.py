class Solution:
    def encode(self, strs: List[str]) -> str:

        solution = ""

        # iterate through all words 
        for word in strs:
            solution += str(len(word))
            solution += "#" # separator 
            solution += word

        return solution

    def decode(self, s: str) -> List[str]:
        
        solution = []
        count = ""

        # while loop to go through encoded string
        i = 0
        while i < len(s):
            # it will always start with the length number, so if its not '#', count it
            if s[i] != "#":
                count += s[i]
                i += 1

            # reached a '#' -> the word starts next
            elif s[i] == "#":
                # convert string count to int and move forward
                count = int(count) 
                i += 1

                # get only the relevant word
                splice = s[i:i+count]
                solution.append(splice)

                # move i forward and reset count
                i += count
                count = ""

        return solution
