class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my_dict = {}
        for x in nums:
            my_dict[x] = 1
        R = 2 * (10 ** 5) + 10
        for i in range(1, R):
            if i in my_dict:
                continue
            else:
                return i
