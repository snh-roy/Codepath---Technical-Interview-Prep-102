# Problem 1: Selective DNA Deletion
'''
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. 
Each nucleotide in the sequence is represented as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.
Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from the current position. - Remove the next n nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.
Return the head of the modified DNA sequence after removing the mentioned nucleotides.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale 
for why you believe your solution has the stated time and space complexity
'''

def problem_1():
    #U:
    '''
    What if the linked list is empty?
    What if m is greater than the length of the linked list?
    '''
    #P:
    '''
    1. Define a function edit_dna_sequence that accepts the head of a linked list dna_strand, and two integers m and n
    2. If the linked list is empty, return None
    3. Initialize a variable current to head
    4. Loop through each node in the linked list until current is None
    5. Initialize a variable m_count to 0
    6. Initialize a variable n_count to 0
    7. Initialize a variable m_flag to True
    8. Initialize a variable n_flag to False
    9. Initialize a variable m_head to None
    10. Initialize a variable m_tail to None
    11. Initialize a variable n_head to None
    12. Initialize a variable n_tail to None
    13. Loop through each node in the linked list until current is None
    14. If m_count is less than m and m_flag is True, append the current node to m_head and update m_tail to current
    15. If m_count is equal to m and m_flag is True, set m_flag to False
    16. If m_count is equal to m and n_count is less than n and n_flag is False, append the current node to n_head and update n_tail to current
    17. If n_count is equal to n and n_flag is False, set n_flag to True
    18. If m_count is equal to m and n_count is equal to n and n_flag is True, set m_count to 0, n_count to 0, m_flag to True, n_flag to False, and set m_tail.next to n_tail.next
    19. If m_flag is True, increment m_count by 1
    20. If n_flag is True, increment n_count by 1
    21. Update current to current.next
    22. Return m_head
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def print_linked_list(head):
        current = head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def edit_dna_sequence(dna_strand, m, n):
        if dna_strand is None:
            return None
        
        current = dna_strand
        m_count = 0
        n_count = 0
        m_flag = True
        n_flag = False
        m_head = None
        m_tail = None
        n_head = None
        n_tail = None
        
        while current is not None:
            if m_count < m and m_flag:
                if m_head is None:
                    m_head = current
                if m_tail is not None:
                    m_tail.next = current
                m_tail = current
            if m_count == m and m_flag:
                m_flag = False
            if m_count == m and n_count < n and not n_flag:
                if n_head is None:
                    n_head = current
                if n_tail is not None:
                    n_tail.next = current
                n_tail = current
            if n_count == n and not n_flag:
                n_flag = True
            if m_count == m and n_count == n and n_flag:
                m_count = 0
                n_count = 0
                m_flag = True
                n_flag = False
                m_tail.next = n_tail.next
            if m_flag:
                m_count += 1
            if n_flag:
                n_count += 1
            current = current.next
        
        return m_head
    
    dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))
    print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
    '''

# Problem 2: Protein Folding Loop Detection
'''
As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. 
These proteins sometimes fold back on themselves, creating loops that can impact their function.
Given the head of a linked list protein where each node in the linked list represents an amino acid in the protein, return an array with the values of any cycle in the list. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.
The values may be returned in any order.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.
'''
def problem_2():
    #U:
    '''
    What if the linked list is empty?
    What if the linked list has only one node?
    '''
    #P:
    '''
    1. Define a function find_cycle that accepts the head of a linked list protein
    2. If the linked list is empty, return an empty list
    3. If the linked list has only one node, return an empty list
    4. Initialize a variable slow to head
    5. Initialize a variable fast to head
    6. Loop through each node in the linked list until fast is None
    7. Update slow to slow.next
    8. Update fast to fast.next.next
    9. If slow is equal to fast, break
    10. If fast is None, return an empty list
    11. Initialize a variable cycle to an empty list
    12. Update slow to head
    13. Loop through each node in the linked list until slow is equal to fast
    14. Append the value of slow to cycle
    15. Update slow to slow.next
    16. Update fast to fast.next
    17. Return cycle
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def cycle_length(protein):
            slow = protein
            fast = protein
            while fast is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
            if fast is None:
                return 0
            cycle = []
            slow = protein
            while slow != fast:
                cycle.append(slow.value)
                slow = slow.next
                fast = fast.next
            cycle.append(slow.value)
            return cycle
    
    protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
    protein_head.next.next.next.next = protein_head.next 

    print(cycle_length(protein_head))
    
        #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
        '''

# Problem 3: Segmenting Protein Chains for Analysis
'''
As a biochemist, you are analyzing a long protein chain represented by a singly linked list, where each node is an amino acid. 
For a specific experiment, you need to split this protein chain into k consecutive segments for separate analysis.
Each segment should be as equal in length as possible, with no two segments differing in size by more than one amino acid.
The segments should appear in the same order as the original protein chain, and segments earlier in the list should have a size greater 
than or equal to those occurring later. If the protein chain cannot be evenly divided, some segments may be an empty list.
Write a function split_protein_chain() that takes the head of the linked list protein and an integer k, and returns an array of k segments.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has 
the stated time and space complexity.
'''
def problem_3():
    #U:
    '''
    What if the linked list is empty?
    What if k is less than or equal to 0?
    '''
    #P:
    '''
    1. Define a function split_protein_chain that accepts the head of a linked list protein and an integer k
    2. If the linked list is empty, return an array of k empty lists
    3. If k is less than or equal to 0, return an array of k empty lists
    4. Initialize a variable current to head
    5. Initialize a variable length to 0
    6. Loop through each node in the linked list until current is None
    7. Increment length by 1
    8. Update current to current.next
    9. Initialize a variable segment_length to length // k
    10. Initialize a variable remaining to length % k
    11. Initialize a variable segments to an array of k empty lists
    12. Update current to head
    13. Loop through each segment in segments
    14. Initialize a variable segment_head to current
    15. Initialize a variable segment_tail to None
    16. Loop through each node in the linked list until current is None
    17. If segment_length is greater than 0, decrement segment_length by 1
    18. If segment_length is equal to 0 and remaining is greater than 0, decrement remaining by 1
    19. If segment_length is equal to 0 and remaining is equal to 0, set segment_tail to current
    20. Update current to current.next
    21. If segment_tail is not None, set segment_tail.next to None
    22. Append segment_head to segment_tail to segments
    23. Return segments
    '''
    # I:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
        
        def print_linked_list(head):
            if not head:
                print("Empty List")
                return
            current = head
            while current:
                print(current.value, end=" -> " if current.next else "\n")
                current = current.next
                

        def split_protein_chain(protein, k):
            if protein is None:
                return [[] for _ in range(k)]
            if k <= 0:
                return [[] for _ in range(k)]
            
            current = protein
            length = 0
            while current is not None:
                length += 1
                current = current.next
            
            segment_length = length

#Example:
    protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
    protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

    parts = split_protein_chain(protein1, 3)
    for part in parts:
        print_linked_list(part)

    parts = split_protein_chain(protein2, 5)
    for part in parts:
        print_linked_list(part)
    
    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each node in the linked list,
    where n is the number of nodes in the linked list.
    '''


########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)