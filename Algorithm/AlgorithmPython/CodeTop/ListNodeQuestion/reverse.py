# coding=utf-8

"""
题目：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
解法1：列表状态变化展示
S0: None; 1 - 2 - 3 - 4 - 5
S1: 1; 2 - 3 - 4 - 5
S2: 2 - 1; 3 - 4 - 5
S3: 3 - 2 - 1; 4 - 5
S4: 4 - 3 - 2 - 1; 5
S5: 5 - 4 - 3 - 2 - 1; None
右侧链表状态实际上与head = head.next的循环状态一致
左侧起始为None，后逐渐变成倒序head，作为返回结果
这样需要一个变量res存储左侧链表状态
需要tmp作为临时头插到左侧head之前
"""


def reverseList(head):
    res = None
    while head:
        tmp = head
        head = head.next
        tmp.next = res
        res = tmp
    return res


if __name__ == "__main__":
    from define import list_to_listnode, listnode_to_list
    head = list_to_listnode([1, 2, 3, 4, 5])

    # test for reverseList
    reversed_head = reverseList(head)
    print(listnode_to_list(reversed_head))
