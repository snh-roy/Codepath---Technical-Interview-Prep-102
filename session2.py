# Problem 1: Transpose Matrix
'''
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
'''
def problem_1():
    #U:
    '''
    What if the matrix is empty?
    What if the matrix is not a square matrix (aka unequal len of 2D lists)?
    '''
    #P:
    '''
    1. Define a function transpose() that accepts a 2D integer array matrix
    2.loop through each row in the matrix
    3. swap the rows and columns
    4. return the transposed matrix

    '''
    #I:
    def transpose(matrix):
        rows, cols = len(matrix), len(matrix[0])  
        transposed = [[0] * rows for _ in range(cols)]  

        for j in range(rows):  
            for i in range(cols):  
                transposed[i][j] = matrix[j][i] 

        return transposed
    
    matrix1 = [[1, 2, 3], [4, 5, 6],  [7, 8, 9]]
    print(transpose(matrix1))

    matrix2= [[1]]
    print(transpose(matrix2))



# Problem 2: Two-Pointer Reverse List
'''
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. 
The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
Instead, use the two-pointer approach, which is a common technique in which we initialize two variables 
(also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers 
to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, 
we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. 
We then shift the pointers to move inwards through the list towards each other, until our problem is solved or 
the pointers reach the opposite ends of the list.
'''

def problem_2():
    #U:
    '''
    What if the list is empty?
    What if the list has only one element?
    '''
    #P:
    '''
    1. Define a function that accepts a list lst
    2. Initialize two pointers left and right to the first and last index of lst
    3. Loop through the list until left is less than right
    4. Swap the elements at the left and right pointers
    5. Increment left and decrement right
    6. Return the reversed list
    7. If the list is empty, return an empty list
    8. If the list has only one element, return the list
    '''
    #I:
    def reverse_list(lst:list) -> list:
        left_pointer, right_pointer = 0, len(lst) - 1
        while left_pointer < right_pointer:
            lst[left_pointer], lst[right_pointer] = lst[right_pointer], lst[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        return lst

    lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
    print(reverse_list(lst))
    
    lst1 = [1, 2, 3, 4, 5]
    print(reverse_list(lst1))

    lst2 = [1]
    print(reverse_list(lst2))


# Problem 3: Squash Spaces
'''
Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring 
with consecutive spaces reduced to a single space. 
Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.
'''

def problem_3():
    #U:
    '''
    What if the string is empty?
    What if the string has no spaces at all?
    '''
    #P:
    '''
    1. Define a function that accepts a string s
    2. Initialize a variable result to an empty string
    3. Initialize a variable space to False
    4. Loop through each character in s
    5. If the character is not a space, add it to result
    6. If the character is a space, check if space is False
    7. If space is False, add the space to result and set space to True
    8. If space is True, continue to the next character
    9. Return the result
    10. If the string is empty, return an empty string
    11. If the string has no spaces, return the string
    '''
    #I:
    def squash_spaces(s:str) -> str:
        result = ""
        space = False
        for char in s:
            if char != " ":
                result += char
                space = False
            elif not space:
                result += char
                space = True
        return result
    
    s = "Up,         up,   and  away! "
    print(squash_spaces(s))

    s = "With great power comes great responsibility."
    print(squash_spaces(s))



###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)