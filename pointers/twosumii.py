#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i <= j:
            print(i)
            print(j)
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]

Solution.twoSum(Solution, [2,7,11,15], 9)
Solution.twoSum(Solution, [2,3,4], 6)
Solution.twoSum(Solution, [-1,0], -1)
