# Write a function that takes some words and return the recursive string


def string_recursion(s):
    str_arr = s.split()  # convert the string input to arr.
    res = []
    for w in str_arr[::-1]:
        res.append(w)

    res = " ".join(res)  # convert the result to string

    return res

main_str = "Dogs bites men who's are bad"
print(string_recursion(main_str))
