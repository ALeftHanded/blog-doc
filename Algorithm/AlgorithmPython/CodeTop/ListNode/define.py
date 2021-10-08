# coding=utf-8

# 链表定义
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def list_to_listnode(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    p = head
    for i in range(1, len(lst)):
        p.next = ListNode(lst[i])
        p = p.next
    return head


def listnode_to_list(head):
    if not head:
        return []
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
