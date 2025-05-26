# Problem 1: Villager Class
'''
A class constructor is a special method or function that is used to create and initialize a new object from a class. 
Define the class constructor __init__() for a new class Villager that represents characters in the game Animal Crossing. 
The constructor accepts three required arguments: strings name, species, and catchphrase. 
The constructor defines four properties for a Villager: name, a string initialized to the argument name
species, a string initialized to the argument species
catchphrase, a string initialized to the argument catchphrase
furniture, a list initialized to an empty list
'''

def problem_1():
    #U:
    '''
    What if the arguments are not strings?
    '''
    #P:
    '''
    1. Define a class Villager
    2. Define the constructor __init__ that accepts three required arguments: name, species, and catchphrase
    3. Initialize the properties name, species, and catchphrase to the arguments
    4. Initialize the property furniture to an empty list
    '''
    # I:
    class Villager:
        def __init__(self, name, species, catchphrase):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []
    
    #Example
    apollo = Villager("Apollo", "Eagle", "pah")
    print(apollo.name)
    print(apollo.species) 
    print(apollo.catchphrase)
    print(apollo.furniture)

# Problem 2: Add Furniture
'''
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.
Update the Villager class with a new method add_item() that takes in one parameter, item_name.
The method should validate the item_name.
If the item is valid, add item_name to the villagers furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", 
"ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree"
'''

def problem_2():
    #U:
    '''
    What if the item_name is not a string?
    '''
    #P:
    '''
    1. Define a method add_item in the Villager class that accepts one parameter item_name
    2. Validate the item_name
    3. If the item is valid, add item_name to the villagers furniture attribute
    '''
    # I:
    class Villager:
        def __init__(self, name, species, catchphrase):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []
        
        def add_item(self, item_name):
            valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            
            if item_name in valid_items:
                self.furniture.append(item_name)
    
    #Example
    alice = Villager("Alice", "Koala", "guvnor")
    print(alice.furniture)

    alice.add_item("acoustic guitar")
    print(alice.furniture)

    alice.add_item("cacao tree")
    print(alice.furniture)

    alice.add_item("nintendo switch")
    print(alice.furniture)

#Problem 3: Group by Personality
    '''
    The Villager class has been updated below to include the new string attribute personality 
    representing the character's personality type.
    Outside of the Villager class, write a function of_personality_type(). 
    Given a list of Villager instances townies and a string personality_type as parameters, 
    return a list containing the names of all villagers in townies with personality personality_type.
    Return the names in any order.
    '''
def problem_3():
    #U:
    '''
    What if the list townies is empty?
    What if there are no villagers with the specified personality type?
    '''
    #P:
    '''
    1. Define a function of_personality_type that accepts two parameters: townies and personality_type
    2. Initialize an empty list names
    3. Loop through each villager in townies
    4. If the villager's personality is equal to personality_type, add the villager's name to names
    5. Return names
    '''
    # I:
    class Villager:
        def __init__(self, name, species, catchphrase, personality):
            self.name = name
            self.species = species
            self.catchphrase = catchphrase
            self.furniture = []
            self.personality = personality
        
        def add_item(self, item_name):
            valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            
            if item_name in valid_items:
                self.furniture.append(item_name)

        def of_personality_type(townies, personality_type):
            names = []
            
            for villager in townies:
                if villager.personality == personality_type:
                    names.append(villager.name)
            
            return names


    isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
    bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
    stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

    print(of_personality_type([isabelle, bob, stitches], "Lazy"))
    print(of_personality_type([isabelle, bob, stitches], "Cranky"))


###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)