# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = None
        curr = dummy_head
        p = l1
        q = l2
        carry = 0
        while p is not None or q is not None:
            # retrieve input value
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0

            # perform summation of each digit value
            addition = carry + x + y
            carry = int(addition / 10)

            # create a node
            if curr is None:
                curr = ListNode(addition % 10)
                dummy_head = curr
            else:
                curr.next = ListNode(addition % 10)
                # point to new node
                curr = curr.next

            # advance to next inputs node
            if p is not None:
                p = p.next

            if q is not None:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)  # create new node to hold extra carry value

        return dummy_head

# add two number
# given 342 + 465, result = 807
# Linked list in reverse order
# 342 : 2->4->3
# 465 : 5->6->4
# 807 : 7->0->8
if __name__ == "__main__":
    sln = Solution()
    # 2->4->3
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # 5->6->4
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    # result 7->0->8
    res = sln.addTwoNumbers(l1, l2)

    print(res)