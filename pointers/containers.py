#!/usr/bin/env python3

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        i, j = 0, len(height) - 1
        while i < j:
            volume = (j - i) * min(height[i], height[j])
            max_volume = max(max_volume, volume)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                j -= 1
                i += 1
        return max_volume

Solution.maxArea(Solution, [8,7,2,1])
