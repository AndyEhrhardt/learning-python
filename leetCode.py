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

# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortestString = 0
        for string in strs:
            if(len(string) > shortestString):
                shortestString = len(string)
        longestPrefix = ''
        for i in range(shortestString):
            subStrArr = []
            for checkString in strs:      
                subStrArr.append(checkString[:i + 1])          
            if (len(set(subStrArr)) == 1):
                longestPrefix = subStrArr[0]
            else:
                break
        return longestPrefix



# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace("{}", '')
        return len(s) == 0


# REVISIT THIS ONE I DO NOT UNDERSTAND 
# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            print(list1, list1.next)
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next
            
          


# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        placeHolder = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[placeHolder] = nums[i]
                placeHolder += 1
        return placeHolder

            

