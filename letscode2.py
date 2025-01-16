from letscode import SimpleRandomEasyDumAssQuestions, DSA, LeetCode

# Create instances
_instanceSimpleRandomEasyDumAssQuestions = SimpleRandomEasyDumAssQuestions()
_instanceDSA = DSA()
_instanceLeetCode = LeetCode()
_instance_list_stack = DSA.Stack()
_instance_list_queue = DSA.Queue()

# Test SimpleRandomEasyDumAssQuestions class
print("Testing SimpleRandomEasyDumAssQuestions class:")
print("Fibonacci of 5:", _instanceSimpleRandomEasyDumAssQuestions.fibonacci(5))  # Output: 5
print("Sum of list [1, 2, 3, 4]:", _instanceSimpleRandomEasyDumAssQuestions.summing_el_list([1, 2, 3, 4]))  # Output: 10
print("Sum of list [1, 2, 3, 4] using binary recursion:", _instanceSimpleRandomEasyDumAssQuestions.summing_el_list_binary_recursion([1, 2, 3, 4], 0, 4))  # Output: 10
print("Power of 2^3:", _instanceSimpleRandomEasyDumAssQuestions.power(2, 3))  # Output: 8

# Test DSA.Stack class
print("\nTesting DSA.Stack class:")
_instance_list_stack.push(10)  # Output: Element pushed successfully
_instance_list_stack.push(20)  # Output: Element pushed successfully
_instance_list_stack.push(30)  # Output: Element pushed successfully
print("Stack traversal:")
_instance_list_stack.list_traverse()  # Output: 10 20 30
_instance_list_stack.pop()  # Output: Element popped successfully
print("Stack traversal after pop:")
_instance_list_stack.list_traverse()  # Output: 10 20

# Test DSA.Queue class
print("\nTesting DSA.Queue class:")
_instance_list_queue.enqueue(10)
_instance_list_queue.enqueue(20)
_instance_list_queue.enqueue(30)
print("Queue length:", _instance_list_queue.queue_len())  # Output: 3
print("First element of queue:", _instance_list_queue.first_element_of_queue())  # Output: 10
_instance_list_queue.dequeue()
print("Queue length after dequeue:", _instance_list_queue.queue_len())  # Output: 2
print("First element of queue after dequeue:", _instance_list_queue.first_element_of_queue())  # Output: 20

# Test DSA.binary_search method
print("\nTesting DSA.binary_search method:")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Is 5 in the list?", _instanceDSA.binary_search(data, 5, 0, len(data) - 1))  # Output: True
print("Is 10 in the list?", _instanceDSA.binary_search(data, 10, 0, len(data) - 1))  # Output: False

# Test reversing_a_list method
print("\nTesting reversing_a_list method:")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
_instanceSimpleRandomEasyDumAssQuestions.reversing_a_list(my_list, 0, len(my_list))
print("Reversed list:", my_list)  # Output: [5, 4, 3, 2, 1]