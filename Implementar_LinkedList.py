class Node:
    def __init__(self, value): #Criando o nó, ele recebe um valor e aponta para o proximo e anterior
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList: # Criando Head e Tail da lista, criado vazio
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value): 
        new_node = Node(value) # cria o nó com o valor recebido em value
        if not self.head: # Se não existir um head, n existe nenhum nó, ent o novo nó vira head e tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head # novo nó aponta para o antigo primeiro nó
            self.head.prev = new_node # o antigo primeiro aponta para o novo
            self.head = new_node # novo nó passa a ser o head

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail # novo nó aponta para o antigo tail
            self.tail.next = new_node # antigo tail passa a apontar para o novo tail
            self.tail = new_node # novo nó passa a ser o tail 

    def remove_from_front(self):
        if not self.head: # se n houver head n ha lista, ent n ha oq remover
            return None
        removed_value = self.head.value # valor q ia ser removido é guardado 
        if self.head == self.tail: # se o head for igual ao tail, só existe um elemento
            self.head = self.tail = None # removendo o unico elemento, lista esta vazia
        else:
            self.head = self.head.next # transforma o segundo nó no head
            self.head.prev = None # remove o vinculo com o antigo primeiro nó
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail: # igual ao de cima
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev # o penultimo passa a ser o tail
            self.tail.next = None # corta o vinculo do penultimo(atual tail) com o antigo tail 
        return removed_value