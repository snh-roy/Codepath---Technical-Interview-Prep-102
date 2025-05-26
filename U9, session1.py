#Problem 1: Croquembouche II
'''
You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. 
They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.
Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, 
traverse the croquembouche in tier order (i.e., level by level, left to right).
You should return a list of lists where each inner list represents a tier (level) of the croquembouche and the elements of each inner list contain the 
flavors of each cream puff on that tier (node vals from left to right).
Note: The build_tree() and print_tree() functions both use variations of a level order traversal. 
To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time complexity.
'''

def problem_1():
    #U:
    '''
    What does "tier order" mean exactly?
    What is the output?
    What is the input?
    '''
    #P:
    '''
    1. Create a list to hold the tiers.
    2. Create a queue to hold the nodes.
    3. Add the root node to the queue.
    4. While the queue is not empty:
        a. Create a list to hold the current tier.
        b. Get the size of the queue.
        c. For each node in the queue:
            i. Pop the first node from the queue.
            ii. Add the node's value to the current tier.
            iii. Add the node's children to the queue.
        d. Add the current tier to the list of tiers.
    5. Return the list of tiers.

    '''
    # I:
    class Puff():
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right
    def listify_design(design):
        if not design:
            return []
        tiers = []
        queue = [design]
        while queue:
            current_tier = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                current_tier.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            tiers.append(current_tier)
        return tiers
    
    croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
    print(listify_design(croquembouche))
    
    #Re:
    '''
    The time complexity is O(n) because we visit each node once.
    The space complexity is O(n) because we store the nodes in a queue and the tiers in a list.
    '''


#Problem 2: Icing Cupcakes in Zigzag Order

'''
You have rows of cupcakes represented as a binary tree cupcakes where each node in the tree represents a cupcake. 
To ice them efficiently, you are icing cupcakes one row (level) at a time, in zig zag order (i.e., from left to right, then right to left for the next row and alternate between).
Return a list of the cupcake values in the order you iced them.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.
'''

def problem_2():
    #U:
    '''
    What does "zigzag order" mean exactly?
    What is the output?
    What is the input?
    '''
    #P:
    '''
    1. Create a list to hold the iced cupcakes.
    2. Create a queue to hold the nodes.
    3. Add the root node to the queue.
    4. Create a variable to keep track of the current level.
    5. While the queue is not empty:
        a. Create a list to hold the current level.
        b. Get the size of the queue.
        c. For each node in the queue:
            i. Pop the first node from the queue.
            ii. Add the node's value to the current level.
            iii. Add the node's children to the queue.
        d. If the current level is even, reverse it.
        e. Add the current level to the list of iced cupcakes.
    6. Return the list of iced cupcakes.
    '''
    # I:
    class TreeNode():
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right
        
        def build_tree(values):
            if not values:
                return None

        def zigzag_icing_order(Cupcakes):
            if not Cupcakes:
                return []
            iced_cupcakes = []
            queue = [Cupcakes]
            left_to_right = True
            while queue:
                current_level = []
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    current_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if not left_to_right:
                    current_level.reverse()
                iced_cupcakes.extend(current_level)
                left_to_right = not left_to_right
            return iced_cupcakes
        
        flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
        cupcakes = build_tree(flavors)
    
    #RE:
    '''
    The time complexity is O(n) because we visit each node once.
    The space complexity is O(n) because we store the nodes in a queue and the iced cupcakes in a list.
    '''

#Problem 3: Larger Order Tree
'''
You have the root of a binary search tree orders, where each node in the tree represents an order and each node's value represents the number of cupcakes the customer ordered. 
Convert the tree to a 'larger order tree' such that the value of each node in tree is equal to its original value plus the sum of all node values greater than it.
As a reminder a BST satisfies the following constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.
'''

def problem_3():
    #U:
    '''
    What does "larger order tree" mean exactly?
    What is the output?
    What is the input?
    '''
    #P:
    '''
    1. Create a variable to hold the sum of all node values.
    2. Create a function to traverse the tree in reverse order (right, root, left).
    3. For each node, add its value to the sum and update its value to the sum.
    4. Return the updated tree.
    '''
    # I:
    class Order():
        def __init__(self, cupcakes, left=None, right=None):
            self.val = cupcakes
            self.left = left
            self.right = right
        
        def larger_order_tree(orders):
            def reverse_inorder(node):
                if not node:
                    return 0
                right_sum = reverse_inorder(node.right)
                node.val += right_sum
                return node.val + reverse_inorder(node.left)
            
            reverse_inorder(orders)
            return orders
        
        def build_tree(values):
            if not values:
                return None
            
        order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
        orders = build_tree(order_sizes)
    
    #RE:
    '''
    The time complexity is O(n) because we visit each node once.
    The space complexity is O(h) where h is the height of the tree because we use recursion.
    '''

###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)