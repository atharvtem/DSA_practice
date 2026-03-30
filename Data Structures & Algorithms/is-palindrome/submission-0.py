class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ", "")
        import string
        translator = str.maketrans('', '', string.punctuation)

        # Remove punctuation
        s = s.translate(translator)
        s=s.lower()
        print(s)
        left=0
        right = len(s)-1
        if len(s)<2:
            return True
        while(left<right):
            if s[left]==s[right]:
                left+=1
                right-=1
                continue
            else:
                return False
        return True
