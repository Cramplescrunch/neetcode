#!/usr/bin/env python3

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s.lower())
        sArr.sort()
        tArr = list(t.lower())
        tArr.sort()
        return sArr == tArr

