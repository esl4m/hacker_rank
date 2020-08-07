#!/usr/bin/python3
#
# By Islam (esl4m)
# 7 Aug 2020
#
# Problem Link: https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        
        for index, item in enumerate(nums):
            if(target - item) in lookup:
                return [lookup[target-item], index]
            else:
                lookup[item] = index
        
        return lookup

nums = [2,7,11,15]
target = 9
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums, target))
