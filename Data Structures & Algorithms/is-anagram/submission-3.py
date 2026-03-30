class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s)!=len(t):
            return False
        for i in s:
            temp = s.count(i)
            s_dict[i]=temp
            temp = t.count(i)
            t_dict[i]=temp

        
        return s_dict == t_dict
