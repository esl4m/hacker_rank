#!/bin/python3

#  Longest Substring Without Repeating Characters .. Leetcode
#  by: esl4m diaa
#      13 Nov 2020

class Solution:
    
    def lengthOfLongestSubstring(self, s):
        output = 0
        left = 0
        seen = {}
        
        for i, char in enumerate(s):
            # When a duplicate is seen, update the left pointer to the last time the character was seen. 
            # No need to update the left pointer one by one.
            if char in seen and left <= seen[char]:
                left = seen[char] + 1
            else:
                # Update the max length
                output = max(output, i - left + 1)
            
            # Keep a track of latest position of every char in string
            seen[char] = i

        return output

if __name__ == '__main__':
    s = Solution()
    st1 = "abcabcbb"
    st2 = "bbbbb"
    st3 = "pwwkew"
    st4 = ""

    print(s.lengthOfLongestSubstring(st1)) # ---> Output: 3
    print(s.lengthOfLongestSubstring(st2)) # ---> Output: 1
    print(s.lengthOfLongestSubstring(st3)) # ---> Output: 3
    print(s.lengthOfLongestSubstring(st4)) # ---> Output: 0

