class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = nums.count(i)
            else:
                continue
        res = []
        for j in range(k):
            max_key = max(dict, key=dict.get)
            res.append(max_key)
            dict.pop(max_key)
        return res