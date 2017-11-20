# __author__ = 'eslam'

s = raw_input().strip()

seq = "SOS"  # sequence to check

wrongLetters = 0
for i in xrange(len(s)):
    #if s[i] not in seq:
    if s[i] != seq[i%3]:
        wrongLetters += 1
print(wrongLetters)
