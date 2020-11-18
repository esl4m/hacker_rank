#!/usr/bin/python3
#  by: esl4m diaa
#      18 Nov 2020

# Problem link https://coderbyte.com/editor/Questions%20Marks:Python3

def solution(s):
    if not s:
        return False

    current = 0
    res = False
    count_q = 0

    for char in s:
        if char.isdigit():
            if int(char) + current == 10:
                if count_q != 3:
                    return "false"
                res = True
            current = int(char)
            count_q = 0
        if char == "?":
            count_q += 1
    
    return "true" if res else "false"

s = 'aa6?9'
s1 = 'acc?7??sss?3rr1??????5'
s2 = 'acc?7??sss?3rr5??????5'
s3 = 'acc?7??sss?3rr5??5'
s4 = 'acc?7??sss?3rr5???5'
print (solution(s))
print (solution(s1))
print (solution(s2))
print (solution(s3))
print (solution(s4))



"""
const r = /[a-z]/gi

cleanStr = str.replace(r, "")
list = cleanStr.match(/[0-9]\?+[0-9]/gi);
result = false;
for (i=0; i < list.length; i++) {
    if ( (Number(list[i][0]) + Number(list[i][(list[i].length)-1])) == 10) {
        if (list[i].length != 5) {
            result = false
            break
        } else {
            result = true
        }
    }
}
console.log(result)
# https://jsfiddle.net/d3k1p9xf/1
"""
