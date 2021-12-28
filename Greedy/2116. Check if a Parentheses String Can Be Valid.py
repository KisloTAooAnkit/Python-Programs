class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        balance = 0
        n = len(s)
        if n%2 != 0:
            return False
            
        for i in range(n):
            if s[i] == "(" or locked[i] == "0":
                balance +=1
            
            elif s[i] == ")":
                balance -=1
            
            if balance <0:
                return False
        balance = 0
            
        for i in range(n-1,-1,-1):
            if s[i] == ")" or locked[i] == "0":
                balance +=1
            
            elif s[i] == "(":
                balance -=1
            
            if balance <0:
                return False
        return True