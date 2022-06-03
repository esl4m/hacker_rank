#!/usr/bin/python


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:  # score are equal
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0


n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print(i.name, i.score)

# input
# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150

# Expected Output
# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50
