class DSA:

    class Linkedlist:
        class SingleTreeNode:
            def __init__(self):
                self.val = None
                self.next = None

        class DoublyTreeNode:
            def __init__(self):
                self.prev = None
                self.next = None
                self.val = None


        class SingleLinkList:

            def __init__(self):
                self.head = DSA.Linkedlist.SingleTreeNode()
                self.tail = None

            def insert_element(self,el):
                if self.head.val is None:
                    self.head.val = el
                    self.head.next = DSA.Linkedlist.SingleTreeNode()
                    self.tail = self.head
                else:
                    new_node= DSA.Linkedlist.SingleTreeNode()
                    new_node.val = el
                    self.tail.next = new_node
                    self.tail = new_node

            def traverse(self):
                temp = self.head
                while temp is not None:
                    print(temp.val)
                    temp = temp.next

        class DoublyLinkLIst:
            def __init__(self):
                self.head = DSA.Linkedlist.DoublyTreeNode()
                self.tail = None

            def insert_element(self,el):
                if self.head.val is None:
                    self.head.val  = el
                    self.tail = None
                    self.head.next = DSA.Linkedlist.DoublyTreeNode()
                    self.head.prev = None
                    self.tail = self.head
                else:
                    new_node = DSA.Linkedlist.DoublyTreeNode()
                    new_node.val = el
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node

            def traverse(self):
                temp = self.head
                while temp is not None:
                    if temp.prev:
                        print(temp.prev.val, temp.val)
                    else:
                        print(temp.val)
                    temp  = temp.next

        class CircualarList:
            def __init__(self):
                self.head = DSA.Linkedlist.SingleTreeNode()
                self.tail  = None

            def insert_element(self, el):
                if self.head.val is None:
                    self.head.val = el
                    self.head.next = DSA.Linkedlist.SingleTreeNode()
                    self.tail = self.head
                else:
                    new_node = DSA.Linkedlist.SingleTreeNode()
                    new_node.val = el
                    new_node.next = self.head.next
                    self.tail.next = new_node
            def traverse(self):
                temp  = self.head
                while temp is not None and temp.next != self.head:
                    print(temp.val)
                    temp = temp.next



a = DSA.Linkedlist.CircualarList()

a.insert_element(5)
a.insert_element(10)

a.insert_element(15)

a.insert_element(15)
a.traverse()