"""
https://leetcode.com/problems/verifying-an-alien-dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

"""

# input words = ["hello", "leetcode"] , order = "hlabcdefgijkmnopqrstuvwxyz"
# output: true
# explain .. as h comes before l , then the sequence is sorted

# ex 2
# input words = ["word", "world", "row"] , order = "worldabcefghijkmnpqstuvxyz"
# output: false
# explain .. as d comes after l , then words[0] > words[1] , hence the sentence is unsorted.

# ex 3
# input words = ["apple", "app"] , order = "abcdefghijklmnopqrstuvwxyz"
# output: false
# explain .. the first 3 characters are same , and the second string is shorter in size. "apple" > "app" .

class Alien(object):

    def compare_sorted(self, words, order):
        # create a "dict" to add index for each letter in order
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # find the first diff
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]] :
                        return False
                    break

                else:
                    # handle the words apple , app
                    if len(word1) > len(word2):
                        return False
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
a = Alien()
print(a.compare_sorted(words, order))
