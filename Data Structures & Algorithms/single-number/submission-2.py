class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visit = set()
        for num in nums:
            if num in visit:
                visit.remove(num)
            else:
                visit.add(num)
        return visit.pop()
            