def lengthOfLongestSubstring_for_test(s):
    res = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            tmp_str = s[i: j + 1]
            if len(tmp_str) == len(set(tmp_str)) and len(tmp_str) > res:
                res = len(tmp_str)
    return res


def lengthOfLongestSubstring_v1(s):
    if not s:
        return 0
    i, j, res, str_index_dic = 0, 1, 1, {}
    while j < len(s) + 1:
        j_str = s[j - 1]
        if j_str not in str_index_dic:
            str_index_dic[j_str] = j - 1
            res = len(str_index_dic) if len(str_index_dic) > res else res
        # print(str_index_dic, i, j, s[i:j])
        else:
            del_keys = []
            for key in str_index_dic:
                if i <= str_index_dic[key] < str_index_dic[j_str]:
                    del_keys.append(key)
            for key in del_keys:
                str_index_dic.pop(key, None)
            i = str_index_dic[j_str] + 1
            str_index_dic[j_str] = j - 1
        # print(str_index_dic, i, j, s[i:j])
        j += 1
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


def lengthOfLongestSubstring_best(s):
    max_length, i, str_index_dic = 0, -1, {}
    for j, ch in enumerate(s):
        if ch in str_index_dic and str_index_dic[ch] > i:
            i = str_index_dic[ch]
            str_index_dic[ch] = j
        else:
            str_index_dic[ch] = j
        max_length = max(max_length, j - i)
    return max_length
