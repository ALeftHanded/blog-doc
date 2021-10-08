# coding=utf-8
from CodeTop.String.random_string import random_string_generator
from random import randint


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
    max_length, i, str_index_dic = 0, -1, {}
    for j, ch in enumerate(s):
        if ch in str_index_dic and str_index_dic[ch] > i:
            i = str_index_dic[ch]
            str_index_dic[ch] = j
        else:
            str_index_dic[ch] = j
        max_length = max(max_length, j - i)
    return max_length


if __name__ == '__main__':
    test = random_string_generator(size=100000)
    # test = "Azz1ZFp0AwDpPA9"
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
