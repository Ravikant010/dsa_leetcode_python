class SimpleRandomEasyDumAssQuestions:
    def __init__(self):
        pass

    def fibonacci(self, number):
        if number < 0:
            print("Invalid input")
            return None
        elif number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return self.fibonacci(number - 1) + self.fibonacci(number - 2)

    def summing_el_list(self, _list, index=0):
        if _list is None or index >= len(_list):
            return 0
        else:
            return _list[index] + self.summing_el_list(_list, index + 1)

    def summing_el_list_binary_recursion(self, _list, start, stop):
        if start >= stop:
            return 0
        if start == stop - 1:
            return _list[start]
        else:
            mid = (start + stop) // 2
            return self.summing_el_list_binary_recursion(_list, start, mid) + self.summing_el_list_binary_recursion(_list, mid, stop)

    def reversing_a_list(self, _list, start, stop):
        if start < stop - 1:
            _list[start], _list[stop - 1] = _list[stop - 1], _list[start]
            return self.reversing_a_list(_list, start + 1, stop - 1)

    def power(self, x, n):
        if n == 0:
            return 1
        else:
            return x * self.power(x, n - 1)


class LeetCode:
    def __init__(self):
        pass


class DSA:
    def __init__(self):
        pass

    def binary_search(self, data, target, low, high):
        if low > high:
            return False
        else:
            mid = (high + low) // 2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                return self.binary_search(data, target, low, mid - 1)
            else:
                return self.binary_search(data, target, mid + 1, high)

    class Stack:
        def __init__(self):
            self._list = []

        def is_empty(self):
            return len(self._list) == 0

        def list_traverse(self):
            if not self.is_empty():
                for i in self._list:
                    print(i)

        def push(self, element):
            self._list.append(element)
            print("Element pushed successfully")

        def pop(self):
            if not self.is_empty():
                self._list.pop()
                print("Element popped successfully")
            else:
                print("Empty list")


        class StackLinkedList:
            pass


    class Queue:
        def __init__(self):
            self._list = []
            self.count = 0

        def is_empty(self):
            return len(self._list) == 0

        def enqueue(self, el):
            self._list.append(el)

        def dequeue(self):
            if not self.is_empty() and self.count < len(self._list):
                del self._list[self.count]
                self.count += 1

        def first_element_of_queue(self):
            if not self.is_empty():
                return self._list[self.count]

        def queue_len(self):
            return len(self._list) - self.count

        def __len__(self):
            return len(self._list)

        def _resize(self,cap):
            old  = self._list
            walk = self.count
            self._list = [None] * cap
            for i in old:
                self._list[i] = old[walk]
                walk  = (walk+1) % len(old)
            self.count = 0

