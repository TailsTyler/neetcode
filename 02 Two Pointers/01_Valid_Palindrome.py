class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars_to_ignore = " !?.,\'\""
        allowed_chars = 'qwertyuioplkjhgfdsazxcvbnm'
        s = s.lower()
        while len(s) > 0:
            while not s[0].isalnum():
                print("removed ", s[0], " from front")
                s = s[1:]
                if len(s) == 0:
                    return True
            while not s[-1].isalnum():
                s = s[:-1]
                print("removed ", s[-1], " from back")
                if len(s) == 0:
                    return True
            if s[0] == s[-1]:
                print(s[0], " == ", s[-1])
                s = s[1:-1]  
                print("so s is now ", s)
            else:
                print(s[0], " != ", s[-1])
                return False
        return True      