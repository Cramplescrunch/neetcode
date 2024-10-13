#!/usr/bin/env python3

class Solution:
    def groupAnagrams(self, strs):
        anagramsMap = {}
        for word in strs:
            lettersCount = {}
            for letter in word:
                if letter in lettersCount.keys():
                   lettersCount[letter] = lettersCount[letter] + 1
                else:
                    lettersCount[letter] = 1
            lettersCount = dict(sorted(lettersCount.items()))
            lettersCountStr = str(lettersCount)
            if lettersCountStr in anagramsMap:
                anagramsMap[lettersCountStr].append(word)
            else:
                anagramsMap[lettersCountStr] = [word]
            print(lettersCount)
        result = []
        for item in anagramsMap.values():
            result.append(item)
        return result

strs = ["ddddddddddg","dgggggggggg"]
print(Solution.groupAnagrams(Solution, strs))
