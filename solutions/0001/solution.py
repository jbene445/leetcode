class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target - num]]
            seen[num] = i
        return []
