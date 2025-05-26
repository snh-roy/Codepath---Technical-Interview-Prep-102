# Problem 1: Sorting Plants by Rarity
'''
You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to bring a mix of cuttings from both common and rare plants in your collection. 
You track your plant collection in a binary search tree (BST) where each node has a key and a val. 
The val contains the plant name, and the key is an integer representing the plant's rarity.
Plants are organized in the BST by their key.
To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant nodes as tuples in the form (key, val) sorted from least to most rare. 
Sorted order can be achieved by performing an inorder traversal of the BST.
Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.
'''

def problem_1():
    #U:
    '''
    1. What if the tree is empty?
    2. What if the tree has only one node?
    3. What if the tree is unbalanced?
    4. What if the tree is a full binary tree?
    5. What if the tree is a complete binary tree?
    '''

    #P:
    '''
    1. Create a function that takes the root of the tree as input.
    2. Create an empty list to store the values of the nodes in the path.
    3. Create a variable to store the current node, starting at the root.
    4. While the current node is not None:
        a. If the current node has a left child, set the current node to its left child.
        b. If the current node does not have a left child, set the current node to its right child.
        c. If the current node does not have a right child, append the value of the current node to the list and set the current node to None.
    5. Return the list.
    '''
    #I:
    class TreeNode:
        def __init__(self, val, key, left=None, right=None):
            self.key = key      # Plant price
            self.val = val      # Plant name
            self.left = left
            self.right = right


        def sort_plants(collection):
            if collection is None:
                return []
            path = []
            def inorder(node):
                if node:
                    inorder(node.left)
                    path.append((node.key, node.val))
                    inorder(node.right)
            inorder(collection)
            return path
        
        def build_tree(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(*values[mid])
            root.left = build_tree(values[:mid])
            root.right = build_tree(values[mid + 1:])
            return root
        
        values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
        collection = build_tree(values)
        print(sort_plants(collection))

    #RE:
    '''
    The time complexity of this function is O(n) because we visit each node in the tree once.
    The space complexity is O(h) where h is the height of the tree because we store the path in a list.
    In a balanced binary tree, the height is log(n) where n is the number of nodes in the tree.
    In a complete binary tree, the height is log(n) as well.
    In a full binary tree, the height is log(n) as well.
    In an unbalanced binary tree, the height can be n in the worst case.
    '''
# Problem 2: Flower Finding
'''
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. 
The plants are organized according to their names (vals) in alphabetical order in the BST.
Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''

def problem_2():
    #U:
    '''
    1. What if the tree is empty?
    2. What if the tree has only one node?
    3. What if the tree is unbalanced?
    4. What if the tree is a full binary tree?
    5. What if the tree is a complete binary tree?
    '''
    #P:
    '''
    1. Create a function that takes the root of the tree and the target flower name as input.
    2. Create a variable to store the current node, starting at the root.
    3. While the current node is not None:
        a. If the current node's value is equal to the target flower name, return True.
        b. If the current node's value is greater than the target flower name, set the current node to its left child.
        c. If the current node's value is less than the target flower name, set the current node to its right child.
    4. Return False.
    '''
    #I:
    class TreeNode():
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right
         
        def find_flower(inventory, name):
            if inventory is None:
                return False
            if inventory.val == name:
                return True
            elif inventory.val > name:
                return find_flower(inventory.left, name)
            else:
                return find_flower(inventory.right, name)
            
        def build_tree(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(*values[mid])
            root.left = build_tree(values[:mid])
            root.right = build_tree(values[mid + 1:])
            return root
        
        values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
        garden = build_tree(values)

        print(find_flower(garden, "Lilac"))  
        print(find_flower(garden, "Sunflower"))     

    #RE:
    '''
    The time complexity of this function is O(h) where h is the height of the tree because we traverse down the tree.
    The space complexity is O(h) where h is the height of the tree because we store the path in the call stack.
    In a balanced binary tree, the height is log(n) where n is the number of nodes in the tree.
    In a complete binary tree, the height is log(n) as well.
    In a full binary tree, the height is log(n) as well.
    In an unbalanced binary tree, the height can be n in the worst case.
    '''
# Problem 3: Adding a New Plant to the Collection
'''
You have just purchased a new houseplant and are excited to add it to your collection! 
Your collection is meticulously organized using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, and houseplants are organized alphabetically by name (val).
Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. Return the root of your updated collection. If another plant with name already exists in the tree, add the new node in the existing node's right subtree.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''

def problem_3():
    #U:
    '''
    1. What if the tree is empty?
    2. What if the tree has only one node?
    3. What if the tree is unbalanced?
    4. What if the tree is a full binary tree?
    5. What if the tree is a complete binary tree?
    '''
    #P:
    '''
    1. Create a function that takes the root of the tree and the new plant name as input.
    2. Create a variable to store the current node, starting at the root.
    3. While the current node is not None:
        a. If the current node's value is equal to the new plant name, set the current node to its right child.
        b. If the current node's value is greater than the new plant name, set the current node to its left child.
        c. If the current node's value is less than the new plant name, set the current node to its right child.
    4. Return False.
    '''
    #I:
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def add_plant(collection, name):
        if collection is None:
            return TreeNode(name)
        if name < collection.val:
            collection.left = add_plant(collection.left, name)
        else:
            collection.right = add_plant(collection.right, name)
        return collection
    
    def build_tree(values):
        if not values:
            return None
        mid = len(values) // 2
        root = TreeNode(*values[mid])
        root.left = build_tree(values[:mid])
        root.right = build_tree(values[mid + 1:])
        return root
    
    def print_tree(node):
        if node is None:
            return []
        return print_tree(node.left) + [node.val] + print_tree(node.right)
    
    values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
    collection = build_tree(values)
    print_tree(add_plant(collection, "Aloe"))


########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(1)