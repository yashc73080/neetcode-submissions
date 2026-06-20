class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0

        # store frequencies of cumulative sums
        totals = {0: 1}
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            # current_sum - old_sum = k -> old_sum = current_sum - k
            if current_sum - k in totals.keys():
                count += totals[current_sum - k]

            totals[current_sum] = totals.get(current_sum, 0) + 1

        return count