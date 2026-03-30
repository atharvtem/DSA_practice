class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        ans = []
        for i in nums:
            if i not in res:
                res[i] =  nums.count(i)
            else:
                continue
        while k>0:
            maxkey = max(res, key=res.get)
            ans.append(maxkey)
            res.pop(maxkey)
            k-=1
        return ans