import itertools as it


def str_rev(input_str):
    return input_str[::-1]


def probability_comb(string, pair_num):
    comb_list = []
    for i in it.combinations(string, pair_num):
        comb_list.append("".join(i))
    return comb_list


# for i in probability_comb("abcde", 3):
#     print(i)
