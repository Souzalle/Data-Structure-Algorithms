# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None # Onde vou armazenar a lista invertida

        while head: # Enqt head apontar para algo, assim quando for None ele para
            next_node = head.next # aponta para o proximo, no primeiro caso o node pós head
            head.next = previous_node # muda o ponteiro do head original para a nova lista
            previous_node = head # previous_node vai para o antigo head
            head = next_node # transforma o proximo valor em head
        return previous_node

