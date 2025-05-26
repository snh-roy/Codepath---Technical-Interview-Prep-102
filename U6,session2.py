#Problem 1: Next in Queue
'''
Each user on a music app should have a queue of songs to play next. Implement the class Queue using a singly linked list. Recall that a queue is a First-In-First-Out (FIfO) data structure where elements are added to the end (the tail) and removed from the front (the head).
Your queue must have the following methods:

__init()__: Initializes an empty queue (provided)
enqueue(): Accepts a tuple of two strings (song, artist) and adds the element with the specified tuple to the end of the queue.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty, returns None.
peek(): Returns the value of the element at the front of the queue without removing it. If the queue is empty, returns None.
is_empty(): Returns True if the queue is empty, and False otherwise.
'''
def problem_1():   
    #U:
    '''
    What if the queue is empty?
    '''
    #P:
    '''
    1. Define a class Queue
    2. Define the __init__ method that initializes an empty queue
    3. Define the enqueue method that accepts a tuple of two strings (song, artist) and adds the element with the specified tuple to the end of the queue
    4. Define the dequeue method that removes and returns the element at the front of the queue. If the queue is empty, return None
    5. Define the peek method that returns the value of the element at the front of the queue without removing it. If the queue is empty, return None
    6. Define the is_empty method that returns True if the queue is empty, and False otherwise
    '''
    #I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
        
        def print_queue(head):
            current = head.front
            while current:
                print(current.value, end=" -> " if current.next else "")
                current = current.next
            print()

        class Queue:
            def __init__(self):
                self.front = None
                self.rear = None
            
            def is_empty(self):
                return self.front is None

            def enqueue(self):
                return self.front
            
            def dequeue(self):
                return self.front
            
            def peek(self):
                return self.front
            
        # Create a new Queue
        q = Queue()

        # Add elements to the queue
        q.enqueue(('Love Song', 'Sara Bareilles'))
        q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
        q.enqueue(('Hug from a Dinosaur', 'Torres'))
        print_queue(q)

        # View the front element
        print("Peek: ", q.peek()) 

        # Remove elements from the queue
        print("Dequeue: ", q.dequeue()) 
        print("Dequeue: ", q.dequeue()) 

        # Check if the queue is empty
        print("Is Empty: ", q.is_empty()) 

        # Remove the last element
        print("Dequeue: ", q.dequeue()) 

        # Check if the queue is empty
        print("Is Empty:", q.is_empty()) 
            
#Problem 2: Merge Playlists
'''
You are given the head of two linked lists, playlist1 and playlist2 with lengths n and m respectively. 
Remove playlist1's nodes from the ath to the bth node and put playlist2 in its place. Assume the lists are 0-indexed.
The blue edges and nodes in the figure below indicate the result:
'''

def problem_2():
    #U:
    '''
    What if the linked list is empty?
    What if the linked list has only one node?
    '''
    #P:
    '''
    1. Define a function merge_playlists that accepts the head of two linked lists, playlist1 and playlist2, and integers a and b
    2. If playlist1 is empty, return playlist2
    3. If playlist2 is empty, return playlist1
    4. Initialize a variable current to playlist1
    5. Loop through each node in playlist1 until the ath node
    6. Initialize a variable temp to the current node
    7. Loop through each node in playlist1 from the ath to the bth node
    8. Update current to current.next
    9. Set temp.next to playlist2
    10. Loop through each node in playlist2 until the last node
    11. Update temp to temp.next
    12. Set temp.next to current.next
    13. Return playlist1
    '''
    #I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        # For testing
        def print_linked_list(head):
            current = head
            while current:
                print(current.value, end=" -> " if current.next else "")
                current = current.next
            print()

        def merge_playlists(playlist1, playlist2, a, b):
            if playlist1 is None:
                return playlist2
            if playlist2 is None:
                return playlist1

            current = playlist1
            for _ in range(a - 1):
                current = current.next

            temp = current
            for _ in range(b - a + 1):
                current = current.next

            temp.next = playlist2

            while temp.next:
                temp = temp.next

            temp.next = current.next

            return playlist1
        
    playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

    playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))
    print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))


#Problem 3: Shuffle Playlist
'''
You are given the head of a singly linked list playlist. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Shuffle the playlist to have the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only the order of the nodes themselves may be changed. Return the head of the shuffled list.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity.
'''

def problem_3():
    #U:
    '''
    What if the linked list is empty?
    What if the linked list has only one node?
    '''
    #P:
    '''
    1. Define a function shuffle_playlist that accepts the head of a linked list playlist
    2. If the linked list is empty, return None
    3. If the linked list has only one node, return head
    4. Initialize a variable slow to head
    5. Initialize a variable fast to head
    6. Loop through the linked list until fast.next is None and fast.next.next is None
    7. Update slow to slow.next
    8. Update fast to fast.next.next
    9. Initialize a variable second_half to slow.next
    10. Set slow.next to None
    11. Reverse the second_half of the linked list
    12. Merge the first half and the reversed second half of the linked list
    13. Return head
    '''
    #I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        # For testing
        def print_linked_list(head):
            current = head
            while current:
                print(current.value, end=" -> " if current.next else "")
                current = current.next
            print()

        def shuffle_playlist(head):
            if head is None:
                return None
            if head.next is None:
                return head

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next
            slow.next = None

            def reverse_linked_list(node):
                prev = None
                current = node
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                return prev

            second_half = reverse_linked_list(second_half)

            def merge_linked_lists(list1, list2):
                current = list1
                while list1 and list2:
                    next_list1 = list1.next
                    next_list2 = list2.next

                    list1.next = list2
                    list2.next = next_list1

                    list1 = next_list1
                    list2 = next_list2

            merge_linked_lists(head, second_half)

            return head
        


    
    playlist1 = Node(1, Node(2, Node(3, Node(4))))
    playlist2 = Node(('Respect', 'Aretha Franklin'),
        Node(('Superstition', 'Stevie Wonder'),
            Node(('Wonderwall', 'Oasis'),
                Node(('Like a Prayer', 'Madonna'),
                    Node(('Bohemian Rhapsody', 'Queen'))))))
    

    print_linked_list(shuffle_playlist(playlist1))
    print_linked_list(shuffle_playlist(playlist2))


########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)
