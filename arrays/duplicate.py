#!/usr/bin/env python3
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx-1] == num:
                return True
        return False

