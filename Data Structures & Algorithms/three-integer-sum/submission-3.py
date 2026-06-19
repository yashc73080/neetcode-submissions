class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # a + b + c = 0 --> -a = b + c

        nums.sort()

        result = []

        for i in range(len(nums)):
            # Avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            complement = nums[i] * -1
            
            left, right = i + 1, len(nums) - 1
            while left < right:

                if nums[left] + nums[right] == complement:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Advance left and right to avoid duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif nums[left] + nums[right] < complement:
                    left += 1
                elif nums[left] + nums[right] > complement:
                    right -= 1
            
        return result