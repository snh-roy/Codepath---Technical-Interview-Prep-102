#Problem 1: Count Unique Characters in a Script
'''
Given a dictionary where the keys are character names and the values are 
lists of their dialogue lines, count the number of unique characters in the script.
Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def problem_1():
    #U:
    '''
    What if the script is empty?
    What if a character has no dialogue lines?
    '''
    #P:
    '''
    1. Define a function that accepts a dictionary script, where keys are character names and values are lists of dialogue lines
    2. Initialize an empty set unique_characters
    3. Loop through each character in script
    4. Add the current character to unique_characters
    5. Return the length of unique_characters
    6. If the script is empty, return 0
    '''
    # I:
    def count_unique_characters(script):
        unique_characters = set()
        
        for character in script:
            unique_characters.add(character)
        
        return len(unique_characters)
    
    script = {
        "Alice": ["Hello there!", "How are you?"],
        "Bob": ["Hi Alice!", "I'm good, thanks!"],
        "Charlie": ["What's up?"]
    }
    print(count_unique_characters(script)) 

    script_with_redundant_keys = {
        "Alice": ["Hello there!"],
        "Alice": ["How are you?"],
        "Bob": ["Hi Alice!"]
    }
    print(count_unique_characters(script_with_redundant_keys)) 

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each character in the script, 
    where n is the number of characters in the script.
    The space complexity is also O(n) because the unique_characters set stores at most n unique characters.
    '''

#Problem 2: Find Most Frequent Keywords
'''
Identify the most frequently used keywords from a dictionary where the keys are scene
names and the values are lists of keywords used in each scene. Return the keyword that 
appears the most frequently across all scenes. If there is a tie, return all the keywords with the highest frequency.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe
your solution has the stated time and space complexity.
'''
def problem_2():
    #U:
    '''
    What if the dictionary is empty?
    What if a scene has no keywords?
    '''
    #P:
    '''
    1. Define a function that accepts a dictionary scenes, where keys are scene names and values are lists of keywords
    2. Initialize an empty dictionary keyword_count
    3. Loop through each scene in scenes
    4. Loop through each keyword in the scene
    5. If the keyword is not in keyword_count, add it with a count of 1
    6. If the keyword is in keyword_count, increment its count by 1
    7. Find the maximum count in keyword_count
    8. Return all keywords with the maximum count
    9. If the dictionary is empty, return an empty list
    '''
    # I:
    def find_most_frequent_keywords(scenes):
        keyword_count = {}
        
        for scene in scenes:
            keywords = scenes[scene]
            
            for keyword in keywords:
                if keyword not in keyword_count:
                    keyword_count[keyword] = 1
                else:
                    keyword_count[keyword] += 1
        
        max_count = max(keyword_count.values())
        frequent_keywords = [keyword for keyword, count in keyword_count.items() if count == max_count]
        
        return frequent_keywords
    
    scenes = {
        "Scene 1": ["action", "hero", "battle"],
        "Scene 2": ["hero", "action", "quest"],
        "Scene 3": ["battle", "strategy", "hero"],
        "Scene 4": ["action", "strategy"]
    }
    print(find_most_frequent_keywords(scenes))

    scenes = {
        "Scene A": ["love", "drama"],
        "Scene B": ["drama", "love"],
        "Scene C": ["comedy", "love"],
        "Scene D": ["comedy", "drama"]
    }
    print(find_most_frequent_keywords(scenes)) 
    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each scene in the scenes dictionary,
    where n is the number of scenes.
    '''

# Problem 3: Track Scene Transitions
'''
Given a list of scenes in a story, use a queue to keep track of the transitions from one scene to the next. 
You need to simulate the transitions by processing each scene in the order they appear and print out each transition
from the current scene to the next. Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''
def problem_3():
    #U:
    '''
    What if the list of scenes is empty?
    What if there is only one scene in the list?
    '''
    #P:
    '''
    1. Define a function that accepts a list of scenes
    2. Initialize an empty queue transitions
    3. Loop through each scene in the list
    4. If the queue is not empty, print the transition from the previous scene to the current scene
    5. Add the current scene to the queue
    6. If the list of scenes is empty, return
    '''
    # I:
    def track_scene_transitions(scenes):
        transitions = []
        
        for i, scene in enumerate(scenes):
            if transitions:
                print(f"Transition from {transitions[-1]} to {scene}")
            transitions.append(scene)
    
    scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
    track_scene_transitions(scenes)

    scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
    track_scene_transitions(scenes)

    #RE:
    '''
    The time complexity of this solution is O(n) because the function loops through each scene in the list of scenes,
    where n is the number of scenes.
    The space complexity is O(n) because the transitions queue stores at most n scenes.
    '''

###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)