class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        my_dict = {}
        sum = 0
        for i in range(k):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            sum += nums[i]
        ans = 0
        if len(my_dict) >= m:
            ans = sum
        
        for i in range(k, len(nums)):
            #delete i-k (nums[i-k])
            my_dict[nums[i - k]] -= 1
            sum -= nums[i - k]
            if my_dict[nums[i - k]] == 0:
                del my_dict[nums[i-k]]

            #add nums[i]
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            
            sum += nums[i]
            if len(my_dict) >= m:
                ans = max(ans, sum)
        return ans
