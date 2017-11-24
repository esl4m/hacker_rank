#!/bin/python3

q = int(input().strip())
for a0 in range(q):
    # every query starting from scrach
    sets_flat = {}
    labels = {}
    val_map = {}
    result = 0
    cnt = 0

    a = input()
    n_cities, n_roads, cost_lib, cost_road = a.strip().split(' ')
    n_cities, n_roads, cost_lib, cost_road = [int(n_cities), int(n_roads), int(cost_lib), int(cost_road)]

    if n_roads == 0:
        print(n_cities * cost_lib)
        continue

    if cost_lib < cost_road:
        print(cost_lib * n_cities)

        # ingest and pass remaining inputs
        for a1 in range(n_roads):
            input()
        continue

    for a1 in range(n_roads):
        cnt += 1

        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]

        c1_label = sets_flat.get(city_1, None)
        c2_label = sets_flat.get(city_2, None)

        if (not c1_label) and (not c2_label):
            label = 'set_{}'.format(cnt)
            val = 'val_{}'.format(cnt)
            labels[label] = val

            sets_flat[city_1] = label
            sets_flat[city_2] = label

            val_map[val] = [label]

        elif (c1_label) and (not c2_label):
            sets_flat[city_2] = c1_label

        elif (not c1_label) and (c2_label):
            sets_flat[city_1] = c2_label

        elif labels[c1_label] == labels[c2_label]:
            continue

        elif labels[c1_label] != labels[c2_label]:
            val_map[labels[c1_label]].extend(val_map[labels[c2_label]])
            val_map.pop(labels[c2_label])

            for label in val_map[labels[c1_label]]:
                labels[label] = labels[c1_label]

        result += cost_road  # +1 road

    # count libraries from merged sets
    result += (len(set(labels.values()))) * cost_lib

    # add separated cities
    count_cities_in_sets = len(sets_flat)
    if count_cities_in_sets < n_cities:
        result += (cost_lib * (n_cities - count_cities_in_sets))

    print(result)


# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def addEdge(self, X, Y):
#         self.graph[X].append(Y)
#         self.graph[Y].append(X)
#
# for ___ in range(int(input())):
#     g = Graph()
#     n, m, cl, cr = [int(x) for x in input().split()]
#     for __ in range(1, n + 1):
#         g.graph[__] = []
#
#     for _ in range(m):
#         a, b = [int(x) for x in input().split()]
#         g.addEdge(a, b)
#
#     answer = 0
#     if cl < cr:
#         answer = n * cl
#
#     else:
#         visit = [0] * (n + 1)
#         num = 1
#
#
#         def dfs(arg, num):
#             visit[arg] = num
#             for j in g.graph[arg]:
#                 if visit[j] == 0:
#                     dfs(j, num)
#
#
#         for i in g.graph:
#             if visit[i] == 0:
#                 dfs(i, num)
#                 num = num + 1
#
#         count = [0] * (num)
#         for k in visit[1::]:
#             count[k] = count[k] + 1
#         for z in count[1::]:
#             answer += cl + cr * (z - 1)
#
#     print(answer)