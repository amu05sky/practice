# 876. Middle of the Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list from the given values
values = [1, 2, 3, 4, 5]
head = ListNode(values[0])
current = head
for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
print(slow)

    
# LeetCode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         slow = head
#         fast = head
#         while (fast!=None and fast.next!=None):
#             slow = slow.next
#             fast = fast.next.next
        
#         return slow