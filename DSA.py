

from abc import ABC, abstractmethod



class DSA:
    class Stack:
        def __init__(self):
            self._list = []
            self.tail = 0

        def isEmpty(self):
            return len(self._list) == 0

        def push(self, element):
            self._list.append(element)
            self.tail += 1

        def pop(self):
            if not self.isEmpty():
                self._list.pop()
                self.tail -= 0
            else:
                raise print("stack is empty")

        def top(self):
            return print(self._list[self.tail])
    class Queue:
        def __init__(self):
            self._list = [None] * 10
            self.front = None
            self.rear = None

        def isEmpty(self):
            return len(self._list) == 0

        def __len__(self):
            return len(self._list) - self.front

        def eq(self, element):
            if self.rear == len(self._list):
                self.resize()
            avail = (self.front + self.rear) % len(self._list)
            self._list[avail] = element
            self.rear += 1

            if not self.isEmpty():
                self._list.append(element)
                self.tail += 1

        def resize(self):
            old = self._list
            self._list = [None] * (len(self._list) * 2)
            walk = self.front
            for i in range(self.rear):
                self._list[i] = old[walk]
                walk = (walk + 1) % len(self._list)
            self.front = 0
    class LinkedList:
        class SingleListNode:
            def __init__(self):
                self.val = None
                self.next = None

        class DoubleListNode:
            def __init__(self):
                self.val = None
                self.next = None
                self.prev = None

        class SingleLinkList:
            def __init__(self):
                self.head = DSA.LinkedList.SingleListNode()
                self.tail = None

            def insert(self, el):
                new_node = DSA.LinkedList.SingleListNode()
                new_node.val = el

                if self.head.val is None:
                    self.head = new_node
                    self.tail = new_node
                    self.head.next = self.tail
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                    # new_node.next = self.tail

            def delete(self):
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                    return print("deleted")
                if self.head.next.next is None:
                    self.head.next = None
                    self.tail = self.head
                    return print("deleted")
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next

                temp.next = None
                self.tail = temp
                print("deleted")

            def traverse(self):
                temp = self.head
                while temp:
                    print(temp.val, "->")
                    temp = temp.next

        class circular_linked_list:
            def __init__(self):
                self.head = DSA.LinkedList.SingleListNode()
                self.tail = self.head

            def insert(self, el):
                new_node = DSA.LinkedList.SingleListNode()
                new_node.val = el
                if self.head.val is None:
                    self.head = new_node
                    self.tail = new_node
                    self.tail.next = self.head
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.next = self.head

            def traverse(self):
                temp = self.head
                while temp:
                    print(temp.val)

                    if temp == self.tail:
                        # print(temp.next.val)
                        break

                    temp = temp.next

            def delete(self):
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                    return print("deleted")
                if self.head.next.next is None:
                    self.head.next = None
                    self.tail = self.head
                    return print("deleted")

                temp = self.head
                while temp is not None and temp.next.next != self.tail.next:
                    temp = temp.next

                temp.next = self.head
                self.tail = temp
                print("delete")

        class doubly_link_list:
            def __init__(self):
                self.head = DSA.LinkedList.DoubleListNode()
                self.tail = None

            def isEmpty(self):
                return self.head.val is None

            def insert(self, el):
                new_node = DSA.LinkedList.DoubleListNode()
                new_node.val = el

                if self.head.val is None:
                    self.head = new_node
                    self.tail = new_node
                    self.tail.prev = None
                else:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node

            def delete(self):
                pass

            def traverse(self):
                temp = self.head
                while temp.next:
                    if temp.prev is not None:
                        print("prev->", temp.prev.val, end="")
                    print("val->", temp.val)
                    temp = temp.next
    class Tree(ABC):
        """Abstract base class representing a tree structure."""

        class Position(ABC):
            """An abstraction representing the location of a single element."""

            @abstractmethod
            def element(self):
                """Return the element stored at this Position."""
                pass

            @abstractmethod
            def __eq__(self, other):
                """Return True if other represents the same Position."""
                pass

            def __ne__(self, other):
                """Return True if other does not represent the same Position."""
                return not (self == other)

        # ---------- Abstract methods ----------
        @abstractmethod
        def root(self):
            """Return the root Position of the tree (or None if empty)."""
            pass

        @abstractmethod
        def parent(self, p):
            """Return the Position of p's parent (or None if p is root)."""
            pass

        @abstractmethod
        def num_children(self, p):
            """Return the number of children of Position p."""
            pass

        @abstractmethod
        def children(self, p):
            """Generate an iteration of Positions representing p's children."""
            pass

        @abstractmethod
        def __len__(self):
            """Return the total number of elements in the tree."""
            pass

        # ---------- Concrete methods ----------
        def is_root(self, p):
            """Return True if Position p represents the root of the tree."""
            return self.root() == p

        def is_leaf(self, p):
            """Return True if Position p does not have any children."""
            return self.num_children(p) == 0

        def is_empty(self):
            """Return True if the tree is empty."""
            return len(self) == 0
    class BinaryTree(Tree, ABC):
        """Abstract base class representing a binary tree structure."""

        @abstractmethod
        def left(self, p):
            """Return the Position of p's left child (or None if no left child)."""
            pass

        @abstractmethod
        def right(self, p):
            """Return the Position of p's right child (or None if no right child)."""
            pass

        def sibling(self, p):
            """Return the Position of p's sibling (or None if no sibling)."""
            parent = self.parent(p)
            if parent is None:  # p is the root
                return None
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

        def children(self, p):
            """Generate an iteration of Positions representing p's children."""
            if self.left(p) is not None:
                yield self.left(p)
            if self.right(p) is not None:
                yield self.right(p)
    class LinkedBinaryTree(BinaryTree):
        """Linked representation of a binary tree structure."""

        class Node:
            """Lightweight, nonpublic class for storing a node."""
            __slots__ = "_element", "_parent", "_left", "_right"

            def __init__(self, element, parent=None, left=None, right=None):
                self._element = element
                self._parent = parent
                self._left = left
                self._right = right

        class Position():
            """An abstraction representing the location of a single element."""

            def __init__(self, container, node):
                """Constructor should not be invoked by user."""
                self._container = container
                self._node = node

            def element(self):
                """Return the element stored at this Position."""
                return self._node._element

            def __eq__(self, other):
                """Return True if other represents the same Position."""
                return type(other) is type(self) and other._node is self._node

        def _validate(self, p):
            """Return the associated Node if Position p is valid."""
            if not isinstance(p, self.Position):
                raise TypeError("p must be a proper Position type")
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            if p._node._parent is p._node:  # convention for deprecated nodes
                raise ValueError("p is no longer valid")
            return p._node

        def _make_position(self, node):
            """Return a Position instance for the given Node (or None if no node)."""
            return self.Position(self, node) if node is not None else None

        # ---------- Binary tree constructor ----------
        def __init__(self):
            """Create an initially empty binary tree."""
            self._root = None
            self._size = 0

        # ---------- Public accessors ----------
        def __len__(self):
            """Return the total number of elements in the tree."""
            return self._size

        def root(self):
            """Return the root Position of the tree (or None if tree is empty)."""
            return self._make_position(self._root)

        def parent(self, p):
            """Return the Position of p's parent (or None if p is root)."""
            node = self._validate(p)
            return self._make_position(node._parent)

        def left(self, p):
            """Return the Position of p's left child (or None if no left child)."""
            node = self._validate(p)
            return self._make_position(node._left)

        def right(self, p):
            """Return the Position of p's right child (or None if no right child)."""
            node = self._validate(p)
            return self._make_position(node._right)

        def num_children(self, p):
            """Return the number of children of Position p."""
            node = self._validate(p)
            count = 0
            if node._left is not None:
                count += 1
            if node._right is not None:
                count += 1
            return count

        # ---------- Nonpublic update methods ----------
        def add_root(self, e):
            """Place element e at the root of an empty tree and return its Position.
            Raise ValueError if the tree is not empty.
            """
            if self._root is not None:
                raise ValueError("Root exists")
            self._size = 1
            self._root = self.Node(e)
            return self._make_position(self._root)

        def add_left(self, p, e):
            """Create a new left child for Position p, storing element e.
            Return the Position of the new node.
            Raise ValueError if Position p is invalid or p already has a left child.
            """
            node = self._validate(p)
            if node._left is not None:
                raise ValueError("Left child exists")
            self._size += 1
            node._left = self.Node(e, node)  # node is its parent
            return self._make_position(node._left)

        def add_right(self, p, e):
            """Create a new right child for Position p, storing element e.
            Return the Position of the new node.
            Raise ValueError if Position p is invalid or p already has a right child.
            """
            node = self._validate(p)
            if node._right is not None:
                raise ValueError("Right child exists")
            self._size += 1
            node._right = self.Node(e, node)  # node is its parent
            return self._make_position(node._right)

        def replace(self, p, e):
            """Replace the element at Position p with e, and return the old element."""
            node = self._validate(p)
            old = node._element
            node._element = e
            return old

        def delete(self, p):
            """Delete the node at Position p, and replace it with its child, if any.
            Return the element that had been stored at Position p.
            Raise ValueError if Position p is invalid or p has two children.
            """
            node = self._validate(p)
            if self.num_children(p) == 2:
                raise ValueError("p has two children")
            child = node._left if node._left else node._right  # might be None
            if child is not None:
                child._parent = node._parent  # child's grandparent becomes parent
            if node is self._root:
                self._root = child  # child becomes root
            else:
                parent = node._parent
                if node is parent._left:
                    parent._left = child
                else:
                    parent._right = child
            self._size -= 1
            node._parent = node  # convention for deprecated node
            return node._element

        def attach(self, p, t1, t2):
            """Attach trees t1 and t2 as left and right subtrees of external Position p."""
            node = self._validate(p)
            if not self.is_leaf(p):
                raise ValueError("position must be a leaf")
            if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
                raise TypeError("Tree types must match")
            self._size += len(t1) + len(t2)
            if not t1.is_empty():
                # attach t1 as left subtree of node
                t1._root._parent = node
                node._left = t1._root
                t1._root = None  # set t1 instance to empty
                t1._size = 0
            if not t2.is_empty():
                # attach t2 as right subtree of node
                t2._root._parent = node
                node._right = t2._root
                t2._root = None  # set t2 instance to empty
                t2._size = 0
    class PriorityQueue:
        class Node:
            def __init__(self, data, priority):
                self.data = data
                self.priority = property
                self.next = None


        def __init__(self):
            self.head = None

        def push(self,data, priority):
            new_node = self.Node(data, priority)
            if self.head is not None or self.head.priority > priority:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next and current.next.priority <= priority:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

        def pop(self):
            if self.is_empty():
                raise IndexError("pop from an empty priority queue")

            temp = self.head
            self.head = self.head.next
            return temp.data

        def peek(self):
            if self.is_empty():
                raise IndexError("peek from an empty priority queue")
            return   self.head.data

        def is_empty(self):
            return self.head  is None

        def size(self):
            count = 1
            current= self.head

            while current:
                count +=1
                current = current.next
            return count
    class Empty(Exception):
        """custom exception to indicate an empty priority queue"""
        pass


    # Base Priority Queue Abstract Class
    class PriorityQueueBase(ABC):
        class Item:
            def __init__(self, key, value):
                self.key = key
                self.value = value

            def __lt__(self, other):
                return self.key < other.key

        @abstractmethod
        def add(self, key, value):
            pass

        @abstractmethod
        def min(self):
            pass

        @abstractmethod
        def remove_min(self):
            pass

        @abstractmethod
        def __len__(self):
            pass

    # Base Heap Implementation
    class HeapBase:
        """Base class for MinHeap and MaxHeap."""

        def __init__(self, elements=None):
            """Initialize the heap. If elements are provided, build the heap bottom-up."""
            self._data = elements if elements else []
            if elements:
                self._heapify()

        def __len__(self):
            return len(self._data)

        def is_empty(self):
            return len(self._data) == 0

        def _parent(self, index):
            return (index - 1) // 2

        def _left(self, index):
            return 2 * index + 1

        def _right(self, index):
            return 2 * index + 2

        def _swap(self, i, j):
            self._data[i], self._data[j] = self._data[j], self._data[i]

        def _sift_down(self, index):
            raise NotImplementedError("This method must be implemented by subclasses.")

        def _sift_up(self, index):
            raise NotImplementedError("This method must be implemented by subclasses.")

        def _heapify(self):
            start = self._parent(len(self._data) - 1)
            for i in range(start, -1, -1):
                self._sift_down(i)

        def add(self, value):
            self._data.append(value)
            self._sift_up(len(self._data) - 1)

        def remove(self):
            if self.is_empty():
                raise ValueError("Heap is empty.")
            self._swap(0, len(self._data) - 1)
            value = self._data.pop()
            if not self.is_empty():
                self._sift_down(0)
            return value

        def peek(self):
            if self.is_empty():
                raise ValueError("Heap is empty.")
            return self._data[0]

    # MinHeap Implementation
    class MinHeap(HeapBase):
        def _sift_down(self, index):
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left < len(self._data) and self._data[left] < self._data[smallest]:
                smallest = left
            if right < len(self._data) and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                self._sift_down(smallest)

        def _sift_up(self, index):
            while index > 0:
                parent = self._parent(index)
                if self._data[index] < self._data[parent]:
                    self._swap(index, parent)
                    index = parent
                else:
                    break

    # MaxHeap Implementation
    class MaxHeap(HeapBase):
        def _sift_down(self, index):
            largest = index
            left = self._left(index)
            right = self._right(index)

            if left < len(self._data) and self._data[left] > self._data[largest]:
                largest = left
            if right < len(self._data) and self._data[right] > self._data[largest]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                self._sift_down(largest)

        def _sift_up(self, index):
            while index > 0:
                parent = self._parent(index)
                if self._data[index] > self._data[parent]:
                    self._swap(index, parent)
                    index = parent
                else:
                    break

    # Priority Queue Using MinHeap
    class HeapPriorityQueue(PriorityQueueBase):
        """A Priority Queue implemented using a MinHeap."""

        def __init__(self):
            self._heap = self.MinHeap()

        def add(self, key, value):
            self._heap.add(self.Item(key, value))

        def min(self):
            if self._heap.is_empty():
                raise ValueError("Priority queue is empty.")
            item = self._heap.peek()
            return (item.key, item.value)

        def remove_min(self):
            if self._heap.is_empty():
                raise ValueError("Priority queue is empty.")
            item = self._heap.remove()
            return (item.key, item.value)

        def __len__(self):
            return len(self._heap)

    # Test Code
    if __name__ == "__main__":
        print("Testing MinHeap:")
        min_heap = MinHeap([5, 3, 8, 1, 9, 2])
        print("MinHeap (Bottom-Up Construction):", min_heap._data)
        min_heap.add(0)
        print("After adding 0:", min_heap._data)
        print("Removed:", min_heap.remove())
        print("After removal:", min_heap._data)

        print("\nTesting MaxHeap:")
        max_heap = MaxHeap([5, 3, 8, 1, 9, 2])
        print("MaxHeap (Bottom-Up Construction):", max_heap._data)
        max_heap.add(10)
        print("After adding 10:", max_heap._data)
        print("Removed:", max_heap.remove())
        print("After removal:", max_heap._data)

        print("\nTesting PriorityQueue:")
        pq = HeapPriorityQueue()
        pq.add(4, "Task A")
        pq.add(2, "Task B")
        pq.add(5, "Task C")
        pq.add(1, "Task D")
        print("Minimum element:", pq.min())
        print("Removed minimum:", pq.remove_min())
        print("Minimum element after removal:", pq.min())


