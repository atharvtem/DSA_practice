class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        prodl, prodr = 1, 1
        pre = []
        post = []
        while l<len(nums):
            prodl = prodl * nums[l]
            pre.append(prodl)
            prodr = prodr * nums[r]
            post.append(prodr)
            l+=1
            r-=1
        post.reverse()
        ans = []
        for i in range(len(nums)):
            lp = pre[i-1] if i > 0 else 1
            rp = post[i+1] if i < len(nums)-1 else 1
            
            ans.append(lp * rp)
        return ans
