#Problem 1: Ivy Cutting
'''You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. 
Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
Assume the input tree is balanced when calculating time and space complexity.'''

def problem_1():
    #U:
    '''
    What if the tree is empty?
    What if the tree has only one node?
    What if the tree is unbalanced?
    What if the tree is a full binary tree?
    What if the tree is a complete binary tree?
    '''
    #P:
    '''
    1. Create a function that takes the root of the tree as input.
    2. Create an empty list to store the values of the nodes in the path.
    3. Create a variable to store the current node, starting at the root.
    4. While the current node is not None:
        a. Append the value of the current node to the list.
        b. If the current node has a right child, set the current node to its right child.
        c. If the current node does not have a right child, set the current node to its left child.
    5. Return the list.
    '''
    #I:
    
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

        def right_vine(root):
            if root is None:
                return []
            path = []
            current = root
            while current:
                path.append(current.val)
                if current.right:
                    current = current.right
                else:
                    current = current.left
            return path
    
    ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
    print(TreeNode.right_vine(ivy1))
    
    #RE:
    '''
    The time complexity of this function is O(n) because we visit each node in the tree once.
    The space complexity is O(h) where h is the height of the tree because we store the path in a list.
    In a balanced binary tree, the height is log(n) where n is the number of nodes in the tree.
    In a complete binary tree, the height is log(n) as well.
    In a full binary tree, the height is log(n) as well.
    In an unbalanced binary tree, the height can be n in the worst case.
    '''

# Problem 2: Ivy Cutting II
'''
If you implemented right_vine() iteratively in the previous problem, implement it recursively. 
If you implemented it recursively, implement it iteratively.
Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity
'''

def problem_2():
    #U:
    '''
    What if the tree is empty?
    What if the tree has only one node?
    What if the tree is unbalanced?
    What if the tree is a full binary tree?
    What if the tree is a complete binary tree?
    '''
    #P:
    '''
    1. Create a function that takes the root of the tree as input.
    2. Create an empty list to store the values of the nodes in the path.
    3. Create a variable to store the current node, starting at the root.
    4. While the current node is not None:
        a. Append the value of the current node to the list.
        b. If the current node has a right child, set the current node to its right child.
        c. If the current node does not have a right child, set the current node to its left child.
    5. Return the list.
    '''
    #I:
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def right_vine(root):
        if root is None:
            return []
        path = []
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                path.append(node.val)
        postorder(root)
        return path
    ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

    ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

    print(right_vine(ivy1))
    print(right_vine(ivy2))

    #RE:
    '''
    The time complexity of this function is O(n) because we visit each node in the tree once.
    The space complexity is O(h) where h is the height of the tree because we store the path in a list.
    In a balanced binary tree, the height is log(n) where n is the number of nodes in the tree.
    In a complete binary tree, the height is log(n) as well.
    In a full binary tree, the height is log(n) as well.
    In an unbalanced binary tree, the height can be n in the worst case.
    '''

# Problem 3: Pruning Plans
'''
You have a large overgrown Magnolia tree that's in desperate need of some pruning.
Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned.
Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. 
In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. 
Postorder traversals are often used when deleting nodes from a tree.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''

def problem_3():
    #U:
    ''' 
    What if the tree is empty?
    What if the tree has only one node?
    What if the tree is unbalanced?
    What if the tree is a full binary tree?
    What if the tree is a complete binary tree?
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
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right
        
        def survey_tree(root):
            if root is None:
                return []
            path = []
            def postorder(node):
                if node:
                    postorder(node.left)
                    postorder(node.right)
                    path.append(node.val)
            postorder(root)
            return path
    
    magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
    
    print(TreeNode.survey_tree(magnolia))


########################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)