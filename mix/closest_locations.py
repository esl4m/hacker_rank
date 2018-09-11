# closest_locations.py .. By Eslam Diaa #


def close_stores(user_location, store_locations, n):
    temp_dict = {}
    for i, store in enumerate(store_locations):
        temp_dict.update({i: distance(user_location, store)})  # add the distance with it's actual value in dict

    location_keys = sort_dic(temp_dict)  # Getting the sorted location keys from the temp_dict based on distance value
    final_res = []
    for l in location_keys:
        final_res.append(store_locations[l])

    return final_res[:n]  # get the k nearest locations


def distance(user, store):
    """ function returns array of distance between user and store locations """
    return [a - b for a, b in zip(store, user)]


def sort_dic(d):
    res = []
    # Get only the key of sorted dict .. key is the actual store location
    for k in sorted(d, key=d.get):
        res.append(k)

    return res

    # Getting the sorted result from the dict. according to highest value
    # for w in sorted(d, key=d.get, reverse=True): print(w, d[w]) --- return list(res.values())[:2]

# Write a function that takes user location (x,y) and store locations and returns the closest store locations #
user_loc = [2, 2]
store_loc = [[5, 6], [5, 4], [3, 2], [1,1]]
k_num_location = 2
print(close_stores(user_loc, store_loc, k_num_location))
