#Problem 1: Brand Filter
'''
You're tasked with filtering out brands that are not sustainable from a list of fashion brands. 
A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials,
ethical labor practices, or being carbon-neutral. Write the filter_sustainable_brands() function, which takes a 
list of brands and a criterion, then returns a list of brands that meet the criterion. Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def problem_1():
    #U:
    ''' 
    What if the list of brands is empty?
    What if the criterion is not met by any brand?
    '''
    #P:
    '''
    1. Define a function that accepts a list of strings brands and a string criterion
    2. Initialize an empty list sustainable_brands
    3. Loop through each brand in brands
    4. If the current brand meets the criterion, append it to sustainable_brands
    5. Return sustainable_brands
    6. If the list of brands is empty, return []
    7. If no brand meets the criterion, return []
    '''
    # I:
    def filter_sustainable_brands(brands, criterion):
        good_brands = []
        

        for brand in brands:

            brand_criteria = brand["criteria"]
    
            if criterion in brand_criteria:
                good_brands.append(brand["name"])
        
        return good_brands

    brands = [
            {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
            {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
            {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
            {"name": "TrendyStyle", "criteria": ["trendy designs"]}
        ]

    brands_2 = [
            {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
            {"name": "FastStyle", "criteria": ["mass production"]},
            {"name": "NatureWear", "criteria": ["eco-friendly"]},
            {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
        ]

    brands_3 = [
            {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
            {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
            {"name": "FastCloth", "criteria": ["cheap production"]}
        ]

    print(filter_sustainable_brands(brands, "eco-friendly"))        # Output: ['EcoWear', 'GreenThreads']
    print(filter_sustainable_brands(brands_2, "ethical labor"))     # Output: ['Earthly']
    print(filter_sustainable_brands(brands_3, "carbon-neutral"))    # Output: ['GreenLife']

    #RE: 
    '''
    The time complexity of this solution is O(n), where n is the number of brands in the list.
    This is because the function loops through each brand in the list to check if it meets the criterion.
    The space complexity of this solution is O(m), where m is the number of brands that meet the criterion.
    This is because the function creates a new list to store the brands that meet the criterion.
    '''

#Problem 2: Eco-Friendly Materials
'''
Certain materials are recognized as eco-friendly due to their low environmental impact. 
You need to track which materials are used by various brands and count how many times each material
 appears across all brands. This will help identify the most commonly used eco-friendly materials.
Write the count_material_usage() function, which takes a list of brands (each with a list of materials)
and returns the material names and the number of times each material appears across all brands.
Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why
you believe your solution has the stated time and space complexity.
'''

def problem_2():
    #U:
    '''
    What if the list of brands is empty?
    What if a brand has no materials listed?
    '''
    #P:
    '''
    1. Define a function that accepts a list of dictionaries brands, where each dictionary represents a brand and its materials
    2. Initialize an empty dictionary material_count
    3. Loop through each brand in brands
    4. Loop through each material in the brand
    5. If the material is not in material_count, add it with a count of 1
    6. If the material is in material_count, increment its count by 1
    7. Return material_count
    8. If the list of brands is empty, return {}
    '''
    # I:
    def count_material_usage(brands):
        material_count = {}
        
        for brand in brands:
            materials = brand["materials"]
            
            for material in materials:
                if material not in material_count:
                    material_count[material] = 1
                else:
                    material_count[material] += 1
        
        return material_count
    brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

    brands_2 = [
        {"name": "NatureWear", "materials": ["hemp", "linen"]},
        {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
        {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
    ]

    brands_3 = [
        {"name": "OrganicThreads", "materials": ["organic cotton"]},
        {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
        {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
    ]

    print(count_material_usage(brands))
    print(count_material_usage(brands_2))
    print(count_material_usage(brands_3))

    #RE:
    '''
    The time complexity of this solution is O(n*m), where n is the number of brands and m is the average number of materials per brand.
    This is because the function loops through each brand and then through each material in the brand.
    The space complexity of this solution is O(k), where k is the number of unique materials used across all brands.
    This is because the function creates a dictionary to store the count of each material.
    '''

#Problem 4: Fabric Pairing
'''
You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. 
Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics whose combined cost 
is the highest possible without exceeding the budget. Write the find_best_fabric_pair() function, which takes a list of fabrics
 (each with a name and cost) and a budget. The function should return the names of the two fabrics whose combined cost is the closest 
 to the budget without exceeding it. Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def problem_3(): 
    #U:
    '''
    What if the list of fabrics is empty?
    What if no pair of fabrics meets the budget constraint?
    '''
    #P:
    '''
    1. Define a function that accepts a list of dictionaries fabrics, where each dictionary represents a fabric and its cost, and an integer budget
    2. Initialize variables max_cost and best_pair to track the maximum cost and the best pair of fabrics
    3. Loop through each fabric in fabrics
    4. Loop through each fabric in fabrics
    5. If the sum of the costs of the two fabrics is less than or equal to the budget and greater than max_cost, update max_cost and best_pair
    6. Return the names of the fabrics in best_pair
    7. If the list of fabrics is empty, return []
    '''
    # I:
    def find_best_fabric_pair(fabrics, budget):
        max_cost = 0              
        best_pair = ()            

        for i in range(len(fabrics)):         
            for j in range(i+1, len(fabrics)): 
                total_cost = fabrics[i][1] + fabrics[j][1]  
                if total_cost <= budget and total_cost > max_cost:  
                    max_cost = total_cost                          
                    best_pair = (fabrics[i][0], fabrics[j][0])     
        return best_pair  

    fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
    fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
    fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

    print(find_best_fabric_pair(fabrics, 45))      # Output: ('Organic Cotton', 'Hemp')
    print(find_best_fabric_pair(fabrics_2, 70))    # Output: ('Tencel', 'Recycled Wool')
    print(find_best_fabric_pair(fabrics_3, 60))    # Output: ('Linen', 'Bamboo')

    #RE:
    '''
    The time complexity of this solution is O(n^2), where n is the number of fabrics in the list.
    This is because the function loops through each pair of fabrics to calculate the total cost.
    The space complexity of this solution is O(1) because the function only uses a constant amount of space
    to store the maximum cost and the best pair of fabrics.
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