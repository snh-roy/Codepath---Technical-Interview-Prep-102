#Problem 1: Counting the Layers of a Sandwich
'''
You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list.
Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def problem_1(): 
    #U: 
    '''
    1. What if the sandwich is empty?
    2. What if the sandwich has only one layer?
    '''
    #P:
    '''
    1. If the sandwich is empty, return 0.
    2. Initialize a variable count to 0.
    3. Loop through the sandwich.
    4. If the element is a list, increment count by 1 and recursively call count_layers on the element.
    5. Return count.
    '''
    #I:
    def count_layers(sandwich):
        if not sandwich:
            return 0

        count = 0
        for layer in sandwich:
            if isinstance(layer, list):
                count += 1 + count_layers(layer)
        return count
    
    sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
    sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

    print(count_layers(sandwich1))
    print(count_layers(sandwich2))
    #RE:
    ''' Time complexity is O(n) and space complexity is O(n) where n is the number of layers in the sandwich.
    The time complexity is O(n) because we are looping through the sandwich list once. The space complexity is O(n)
    because the recursive calls will be stored in the call stack until the base case is reached.
    '''

#Problem 2: Reversing Deli Orders
'''
The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. 
Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def problem_2():
    #U:
    '''
    1. What if the orders string is empty?
    2. What if the orders string has only one order?
    '''
    #P:
    '''
    1. If the orders string is empty, return an empty string.
    2. Split the orders string by space.
    3. If the length of the split orders is 1, return the orders string.
    4. Return the last order followed by a space and recursively call reverse_orders on the rest of the orders.
    '''
    #I:
    def reverse_orders(orders):
        if not orders:
            return ""

        split_orders = orders.split()
        if len(split_orders) == 1:
            return orders

        return split_orders[-1] + " " + reverse_orders(" ".join(split_orders[:-1]))
    
    print(reverse_orders("Bagel Sandwich Coffee"))
    print(reverse_orders("Salad Pizza Soda"))
    #RE:
    ''' The time complexity is O(n) because we are splitting the string into a list of orders and joining them back together.
     The space complexity is O(n) because the recursive calls will be stored in the call stack until the base case is reached.'''

# Problem 3: Sharing the Coffee
'''
The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. 
Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() that accepts a list of integers coffee representing
 the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. '''

def problem_3():
    #U:
    '''
    1. What if the coffee list is empty?
    2. What if the coffee list has only one batch of coffee?
    '''
    #P:
    '''
    1. If the coffee list is empty, return False.
    2. If the coffee list has only one batch of coffee, return True if the volume is divisible by n and False otherwise.
    3. Initialize a variable total_volume to the sum of the coffee list.
    4. If the total volume is not divisible by n, return False.
    5. Initialize a variable target_volume to total_volume divided by n.
    6. Sort the coffee list in descending order.
    7. Initialize a variable current_volume to 0.
    8. Loop through the coffee list.
    9. Add the current batch volume to current_volume.
    10. If current_volume is equal to target_volume, decrement n by 1 and reset current_volume to 0.
    11. If n is 0, return True.
    12. Return False.
    '''
    #I:
    def can_split_coffee(coffee, n):
        if not coffee:
            return False

        if len(coffee) == 1:
            return coffee[0] % n == 0

        total_volume = sum(coffee)
        if total_volume % n != 0:
            return False

        target_volume = total_volume // n
        coffee.sort(reverse=True)

        current_volume = 0
        for volume in coffee:
            current_volume += volume
            if current_volume == target_volume:
                n -= 1
                current_volume = 0
            if n == 0:
                return True
        return False
    
    print(can_split_coffee([4, 4, 8], 2)) # True
    print(can_split_coffee([5, 10, 15], 4)) #False
    #RE:
    ''' The time complexity is O(n log n) because we are sorting the coffee list. The space complexity is O(n) because the recursive calls will be stored in the call stack until the base case is reached.'''

########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)