# Problem 4: Return Item
'''
    Implement a function get_item() that accepts a 0-indexed list items and 
    a non-negative integer x and returns the element at index x in items. 
    If x is not a valid index of items, return None
    '''
def problem_1():

    #U:
    '''
    Is items an empty list?
    What is x is equal to the length of items?
   '''

    #P:
    '''
    1. Define a function get_item() that accepts a 0-indexed list items and a non-negative integer x.
    2. Check if x is less than the length of items. 
    3. If x is less than the length of items, return the element at index x in items.
    4. If x is not a valid index of items, return None.
    '''
    #I:
    def get_item(items:list, x:int):
        if x < len(items):
            return items[x]
        else:
            return None 
            

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 1
    print(get_item(items, x))


# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
'''
bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, 
return the final value of tigger after performing all the operations.
'''

def problem_2():
    #U:
    '''
    What if the list of operations is empty?
    How do we keep track of tigger?
    '''
    #P:
    '''
    1. Define a function that accepts a list of strings operations
    2. Initialize a variable tigger to 1
    3. Loop through each operation in operations
    4. If the operation is "bouncy" or "flouncy", increment tigger by 1
    5. If the operation is "trouncy" or "pouncy", decrement tigger by 1
    6. Return the final value of tigger
    7. If the list of operations is empty, return 1
    '''
    # I:
    def final_value_after_operations(operations:list) -> int:
        if not operations:
            return 1
        
        tigger = 1  
        for i in operations:
            if i in ["bouncy", "flouncy"]:
                tigger += 1
            elif i in ["trouncy", "pouncy"]:
                tigger -= 1
        return tigger

    operations1 = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations1))  

    operations2 = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations2))  

# Problem 4: Non-decreasing Array
    '''
    Given an array nums with n integers, write a function non_decreasing() 
    that checks if nums could become non-decreasing by modifying at most one element.
    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
    such that (0 <= i <= n - 2
    '''
def problem_3():
    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    '''
    #P:
    '''
    1. Define a function that accepts an array nums with n integers
    2. Initialize a variable count to 0
    3. Loop through each element in nums
    4. If the current element is greater than the next element, increment count by 1 
    5. If count is greater than 1, return False
    6. If count is less than or equal to 1, return True
    7. If the array is empty, return True
    8. If the array has only one element, return True
    '''
    #I:
    def non_decreasing(nums:list) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
        return count <= 1
    
    nums1 = [4, 2, 3]
    print(non_decreasing(nums1)) 

    nums2 = [4, 2, 1]
    print(non_decreasing(nums2))

    nums3 = [3]
    print(non_decreasing(nums3))

    num4 = []
    print(non_decreasing(num4))


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)