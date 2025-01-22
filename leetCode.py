#

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[x::-1]



# 13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        noMoreCombos = False
        for i, char in enumerate(s):
            if('CM' in s):
                s = s.replace('CM', '')
                total += 900
            elif('CD' in s):
                s = s.replace('CD', '')
                total += 400
            elif('XC' in s):
                s = s.replace('XC', '')
                total += 90
            elif('XL' in s):
                s = s.replace('XL', '')
                total += 40
            elif('IX' in s):
                s = s.replace('IX', '')
                total += 9
            elif('IV' in s):
                s = s.replace('IV', '')
                total += 4
            else: 
                break
        for i, char in enumerate(s):
            if (char == 'I'):
                total += 1
            elif (char == 'V'):
                total += 5
            elif (char == 'X'):
                total += 10
            elif (char == 'L'):
                total += 50
            elif (char == 'C'):
                total += 100
            elif (char == 'D'):
                total += 500
            elif (char == 'M'):
                total += 1000
        return total
