class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

            if left == right:
                break
        
        return True