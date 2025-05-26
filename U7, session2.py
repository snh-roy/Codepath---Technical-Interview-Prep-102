#Problem 1: Find Millenium Falcon Part
'''
Han Solo's ship, the Millenium Falcon, has broken down and he's searching for a specific replacement part. 
As a repair shop owner helping him out, write a function check_stock() that takes in a list inventory where 
each element is an integer ID of a part you stock in your shop, and an integer part_id representing the integer ID of
the part Han Solo is looking for. Return True if the part_id is in inventory and False otherwise.
Your solution must have O(log n) time complexity.
'''

def problem_1():
    #U:
    '''
    1. What if the inventory list is empty?
    2. What if the inventory list has only one part?
    '''
    #P:
    '''
    1. Define a function check_stock that accepts a list inventory and an integer part_id
    2. If the inventory list is empty, return False
    3. If the inventory list has only one part, return True if the part_id is equal to the part in the inventory list and False otherwise
    4. Initialize a variable low to 0
    5. Initialize a variable high to the length of the inventory list minus 1
    6. Loop while low is less than or equal to high
    7. Initialize a variable mid to the average of low and high
    8. If the part_id is equal to the part at index mid, return True
    9. If the part_id is less than the part at index mid, set high to mid minus 1
    10. Otherwise, set low to mid plus 1
    11. Return False
    '''
    #I:
    def check_stock(inventory, part_id):
        if not inventory:
            return False

        if len(inventory) == 1:
            return part_id == inventory[0]

        low = 0
        high = len(inventory) - 1

        while low <= high:
            mid = (low + high) // 2

            if part_id == inventory[mid]:
                return True
            if part_id < inventory[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False
    print(check_stock([1, 2, 5, 12, 20], 20))
    print(check_stock([1, 2, 5, 12, 20], 100))

    #RE:
    ''' The time complexity is O(log n) because we are using binary search to find the part_id in the inventory list. The space complexity is O(1) because we are using a constant amount of space.'''

#Problem 2: Find Millenium Falcon Part II
'''
If you implemented your check_stock() function from the previous problem iteratively, implement it recursively.'''

def problem_2():
    #I:
    def check_stock(inventory, part_id):
        def binary_search(low, high):
            if low > high:
                return False

            mid = (low + high) // 2

            if part_id == inventory[mid]:
                return True
            if part_id < inventory[mid]:
                return binary_search(low, mid - 1)
            return binary_search(mid + 1, high)

        return binary_search(0, len(inventory) - 1)
    
    print(check_stock([1, 2, 5, 12, 20], 20))
    print(check_stock([1, 2, 5, 12, 20], 100))

    #RE:
    ''' The time complexity is O(log n) because we are using binary search to find the part_id in the inventory list. The space complexity is O(log n) because the recursive calls will be stored in the call stack until the base case is reached.'''

#Problem 3: Find First and Last Frequency Positions
'''
The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire. 
Each transmission is marked with a unique frequency code, represented as integers, 
and these codes are stored in a sorted array transmissions. As a skilled codebreaker for the Rebellion, 
write a function find_frequency_positions() that returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. 
If target_code does not exist in transmissions, return (-1, -1).

Your solution must have O(log n) time complexity.
'''

def problem_3(): 
    #U:
    '''
    1. What if the transmissions list is empty?
    2. What if the transmissions list has only one frequency code?
    '''
    #P:
    '''
    1. Define a function find_frequency_positions that accepts a list transmissions and an integer target_code
    2. If the transmissions list is empty, return (-1, -1)
    3. If the transmissions list has only one frequency code, return (0, 0) if the frequency code is equal to the target_code and (-1, -1) otherwise
    4. Initialize a variable low to 0
    5. Initialize a variable high to the length of the transmissions list minus 1
    6. Initialize a variable first to -1
    7. Initialize a variable last to -1
    8. Loop while low is less than or equal to high
    9. Initialize a variable mid to the average of low and high
    10. If the target_code is equal to the frequency code at index mid, set first to mid and last to mid
    11. If the target_code is less than the frequency code at index mid, set high to mid minus 1
    12. Otherwise, set low to mid plus 1
    13. Return a tuple with first and last
    '''
    #I:
    def find_frequency_positions(transmissions, target_code):
        if not transmissions:
            return (-1, -1)

        if len(transmissions) == 1:
            return (0, 0) if transmissions[0] == target_code else (-1, -1)

        low = 0
        high = len(transmissions) - 1
        first = -1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if target_code == transmissions[mid]:
                first = mid
                last = mid
            if target_code < transmissions[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return (first, last)
    print(find_frequency_positions([5,7,7,8,8,10], 8))
    print(find_frequency_positions([5,7,7,8,8,10], 6))
    print(find_frequency_positions([], 0))      

    #RE:
    ''' The time complexity is O(log n) because we are using binary search to find the first and last indices of the target_code in the transmissions list. 
    The space complexity is O(1) because we are using a constant amount of space.'''

########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)
