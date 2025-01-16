from abc import  ABC,abstractmethod
class Tree(ABC):
    class Position(ABC):
        @abstractmethod
        def element(self):
            pass
        @abstractmethod
        def __eq__(self):
            pass
        @abstractmethod
        def __ne__(self, other):
            pass
    @abstractmethod
    def root(self):
        pass
    @abstractmethod
    def parent(self, p):
        pass
    @abstractmethod
    def num_of_children(self, p):
        pass
    @abstractmethod
    def children(self, p):
        pass
    def __len__(self):
        pass
    def is_root(self, p):
        pass
    def is_leaf(self, p):
        pass

    def is_empty(self, p):
        pass

class BinaryTree(ABC, Tree):
    @abstractmethod
    def left(self, p):
        pass
    @abstractmethod
    def right(self, p):
        pass
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if  p == self.left(parent):
            return  self.right(parent)
        else:
            return self.left(parent)
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield  self.right(p)



class LinkedBinaryTree(ABC, BinaryTree):
    class Node:
        def __init__(self, element, parent=None, left= None, right = None):
            self.element = element
            self.right = right
            self.left = left
            self.parent= parent

    class Position(ABC,Node):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return  type(other) is type(self) and other._node is self._node

    def _validate(self,p):
        if not isinstance(p, self.Position):
            raise  TypeError("p must be a proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")

        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node


    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None


    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    def left(self, p):
        node  = self._validate(p)
        return self._make_position(node._left)
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def add_root(self,e):
        if self._root is not None:
            raise ValueError("Root Exists")
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)


    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size+=1
        node._left = self.Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exist")
        self._size +=1
        node._right = self.Node(e, node)
        return self._make_position(node._right)

    def replace(self,p, e):
        node = self._validate(p)
        old=node._element
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_of_children(p)==2:
            raise ValueError("p has two children")
        child = node ._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -=1
        node._parent = node
        return node._element


    def attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be a leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            node._right = t2._root
            t2._root = None
            t2.size =0





