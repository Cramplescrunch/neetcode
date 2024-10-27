#!/usr/bin/env python3
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        map = {}
        for i in range(len(strs)):
            map[i] = strs[i]
        return str(map)

    def decode(self, s: str) -> List[str]:
        map = eval(s)
        return list(map.values())

input = ["we","say",":","yes"]
encoded = Solution.encode(Solution, input)
print(encoded)
print(Solution.decode(Solution, encoded))
