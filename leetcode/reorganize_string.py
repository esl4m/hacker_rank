#!/bin/python3

#  reorganize_string.py .. Leetcode
#  by: esl4m diaa
#      25 Mar 2020

"""
https://leetcode.com/problems/reorganize-string/
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Ex1
Input: S = "aab"
Output: "aba"

Ex2
Input: S = "aaab"
Output: ""
"""


class Solution:

    def reorganize_string(self, s):
        ln_s = len(s)
        arr = []

        for c, x in sorted((s.count(x), x) for x in set(s)):
            # print(c, x)
            if c > (ln_s+1) / 2:
                return ''
            arr.extend(c * x)

        res = [None] * ln_s
        res[::2], res[1::2] = arr[ln_s/2:], arr[:ln_s/2]

        # print(res)
        return ''.join(res)

S = "baabaab"
c = Solution()
print(c.reorganize_string(S))
