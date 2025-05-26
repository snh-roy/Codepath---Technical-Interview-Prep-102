# Problem 1: Arrange Guest Arrival Order
'''
The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I'
meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should 
have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:
guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
'''
def problem_1():
    #U:
    '''
    What if the arrival_pattern is empty?
    What if the arrival_pattern has only one element?
    '''
    #P:
    '''
    1. Define a function that accepts a string arrival_pattern of length n  
    2. Initialize a variable guest_order to an empty list
    3. Initialize a variable current_guest to 0
    4. Loop through each character in arrival_pattern
    5. If the current character is 'I', append current_guest to guest_order and increment current_guest by 1
    6. If the current character is 'D', append current_guest to guest_order and decrement current_guest by 1
    7. Append the final value of current_guest to guest_order
    8. Return guest_order
    '''
    # I:
    def arrange_guest_arrival_order(arrival_pattern):
        if not arrival_pattern:
            return []
        
        guest_order = []
        current_guest = 1
        for i in arrival_pattern:
            if i == 'I':
                guest_order.append(current_guest)
                current_guest += 1
            elif i == 'D':
                guest_order.append(current_guest)
                current_guest -= 1
        guest_order.append(current_guest)
        return guest_order
    
    print(arrange_guest_arrival_order("IIIDIDDD"))  #123549876 
    print(arrange_guest_arrival_order("DDD"))  #3210

# Problem 2: Reveal Attendee List in Order
'''
ou are organizing an event where attendees have unique registration numbers. 
These numbers are provided in the list attendees. You need to arrange the attendees 
in a way that, when their registration numbers are revealed one by one, the numbers appear in increasing order.
The process of revealing the attendee list follows these steps repeatedly until all registration numbers are revealed:
Take the top registration number from the list, reveal it, and remove it from the list.
If there are still registration numbers in the list, take the next top registration number and move it to the bottom of the list.
If there are still unrevealed registration numbers, go back to step 1. Otherwise, stop.
Return an ordering of the registration numbers that would reveal the attendees in increasing order.
'''
def problem_2():
    #U:
    ''' 
    What if the list of attendees is empty?
    '''
    #P:
    '''
    1. Define a function that accepts a list of integers attendees
    2. Initialize an empty list revealed_order
    3. Loop through each attendee in attendees
    4. Append the current attendee to revealed_order
    5. If there are still attendees in the list, move the next attendee to the end of the list
    6. Return revealed_order
    7. If the list of attendees is empty, return []
    '''
    # I:
    def reveal_attendee_list_in_order(attendees):
        if not attendees:
            return []
        
        revealed_order = []
        while attendees:
            revealed_order.append(attendees.pop(0))
            if attendees:
                attendees.append(attendees.pop(0))
        return revealed_order
    print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) #17,13,11,2,3,5,7
    print(reveal_attendee_list_in_order([1,1000])) #1,1000 

# Problem 3: Arrange Event Attendees by Priority
'''
You are organizing a large event and need to arrange the attendees based on their priority levels.
 You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, 
 and an integer priority that indicates a particular level of priority.

Your task is to rearrange the attendees list such that the following conditions are met:

Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
Return the attendees list after the rearrangement.
'''
def problem_3():
    #U: 
    '''
    What if the list of attendees is empty?
    '''
    #P:
    ''' 
    1. Define a function that accepts a list of integers attendees and an integer priority
    2. Initialize an empty list priority_order
    3. Loop through each attendee in attendees
    4. If the current attendee is less than the priority, append the current attendee to priority_order
    5. Loop through each attendee in attendees
    6. If the current attendee is equal to the priority, append the current attendee to priority_order
    7. Loop through each attendee in attendees
    8. If the current attendee is greater than the priority, append the current attendee to priority_order
    9. Return priority_order
    10. If the list of attendees is empty, return []
    '''
    # I:
    def arrange_attendees_by_priority(attendees, priority):
        if not attendees:
            return []
        
        priority_order = []
        for i in attendees:
            if i < priority:
                priority_order.append(i)
        for i in attendees:
            if i == priority:
                priority_order.append(i)
        for i in attendees:
            if i > priority:
                priority_order.append(i)
        return priority_order

    print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) #[9,5,3,10,10,12,14]
    print(arrange_attendees_by_priority([-3,4,3,2], 2)) #[-3,4,3,2]


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)