# Create an instance of LinkedBinaryTree
tree = DSA.LinkedBinaryTree()

# Add a root node
root = tree.add_root("A")
print("Root added:", root.element())  # Output: Root added: A

# Add left and right children to the root
left_child = tree.add_left(root, "B")
right_child = tree.add_right(root, "C")
print("Left child of root:", left_child.element())  # Output: Left child of root: B
print("Right child of root:", right_child.element())  # Output: Right child of root: C

# Add left and right children to the left child of the root
tree.add_left(left_child, "D")
tree.add_right(left_child, "E")

# Add left and right children to the right child of the root
tree.add_left(right_child, "F")
tree.add_right(right_child, "G")

# Check the size of the tree
print("Size of the tree:", len(tree))  # Output: Size of the tree: 7

# Check if the root is a leaf
print("Is root a leaf?", tree.is_leaf(root))  # Output: Is root a leaf? False

# Check if a node is a leaf
leaf_node = tree.left(left_child)
print("Is D a leaf?", tree.is_leaf(leaf_node))  # Output: Is D a leaf? True

# Get the parent of a node
parent_of_E = tree.parent(tree.right(left_child))
print("Parent of E:", parent_of_E.element())  # Output: Parent of E: B

# Get the sibling of a node
sibling_of_F = tree.sibling(tree.left(right_child))
print("Sibling of F:", sibling_of_F.element())  # Output: Sibling of F: G

