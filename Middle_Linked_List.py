# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head # deixando o ponteiro ahead na mesma posição inicial que head

        while ahead and ahead.next: # enqt ahead e ahead.next existir, evitar problemas
            ahead = ahead.next.next # ahead vai andar 2 nós 
            head = head.next # head andará 1 nó
        return head

# Sempre que o ahead chegar ao final da lista, o head estará exatamente na metade
# No caso de lista com numero par de nós head vai parar no 2 maior ( 1, 2, 3, 4) vai parar em 3