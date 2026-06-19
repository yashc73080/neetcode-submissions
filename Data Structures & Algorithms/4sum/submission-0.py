class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Fix one number, and do three sum
        # that is, fix one number, then fix another number, then do two sum with 2 pointers
        # handle duplicates by sorting and advancing pointers if same as previous

        result = []
        nums.sort()

        # Fix the first number (a)
        for i in range(len(nums)):
            # a + b + c + d = target -> b + c + d = target - a = complement
            complement = target - nums[i]

            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Fix the second number (b)
            for j in range(i+1, len(nums)):
                # b + c + d = complement -> c + d = complement - b = sub_complement
                sub_complement = complement - nums[j]

                # Skip duplicates again
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1 # c
                right = len(nums) - 1 # d
                while left < right:

                    # Correct value
                    if nums[left] + nums[right] == sub_complement:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Advance from duplicates
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        
                    # Too small
                    elif nums[left] + nums[right] < sub_complement:
                        left += 1 
                    
                    # Too big
                    elif nums[left] + nums[right] > sub_complement:
                        right -= 1
        
        return result