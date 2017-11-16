#!/bin/python3

#  linkedlist_elements.py LinkedList Task .. HackerRank
#  by: esl4m diaa
#      08 Nov 2017

def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)

l = [1, 2, 3]
print_list(l)
