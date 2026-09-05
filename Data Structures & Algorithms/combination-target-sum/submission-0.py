class Solution:
    def combinationSum(self, nums, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])

                # i (not i + 1) because we can reuse the same number
                backtrack(i, current, total + nums[i])

                current.pop()

        backtrack(0, [], 0)
        return result