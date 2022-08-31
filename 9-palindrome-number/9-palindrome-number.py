class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x): return False
        x = str(x)
        st, ed = 0, len(x)-1

        while st < ed:
            if x[st] != x[ed]:
                return False
            st += 1
            ed -=1
        return True
