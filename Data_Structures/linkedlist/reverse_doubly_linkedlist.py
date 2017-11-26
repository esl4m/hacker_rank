#!/bin/python3

#  reverse_doubly_linkedlist.py LinkedList Task .. HackerRank
#  by: esl4m diaa
#      23 Nov 2017

"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def reverse(head):
    if not head:  # if null return it.
        return head

    head.next, head.prev = head.prev, head.next  # swap prev and next pointers
    if not head.prev:
        return head
    return reverse(head.prev)

# Time Complexity:O(N)
# Passed the hacker rank input
