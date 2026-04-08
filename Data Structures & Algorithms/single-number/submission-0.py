class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = Counter(nums)
        for key,value in map.items():
            if value<2:
                return key