# Replace an element in the tree
old_element = tree.replace(tree.left(right_child), "X")
print("Replaced element at F:", old_element)  # Output: Replaced element at F: F
print("New element at X:", tree.left(right_child).element())  # Output: New element at X: X

# Delete a node with one child
deleted_element = tree.delete(tree.left(left_child))
print("Deleted element:", deleted_element)  # Output: Deleted element: D
print("Size of the tree after deletion:", len(tree))  # Output: Size of the tree after deletion: 6

# Attach two new trees to a leaf node
# Create two new trees
t1 = DSA.LinkedBinaryTree()
t1_root = t1.add_root("H")
t1.add_left(t1_root, "I")
t1.add_right(t1_root, "J")

t2 = DSA.LinkedBinaryTree()
t2_root = t2.add_root("K")
t2.add_left(t2_root, "L")
t2.add_right(t2_root, "M")

# Attach t1 and t2 to the right child of the root (C)
tree.attach(right_child, t1, t2)

# Check the size of the tree after attachment
print("Size of the tree after attachment:", len(tree))  # Output: Size of the tree after attachment: 11

# Print the tree structure using a traversal
def print_tree(tree, p):
    print(p.element())
    for child in tree.children(p):
        print_tree(tree, child)

print("Tree structure:")
print_tree(tree, tree.root())

# Output:
# Tree structure:
# A
# B
# E
# C
# X
# H
# I
# J
# K
# L
# M