"""
Utilizar a mesma implementação que ja usei no binary tree

pre order: root vai ser primeiro valor da lista
    - ele vai andar, root, esquerda, direita

in order: root vai estar no centro, visto que a arvore desce dele e os valores menores são esquerda e os maiores direita
    - ele vai andar tudo pra esquerda, e voltar colocando os valores até o root, depois desde para a direita do root e repete, vai até a esquerda volta e direita

post order: root será o ultimo valor
    - ele anda toda a esquerda e vai colocando os valores, sobe até o root nao coloca ele e vai para a direita, e começa a checar se existe valores a esquerda, direita e só no fim coloca o root


"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)

# PRE ORDER A PARTIR DAQUI ================================================================

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

# POST ORDER A PARTIR DAQUI ================================================================

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)

# IN ORDER A PARTIR DAQUI ================================================================

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)


tree = BinaryTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for val in values_to_insert:
    tree.insert(val)

print(tree.search(7))
print(tree.search(14))
print(tree.search(10))
print(tree.search(18))

print("Preorder Traversal:", tree.preorder_traversal())
print("Inorder Traversal:", tree.inorder_traversal())
print("Postorder Traversal:", tree.postorder_traversal())