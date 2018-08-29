class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        _root = None
    
    def search(self, key):
        cur = self._root
        while cur:
            if key < cur.data:
                cur = cur.left
            elif key > cur.data:
                cur = cur.right
            else:
                return cur
        return None

    def insert(self, key):
        if _root == None:
            _root = Node(key)
            return
        cur = self._root
        while cur:
            if key < cur.data:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(key)
            elif key > cur.data:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(key)
            else:
                return
    
    def delete(self, key):
        parent, cur = None, self._root
        while cur:
            if key < cur.data:
                parent = cur
                cur = cur.left
            elif key > cur.data:
                parent = cur
                cur = cur.right
            else:
                break
        else:
            return false
        
        if cur.left is None and cur.right is None:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        
        elif cur.left is not None and cur.right is None:
            if parent.left == cur:
                parent.left = cur.left
            else:
                parent.right = cur.left
        elif cur.left is None and cur.right is not None:
            if parent.left == cur:
                parent.left = cur.right
            else:
                parent.right = cur.right
            
        else:
            p, q = cur, cur.right
            while q.left:
                p = q
                q = q.left
            cur.data = q.data
            if p.right == q:
                p.right = None
            else:
                p.left = None