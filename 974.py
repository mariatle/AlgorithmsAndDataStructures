class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] += prefix_sum[i - 1] + nums[i - 1]
        my_dict = {}
        ans = 0
        for i in range(n + 1):
            prefix_sum[i] = (prefix_sum[i] + k) % k
            if prefix_sum[i] in my_dict:
                ans += my_dict[prefix_sum[i]] 
            



            if prefix_sum[i] in my_dict:
                my_dict[prefix_sum[i]] += 1
            else: 
                my_dict[prefix_sum[i]] = 1
        
        return ans
