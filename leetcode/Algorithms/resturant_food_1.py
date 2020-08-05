#!/usr/bin/python3
#
# By Islam (esl4m)
# 4 Aug 2020
#
# Problem Link: https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from collections import defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_items = list({order[2] for order in orders})
        food_items.sort()
        
        res = [["Table"]]
        res[0].extend(food_items)
        
        hashmap=defaultdict(dict)
        
        for order in orders:
            if order[2] in hashmap[order[1]]:
                hashmap[order[1]][order[2]] += 1
            else:
                hashmap[order[1]][order[2]] = 1
        
        customers = sorted({int(c[1]) for c in orders})
        
        for c in customers:
            c = str(c)
            alist = []
            order = hashmap[c]
            
            for item in food_items:
                if item in order:
                    alist.append(str(order[item]))
                else:
                    alist.append("0")
                
            alist = [c] + alist
            res.append(alist)
        
        return res

# input
orders = [
    ["David","3","Ceviche"],
    ["Corina","10","Beef Burrito"],
    ["David","3","Fried Chicken"],
    ["Carla","5","Water"],
    ["Carla","5","Ceviche"],
    ["Rous","3","Ceviche"]
]

# expected output:


if __name__ == "__main__":
    s = Solution()
    print(s.displayTable(orders))
