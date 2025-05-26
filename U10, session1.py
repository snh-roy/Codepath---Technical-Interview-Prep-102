# Problem 1: There and Back
'''
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a 
different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i].
Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight 
from destination j to destination i. Return False otherwise.
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
    1. Create a set to hold the flights.
    2. Iterate through the flights array.
    3. For each flight, check if the reverse flight exists in the set.
    4. If it does not exist, return False.
    5. If all flights exist in both directions, return True.
    '''
    # I:
    from collections import defaultdict
    def bidirectional_flights(flights):
        flight_set = set()
        for i, destinations in enumerate(flights):
            for dest in destinations:
                flight_set.add((i, dest))
        
        for i, destinations in enumerate(flights):
            for dest in destinations:
                if (dest, i) not in flight_set:
                    return False
        return True
    
    flights1 = [[1, 2], [0], [0, 3], [2]]
    flights2 = [[1, 2], [], [0], [2]]

    print(bidirectional_flights(flights1))
    print(bidirectional_flights(flights2))


# Problem 2: Find Center of Airport
'''
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with 
n nodes where each node represents a terminal in the airport labeled from 1 to n. 
You want to find the center terminal in the airport where the pilots' lounge is located.
Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, 
return the center of the given airport.
A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.
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
    1. Create a dictionary to hold the degree of each node.
    2. Iterate through the terminals array.
    3. For each terminal, increment the degree of both nodes.
    4. Find the node with degree n-1.
    5. Return the node with degree n-1.
    '''
    # I:
    def find_center(terminals):
        degree = {}
        for u, v in terminals:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        
        for node, deg in degree.items():
            if deg == len(terminals):
                return node
        return -1
    terminals1 = [[1,2],[2,3],[4,2]]
    terminals2 = [[1,2],[5,1],[1,3],[1,4]]

    print(find_center(terminals1))
    print(find_center(terminals2))

# Problem 3: Finding All Reachable Destinations    
'''
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. 
The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, 
and the corresponding value is a list of other destinations that are reachable through a direct flight.
Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting 
flights with layovers. The list should be provided in ascending order by number of layovers required.
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
    def get_all_destinations(flights):
        visited = set()
        queue = []
        
        for start in flights:
            queue.append(start)
            while queue:
                airport = queue.pop(0)
                if airport not in visited:
                    visited.add(airport)
                    for dest in flights[airport]:
                        if dest not in visited:
                            queue.append(dest)
        
        return sorted(list(visited))
    flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}


    print(get_all_destinations(flights, "Beijing"))
    print(get_all_destinations(flights, "Helsinki"))


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)