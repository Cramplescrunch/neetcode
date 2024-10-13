#!/usr/bin/env python3

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = {}
        for num in nums:
            if num in countMap.keys():
                countMap[num] += 1
            else:
                countMap[num] = 1
        countMapTops = sorted(countMap.items(), key=lambda item: item[1], reverse=True)
        result = []
        for val in countMapTops:
            result.append(val[0])
        return result[:k]

nums = [4,1,-1,2,-1,2,3]
print(Solution.topKFrequent(Solution, nums, 2))
