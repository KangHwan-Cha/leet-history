class Solution:
    def romanToInt(self, s: str) -> int:
            # I             1
            # V             5
            # X             10
            # L             50
            # C             100
            # D             500
            # M             1000
        s = s.upper()
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        num = roman_map[s[-1]]
        for i in range(len(s)-2, -1, -1):
            # if not i in roman_map:
            #     return 0
            if roman_map[s[i]] >= roman_map[s[i+1]]:
                num += roman_map[s[i]]
            else:
                num -= roman_map[s[i]]

        return num
        