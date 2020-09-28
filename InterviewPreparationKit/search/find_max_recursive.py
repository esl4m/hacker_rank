# user a rercursive algorithm to find max value.

items = [6, 20, 8, 91, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # TODO break condition last item n list? return it.
    if len(items) == 1:
        return items[0]
    
    # TODO else get the first item , call function again to continue the other list
    op1 = items[0]
    # print(op1)
    op2 = find_max(items[1:])
    # print(op2)

    # TODO perform the comparison when it's down to just two
    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(items))
