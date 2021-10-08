# coding=utf-8
from CodeTop.StringTools.random_string import random_string_generator
# from random import randint


def lengthOfLongestSubstring_for_test(s):
    res = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            tmp_str = s[i: j + 1]
            if len(tmp_str) == len(set(tmp_str)) and len(tmp_str) > res:
                res = len(tmp_str)
    return res


def lengthOfLongestSubstring_v2(s):
    i, j, res, str_index_dic = 0, 1, 0, {}
    while j < len(s) + 1:
        if s[j - 1] not in str_index_dic:
            str_index_dic[s[j - 1]] = j - 1
            res = max(j - i, res)
        else:
            i = str_index_dic[s[j - 1]] + 1
            str_index_dic = {s[index]: index for index in range(i, j)}
        j += 1
    return res


def lengthOfLongestSubstring_v3(s):
    res, i, str_index_map = 0, -1, {}
    for j, ch in enumerate(s):
        if ch in str_index_map and str_index_map[ch] > i:
            i = str_index_map[ch]
            str_index_map[ch] = j
        else:
            str_index_map[ch] = j
        res = max(res, j - i)
    return res


if __name__ == '__main__':
    test = random_string_generator(size=150)
    # test = "tmmzuxt"
    print(test)

    from time import process_time

    # a = process_time()
    # ans = lengthOfLongestSubstring_for_test(test)
    # b = process_time() - a
    # print("----- for_test -----")
    # print(ans, b)

    a = process_time()
    ans = lengthOfLongestSubstring_v2(test)
    b = process_time() - a
    print("----- v2 -----")
    print(ans, b)

    a = process_time()
    ans = lengthOfLongestSubstring_v3(test)
    b = process_time() - a
    print("----- v3 -----")
    print(ans, b)
