#!/usr/bin/env python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s.lower())
        sArr.sort()
        tArr = list(t.lower())
        tArr.sort()
        return sArr == tArr
