node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = Node(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, tree):
        if tree is not None:
            print(tree.data)
            self.preorder_trav(tree.left)
            self.preorder_trav(tree.right)
    
    def inorder_trav(self, tree):
        if tree is not None:
            self.inorder_trav(tree.left)
            print(tree.data)
            self.inorder_trav(tree.right)
    
    def postorder_trav(self, tree):
        if tree is not None:
            self.postorder_trav(tree.left)
            self.postorder_trav(tree.right)
            print(tree.data)