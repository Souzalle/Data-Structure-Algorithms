# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None # Onde vou armazenar a lista invertida

        while head: # Enqt head apontar para algo, assim quando for None ele para
            next_node = head.next # aponta para o proximo, no primeiro caso o node pós head
            head.next = new_list # muda o ponteiro do head original para a nova lista
            new_list = head # new_list vai para o antigo head
            head = next_node # transforma o proximo valor em head
        return new_list 
    
