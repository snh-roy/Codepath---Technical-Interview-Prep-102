#Problem 1: Creating Cookie Orders from Descriptions
'''
In your bakery, customer cookie orders are organized in a binary tree, where each node represents a different flavor of cookie ordered by the customers. 
You are given a 2D integer array descriptions where descriptions[i] = [parent_i, child_i, is_left_i] 
indicates that parent_i is the parent of child_i in a binary tree of unique flavors.
If is_left_i == 1, then child_i is the left child of parent_i.
If is_left_i == 0, then child_i is the right child of parent_i.
Construct the binary tree described by descriptions and return its root.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.
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
    1. Create a dictionary to hold the nodes.
    2. Create a variable to hold the root node.
    3. Iterate through the descriptions array.
    4. For each description, create a node for the parent if it doesn't exist.
    5. Create a node for the child if it doesn't exist. 
    6. If is_left_i == 1, set the left child of the parent to the child.
    7. If is_left_i == 0, set the right child of the parent to the child.
    8. If the parent is not in the dictionary, set it as the root node.
    9. Return the root node.
    '''

    # I:
    from collections import deque
    class TreeNode:
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right

        def build_cookie_tree(descriptions):
            nodes = {}
            root = None

            for parent, child, is_left in descriptions:
                if parent not in nodes:
                    nodes[parent] = TreeNode(parent)
                if child not in nodes:
                    nodes[child] = TreeNode(child)

                if is_left:
                    nodes[parent].left = nodes[child]
                else:
                    nodes[parent].right = nodes[child]

                if root is None or root.val == child:
                    root = nodes[parent]

            return root
        
        def build_tree(values):
            if not values:
                return None
            
        def print_tree(root):
            if not root:
                return "Empty"
            result = []
            queue = deque([root])
            while queue:
                node = queue.popleft()
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            while result and result[-1] is None:
                result.pop()
            print(result)
            

        descriptions1 = [
            ["Chocolate Chip", "Peanut Butter", 1],
            ["Chocolate Chip", "Oatmeal Raisin", 0],
            ["Peanut Butter", "Sugar", 1]
        ]
        print_tree(build_cookie_tree(descriptions1))

        descriptions2 = [
            ["Ginger Snap", "Snickerdoodle", 0],
            ["Ginger Snap", "Shortbread", 1]
        ]
        print_tree(build_cookie_tree(descriptions2))

#Problem 2: Cookie Sum
'''
Given the root of a binary tree where each node represents a certain number of cookies, 
return the number of unique paths from the root to a leaf node where the total number of cookies equals a given target_sum.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your
solution has the stated time and space complexity. Evaluate the complexities for both a balanced and unbalanced tree.
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
    1. Create a variable to hold the count of unique paths.
    2. Create a recursive function to traverse the tree.
    3. If the current node is None, return 0.
    4. If the current node is a leaf node and its value equals target_sum, increment the count.
    5. Recursively call the function for the left and right children, subtracting the current node's value from target_sum.
    6. Return the total count.
    '''
    # I:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        
        def build_tree(values):
            if not values:
                return None

        def count_cookie_paths(root, target_sum):
            if not root:
                return 0

            def dfs(node, current_sum):
                if not node:
                    return 0
                current_sum += node.val
                if not node.left and not node.right:
                    return 1 if current_sum == target_sum else 0
                return dfs(node.left, current_sum) + dfs(node.right, current_sum)

            return dfs(root, 0)
        cookie_nums = [10, 5, 8, 3, 7, 12, 4]
        cookies1 = print(build_tree(cookie_nums))

    #RE:
    '''
    The time complexity is O(n) because we visit each node once.
    The space complexity is O(h) where h is the height of the tree because we use recursion.
    For a balanced tree, h = log(n), so the space complexity is O(log(n)).
    For an unbalanced tree, h = n, so the space complexity is O(n).
    '''

#Problem 3: Most Popular Cookie Combo
'''
In your bakery, each cookie order is represented by a binary tree where each node contains the number of cookies of a particular type. 
The cookie combo for any node is defined as the total number of cookies in the entire subtree rooted at that node (including that node itself).
Given the root of a cookie order tree, return an array of the most frequent cookie combo in your bakery's orders. 
If there is a tie, return all the most frequent combos in any order.
Evaluate the time and space complexity of your function. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Evaluate the complexities for both a balanced and unbalanced tree.
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
    1. Create a dictionary to hold the frequency of each combo.
    2. Create a variable to hold the maximum frequency.
    3. Create a recursive function to traverse the tree and calculate the combo for each node.
    4. If the combo is not in the dictionary, add it with a frequency of 1.
    5. If it is in the dictionary, increment its frequency.
    6. Update the maximum frequency if necessary.
    7. Return the list of combos with the maximum frequency.
    '''
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

        def most_popular_cookie_combo(root):
            from collections import defaultdict

            def dfs(node):
                if not node:
                    return 0
                combo = node.val + dfs(node.left) + dfs(node.right)
                freq[combo] += 1
                return combo

            freq = defaultdict(int)
            dfs(root)

            max_freq = max(freq.values())
            return [combo for combo, count in freq.items() if count == max_freq]
        
        cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))
        print(most_popular_cookie_combo(cookies1))  

    #RE:
    '''
    The time complexity is O(n) because we visit each node once.
    The space complexity is O(n) for the frequency dictionary in the worst case.
    For a balanced tree, the space complexity is O(log(n)).
    For an unbalanced tree, the space complexity is O(n).
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