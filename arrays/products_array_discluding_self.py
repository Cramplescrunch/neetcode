#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[i] = nums[i]
        res = []
        for i in range(len(nums)):
