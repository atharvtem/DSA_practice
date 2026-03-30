class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            temp = s.count(i)
            s_dict[i]=temp

        t_dict = {}
        for j in t:
            temp = t.count(j)
            t_dict[j]=temp
        
        return s_dict == t_dict
