class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = 0
        for i in nums:
            temp = nums.count(i)
            if temp>1:
                return True
            else:
                continue

        return False;