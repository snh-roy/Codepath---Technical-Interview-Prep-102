# Problem 1: Blueprint Approval Process
'''
You are in charge of overseeing the blueprint approval process for various architectural designs. 
Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, 
the approval process follows a strict order:

Blueprints with lower complexity should be reviewed first.
If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

Return the order in which the blueprints are approved.
'''
def problem_1():
    #U:
    '''
    What if the list of blueprints is empty?
    How do we keep track of the order in which blueprints are approved?
    '''
    #P:
    '''
    1. Define a function that accepts a list of integers blueprints
    2. Initialize a queue
    3. Loop through each blueprint in blueprints
    4. If the queue is empty, append the blueprint to the queue
    5. If the queue is not empty, insert the blueprint at the correct position in the queue
    6. Return the queue
    7. If the list of blueprints is empty, return an empty queue
    '''
    # I:
    def blueprint_approval(blueprints:list) -> list:
        if not blueprints:
            return []
        
        queue = []
        for i in blueprints:
            if not queue:
                queue.append(i)
            else:
                for j in range(len(queue)):
                    if i < queue[j]:
                        queue.insert(j, i)
                        break
                else:
                    queue.append(i)
        return queue 

    print(blueprint_approval([3, 5, 2, 1, 4])) 
    print(blueprint_approval([7, 4, 6, 2, 5])) 

# Problem 2: Build the Tallest Skyscraper
'''
You are given an array floors representing the heights of different building floors. 
Your task is to design a skyscraper using these floors, where each floor must be placed on
top of a floor with equal or greater height. However, you can only start a new skyscraper when necessary, 
meaning when no more floors can be added to the current skyscraper according to the rules.

Return the number of skyscrapers you can build using the given floors.
'''
def problem_2():
    #U:
    '''
    What if the array is empty?
    How do we keep track of the number of skyscrapers built?
    '''
    #P:
    '''
    1. Define a function that accepts an array floors with n integers
    2. Initialize a variable count to 0
    3. Initialize a variable current_height to 0
    4. Loop through each floor in floors
    5. If the current floor is greater than or equal to the current height, increment count by 1
    6. Set the current height to the current floor
    7. Return the count
    8. If the array is empty, return 0
    '''
    #I:
    def build_skyscrapers(floors: list) -> int:
        if not floors:
            return 0

        count = 1  
        for i in range(1, len(floors)):
            if floors[i] >= floors[i - 1]: 
                count += 1

        return count

    print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) #4
    print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  #4
    print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))  #6


#Problem 3: Dream Corridor Design
'''
You are an architect designing a corridor for a futuristic dream space. 
The corridor is represented by a list of integer values where each value represents
the width of a segment of the corridor. Your goal is to find two segments such that 
the corridor formed between them (including the two segments) has the maximum possible area.
 The area is defined as the minimum width of the two segments multiplied by the distance between them.

You need to return the maximum possible area that can be achieved.
'''
def problem_3():
    #U:
    '''
    What if the list of widths is empty?
    How do we keep track of the maximum area?
    '''
    #P:
    '''
    1. Define a function that accepts a list of integers widths
    2. Initialize a variable max_area to 0
    3. Loop through each width in widths
    4. Loop through each width in widths starting from the current width
    5. Calculate the area between the two widths
    6. If the area is greater than the max_area, update max_area
    7. Return max_area
    8. If the list of widths is empty, return 0
    '''
    #I:
    def max_corridor_area(widths:list) -> int:
        if not widths:
            return 0

        max_area = 0
        for i in range(len(widths)):
            for j in range(i, len(widths)):
                area = min(widths[i], widths[j]) * (j - i)
                if area > max_area:
                    max_area = area

        return max_area

    print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
    print(max_corridor_area([1, 1])) 


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)