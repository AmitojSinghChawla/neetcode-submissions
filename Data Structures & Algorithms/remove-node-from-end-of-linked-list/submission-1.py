# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None and n ==1 :
            head = None
            return head

        curr = head
        length = 0
        while curr:
            length +=1
            curr = curr.next
        
        index = length - n

        current = head
        prev = None
        for i in range(0,index+1):
            if index == 0 :
                temp = current.next
                current.next = None
                return temp
            if i == index :
                temp = current.next
                prev.next = temp
                current.next = None
                return head
            else:
                prev = current
                current = current.next