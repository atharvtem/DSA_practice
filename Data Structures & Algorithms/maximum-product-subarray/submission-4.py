class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for i in nums:
            temp = currMax * i
            currMax = max(currMax*i, currMin*i, i)
            currMin = min(temp, currMin*i, i)
            res = max(res,currMax)
        return res