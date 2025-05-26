# Problem 1: Get Flight Cost
'''
You are given an adjacency dictionary flights where for any location source, flights[source] is a list of tuples in the form (destination, cost) 
indicating that there exists a flight from source to destination at ticket price cost.
Given a starting location start and a final destination dest return the total cost of flying from start to dest. If it is not possible to fly from start to dest, 
return -1. If there are multiple possible paths from start to dest, return any of the possible answers.
'''

def problem_1():
    #U:
    '''
    What is the input?
    What is the output?
    What is the input format?
    What is the output format?
    '''
    #P:
    '''
    1. Create a set to hold the visited airports.
    2. Create a queue to hold the airports to visit.
    3. Add the starting airport to the queue.
    4. While the queue is not empty, pop an airport from the queue.
    5. If the airport has not been visited, add it to the visited set.
    6. Add all unvisited destinations from the current airport to the queue.
    7. Return the visited set as a sorted list.
    '''
    # I:
    from collections import deque
    def calculate_cost(flights, start, dest):
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            airport, cost = queue.popleft()
            if airport == dest:
                return cost
            if airport not in visited:
                visited.add(airport)
                for destination, ticket_cost in flights.get(airport, []):
                    if destination not in visited:
                        queue.append((destination, cost + ticket_cost))
        return -1
    
    flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW': 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

    print(calculate_cost(flights, 'LAX', 'MIA'))

# Problem 2: Expanding Flight Offerings
'''
CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to reach all other airports. 
They track their current flight offerings in an adjacency dictionary flights where each key is an airport i and flights[i] is an array indicating that 
there is a flight from destination i to each destination in flights[i]. Assume that if there is flight from airport i to airport j, the reverse is also true.
Given flights, return the minimum number of flights (edges) that need to be added such that there is flight path from each airport in flights to every other airport.
'''

def problem_2():
    #U:
    '''
    What is the input?
    What is the output?
    What is the input format?
    What is the output format?
    '''
    #P:
    '''
    1. Create a set to hold the visited airports.
    2. Create a queue to hold the airports to visit.
    3. Add the starting airport to the queue.
    4. While the queue is not empty, pop an airport from the queue.
    5. If the airport has not been visited, add it to the visited set.
    6. Add all unvisited destinations from the current airport to the queue.
    7. Return the visited set as a sorted list.
    '''

    # I:
    from collections import deque
    def min_flights_to_expand(flights):
        visited = set()
        queue = deque()
        for airport in flights:
            if airport not in visited:
                queue.append(airport)
                while queue:
                    current_airport = queue.popleft()
                    if current_airport not in visited:
                        visited.add(current_airport)
                        for destination in flights.get(current_airport, []):
                            if destination not in visited:
                                queue.append(destination)
        return len(flights) - len(visited)
    
    flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

    print(min_flights_to_expand(flights))

# Problem 3: Get Flight Itinerary
    
'''
Given an adjacency dictionary of flights flights where each key is an airport i and flights[i] is an array indicating that there is a flight from destination 
i to each destination in flights[i], return an array with the flight path from a given source location to a given destination location.
If there are multiple flight paths from the source to destination, return any flight path.
'''

def problem_3():
    #U:
    '''
    What is the input?
    What is the output?
    What is the input format?
    What is the output format?
    '''
    #P:
    '''
    1. Create a set to hold the visited airports.
    2. Create a queue to hold the airports to visit.
    3. Add the starting airport to the queue.
    4. While the queue is not empty, pop an airport from the queue.
    5. If the airport has not been visited, add it to the visited set.
    6. Add all unvisited destinations from the current airport to the queue.
    7. Return the visited set as a sorted list.
    '''
    # I:
    from collections import deque
    def get_itinerary(flights, source, dest):
        visited = set()
        queue = deque([(source, [source])])
        while queue:
            airport, path = queue.popleft()
            if airport == dest:
                return path
            if airport not in visited:
                visited.add(airport)
                for destination in flights.get(airport, []):
                    if destination not in visited:
                        queue.append((destination, path + [destination]))
        return []
    
    
    flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
    }

    print(get_itinerary(flights, 'LAX', 'MIA'))

###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)


