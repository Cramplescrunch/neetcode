#!/usr/bin/env python3

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print (nums[i] + nums[j])
                if (nums[i] + nums[j] == target) and (j>i):
                    return [i, j]

Solution.twoSum(Solution, [0,4,3,0], 0)
