# Problem 3: Find All Duplicate Treasure Chests in an Array
'''
Captain Blackbeard has an integer array chests of length n 
where all the integers in chests are in the range [1, n] and
 each integer appears once or twice. Return an array of all the
integers that appear twice, representing the treasure chests that have duplicates
'''

def problem_1():
    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    '''

    #P:
    '''
    1. Define a function that accepts an array chests of length n
    2. Initialize an empty list duplicates
    3. Initialize an empty dictionary chest_count
    4. Loop through each element in chests
    5. If the element is not in chest_count, add it to chest_count with a value of 1
    6. If the element is in chest_count, increment the value by 1
    7. Loop through each key, value pair in chest_count
    8. If the value is equal to 2, add the key to duplicates
    9. Return duplicates
    10. If the array is empty, return an empty list
    11. If the array has only one element, return an empty list
    '''

    #I:
    def find_duplicate_chests(chests:list) -> list:
        duplicates = []
        chest_count = {}
        for i in chests:
            if i not in chest_count:
                chest_count[i] = 1
            else:
                chest_count[i] += 1
        for key, value in chest_count.items():
            if value == 2:
                duplicates.append(key)
        return duplicates
    
    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))

# Problem 5: Overflowing With Gold
'''
Given an array of integers gold_amounts representing 
the amount of gold at each location and an integer target, 
return the indices of the two locations whose gold amounts add up to the target
'''

def problem_2():
    #U:
    '''
    What if there are no two locations whose gold amounts add up to the target?
    '''

    #P:
    '''
    1. Define a function that accepts an array gold_amounts and an integer target
    2. Initialize an empty dictionary gold_map
    3. Loop through each index, value pair in gold_amounts
    4. Calculate the difference between the target and the value
    5. If the difference is in gold_map, return the indices of the current index and the index of the difference
    6. If the difference is not in gold_map, add the value to gold_map with the index as the value
    7. If there are no two locations whose gold amounts add up to the target, return an empty list
    '''

    #I:
    def find_treasure_indices(gold_amounts:list, target:int) -> list:
        gold_map = {}
        for i, gold in enumerate(gold_amounts):
            diff = target - gold
            if diff in gold_map:
                return [gold_map[diff], i]
            gold_map[gold] = i
        return []

    gold_amounts1 = [2, 7, 11, 15]
    target1 = 9

    gold_amounts2 = [3, 2, 4]
    target2 = 6

    gold_amounts3 = [3, 3]
    target3 = 6

    print(find_treasure_indices(gold_amounts1, target1))
    print(find_treasure_indices(gold_amounts2, target2))
    print(find_treasure_indices(gold_amounts3, target3))


#Problem 6: Organize the Pirate Crew
'''
You are given an integer array group_sizes,
where group_sizes[i] is the size of the group that pirate i should be in. 
For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.
Return a list of groups such that each pirate i is in a group of size group_sizes[i].
Each pirate should appear in exactly one group, and every pirate must be in a group. 
If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
'''

def problem_3():

    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    '''

    #P:
    '''
    1. Define a function that accepts an array group_sizes
    2. Initialize an empty dictionary groups
    3. Loop through each index, size pair in group_sizes
    4. If the size is not in groups, add it to groups with an empty list as the value
    5. Append the index to the list of the corresponding size
    6. Loop through each key, value pair in groups
    7. If the length of the value is not equal to the key, return an empty list
    8. Return the values of groups
    9. If the array is empty, return an empty list
    10. If the array has only one element, return an empty list
    '''

    #I:
    def organize_pirate_crew(group_sizes:list) -> list:
        groups = {}
        for i, size in enumerate(group_sizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
        for size, pirates in groups.items():
            if len(pirates) != size:
                return []
        return list(groups.values())

    group_sizes1 = [3, 3, 3, 3, 3, 1, 3] 
    group_sizes2 = [2, 1, 3, 3, 3, 2]

    print(organize_pirate_crew(group_sizes1)) #[[5], [0, 1, 2], [3, 4, 6]]
    print(organize_pirate_crew(group_sizes2)) #[[1], [0, 5], [2, 3, 4]]


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)