#!/usr/bin/python3
"""
https://leetcode.com/problems/defanging-an-ip-address/
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
"""
# Ex: 1
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"


class Solution():

    def defang_ip(self, ip_address):
        replaced_str = "[.]"
        res = ""

        for i in ip_address:
            if i == '.':
                res += replaced_str
            else:
                res += i

        return res


s = Solution()
address = "1.1.1.1"
print(s.defang_ip(address))
