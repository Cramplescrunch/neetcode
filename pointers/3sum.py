#!/usr/bin/env python3

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        i = 0
        while i <= len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum  == 0:
                    result.append(sorted([nums[i], nums[j], nums[k]]))
                    k -= 1
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j +=1
            i += 1
        new_r = []
        for e in result:
            if e not in new_r:
                new_r.append(e)
        return new_r

Solution.threeSum(Solution, [-1,0,1,2,-1,-4])
Solution.threeSum(Solution, [0,1,1])
Solution.threeSum(Solution, [0,0,0])
Solution.threeSum(Solution, [3,0,-2,-1,1,2])
