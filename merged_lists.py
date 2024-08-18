# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

# Helper function to print the linked list
def print_linkedlist(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Manually creating the first linked list: 1 -> 6 -> 4
list1 = ListNode(1)
list1.next = ListNode(6)
list1.next.next = ListNode(4)

# Manually creating the second linked list: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two linked lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged linked list
print_linkedlist(merged_list)
