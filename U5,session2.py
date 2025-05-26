#Problem 1: Greatest Node
'''
Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. 
You can assume the linked list will contain only numeric values.
Evaluate the time and space complexity of your solution. Define your variables and provide 
a rationale for why you believe your solution has the stated time and space complexity.
'''
def problem_1():
    #U:
    '''
    What if the linked list is empty?
    '''
    #P:
    '''
    1. Define a function find_max that accepts the head of a linked list
    2. Initialize a variable max_value to negative infinity
    3. Loop through each node in the linked list    
    4. If the value of the current node is greater than max_value, update max_value
    5. Return max_value
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def find_max(head):
        max_value = float('-inf')
        
        current = head
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value
    
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    head1 = Node(5, Node(6, Node(7, Node(8))))
    print(find_max(head1))

    head2 = Node(5, Node(8, Node(6, Node(7))))
    print(find_max(head2))

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
    '''

# Problem 2: Remove Tail
'''
The following code incorrectly implements the function remove_tail(). 
When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node 
(the tail) in the list. The function should return the head of the modified list.
Step 1: Copy this code into Replit.
Step 2: Create your own test cases to run the code against. Use print statements, 
print_linked_list(), and the stack trace to identify and fix any bugs so that the function 
correctly removes the last node from the list.
'''
def problem_2():
    #U: 
    '''
    What if the linked list is empty?
    What if the linked list has only one node?
    '''
    #P:
    '''
    1. Define a function remove_tail that accepts the head of a linked list
    2. If the linked list is empty, return None
    3. If the linked list has only one node, return None
    4. Initialize a variable current to head
    5. Loop through each node in the linked list until current.next is None
    6. Set current.next to None
    7. Return head
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def remove_tail(head):
        if head is None:
            return None
        if head.next is None:
            return None
        
        current = head
        while current.next.next is not None:
            current = current.next
        
        current.next = None
        return head
    
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    head = Node("Isabelle", Node("Alfonso", Node("Cyd")))
    print_linked_list(remove_tail(head))

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
    '''

# Problem 3: Delete Duplicates in a Linked List
'''
Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). 
The resulting list should maintain sorted order. Return the head of the linked list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity
'''
def problem_3():
    #U:
    '''
    What if the linked list is empty?
    What if the linked list has only one node?
    '''
    #P:
    '''
    1. Define a function delete_duplicates that accepts the head of a linked list
    2. If the linked list is empty, return None
    3. If the linked list has only one node, return head
    4. Initialize a variable current to head
    5. Loop through each node in the linked list until current.next is None
    6. If the value of the current node is equal to the value of the next node, set current.next to current.next.next
    7. Otherwise, update current to current.next
    8. Return head
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def delete_duplicates(head):
        if head is None:
            return None
        if head.next is None:
            return head
        
        current = head
        while current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
    
    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
    print_linked_list(delete_duplicates(head))

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
    '''

###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)