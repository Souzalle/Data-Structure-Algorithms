class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not len(self.items):
            raise IndexError("Empty List")
        
        return self.items.pop()
    
    def peek(self):
        if not len(self.items):
             raise IndexError("Empty List")
        
        return self.items[-1] # o -1 me mostra o ultimo valor da lista, dessa forma eu n precisao saber se ela tem 5, 10, 20 itens, o -1 me garante que o ultimo sera mostrado
    
    def size(self):
        return len(self.items)
               
    
