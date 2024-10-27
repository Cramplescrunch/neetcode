#!/usr/bin/env python3

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j, k = 0, len(s) - 1
        while j <= k:
            if not s[j].isalnum():
                j += 1
            elif not s[k].isalnum():
                k -= 1
            elif s[j].lower() == s[k].lower():
                j += 1
                k -= 1
            else:
                return False
        return True

Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama")
Solution.isPalindrome(Solution, "race a car")
Solution.isPalindrome(Solution, " ")
