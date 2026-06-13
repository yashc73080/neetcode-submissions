class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()

        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0:
                    subAns = [nums[i], nums[left], nums[right]]
                    out.add(tuple(subAns))
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1

                elif currentSum < 0:
                    left += 1
                
                else:
                    right -= 1

        return [list(triplet) for triplet in out]