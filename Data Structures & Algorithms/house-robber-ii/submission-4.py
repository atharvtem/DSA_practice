class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        rob1, rob2 = 0, 0
        for n in nums[:-1]:
            temp1 = max(rob1+n,rob2)
            rob1 = rob2
            rob2=temp1
        rob3, rob4 = 0, 0
        for n in nums[1:]:
            temp2 = max(rob3+n,rob4)
            rob3=rob4
            rob4=temp2
        return max(rob2,rob4)