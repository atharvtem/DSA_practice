class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            temp = 0
            while i:
                temp += i%2
                i = i >> 1
            res.append(temp)
        return res