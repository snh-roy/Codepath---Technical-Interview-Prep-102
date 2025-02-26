# Problem 1: Balanced Art Collection
'''
A balanced collection is one where the difference between the maximum and 
minimum value of the art pieces is exactly 1.
Given an integer array art_pieces representing the value of each art piece, 
write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.
A subsequence is a sequence derived from the array by deleting some or
 no elements without changing the order of the remaining elements.
'''
def problem_1():

    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    '''
    #P:
    '''
    1. Define a function that accepts an array art_pieces
    2. Initialize a variable max_length to 0
    3. Loop through each element in art_pieces
    4. Initialize a variable count to 0
    5. Loop through each element in art_pieces
    6. If the difference between the current element and the outer element is 1, increment count by 1
    7. If count is greater than max_length, set max_length to count
    8. Return max_length
    9. If the array is empty, return 0
    10. If the array has only one element, return 0
    '''
    #I:
    def find_balanced_subsequence(art_pieces:list) -> int:
        if not art_pieces:
            return 0
        if len(art_pieces) == 1:
            return 0
        max_length = 0
        for i in range(len(art_pieces)):
            count = 0
            for j in range(len(art_pieces)):
                if abs(art_pieces[j] - art_pieces[i]) == 1:
                    count += 1
            if count > max_length:
                max_length = count
        return max_length
    
    art_pieces1 = [1,3,2,2,5,2,3,7] 
    art_pieces2 = [1,2,3,4]
    art_pieces3 = [1,1,1,1]

    print(find_balanced_subsequence(art_pieces1)) 
    print(find_balanced_subsequence(art_pieces2))
    print(find_balanced_subsequence(art_pieces3))

#Problem 2: Verifying Authenticity
'''
The collection is considered "authentic" if it is a permutation of an array base[n].
The base[n] array is defined as [1, 2, ..., n - 1, n, n], 
meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once,
 and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].
Write a function is_authentic_collection that accepts an array of integers art_pieces and
returns True if the given array is an authentic array, and otherwise returns False
'''
def problem_2():

    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    ''' 
    #P:
    '''
    1. Define a function that accepts an array art_pieces
    2. Initialize a variable n to the length of art_pieces
    3. Initialize a variable base to an empty list
    4. Loop through each element in range 1 to n
    5. Append the current element to base
    6. Append n to base
    7. Return True if art_pieces is equal to base, otherwise return False
    '''
    #I:
    def is_authentic_collection(art_pieces: list) -> bool:
        n = len(art_pieces)
        count = [0] * (n + 1) 

        for num in art_pieces:
            if 1 <= num <= n:
                count[num] += 1  

        for i in range(1, n + 1):  
            if count[i] == 0:
                return False

        return True
    
    collection1 = [2, 1, 3]
    collection2 = [1, 3, 3, 2]
    collection3 = [1, 1]

    print(is_authentic_collection(collection1)) 
    print(is_authentic_collection(collection2)) 
    print(is_authentic_collection(collection3)) 

# Problem 4: Gallery Subdomain Traffic
'''
Domain like "modern.artmuseum.com" consists of various subdomains. At the top level, we have "com", 
at the next level, we have "artmuseum.com", and at the lowest level, "modern.artmuseum.com".
When visitors access a domain like "modern.artmuseum.com", they also implicitly visit the parent
domains "artmuseum.com" and "com". A count-paired domain is represented as "rep d1.d2.d3" where rep is the
number of visits to the domain and d1.d2.d3 is the domain itself.
For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. 
The order of the output does not matter.
'''
def problem_3():
    
    #U:
    '''
    What if the array is empty?
    What if the array has only one element?
    '''
    #P:
    '''
    1. Define a function that accepts an array cpdomains
    2. Initialize an empty dictionary domain_count
    3. Loop through each element in cpdomains
    4. Split the current element by space
    5. Initialize a variable count to the integer of the first element
    6. Initialize a variable domain to the second element
    7. Split the domain by "."
    8. Loop through each index, subdomain in enumerate reversed split domain
    9. Join the subdomain with "."
    10. If the subdomain is not in domain_count, add it to domain_count with the count as the value
    11. Otherwise, increment the value of the subdomain by count
    12. Initialize an empty list result
    13. Loop through each key, value pair in domain_count
    14. Append the value and key to result
    15. Return result
    16. If the array is empty, return an empty list
    17. If the array has only one element, return an empty list
    '''
    #I:
    def subdomain_visits(cpdomains: list) -> list:
        domain_count = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                if subdomain not in domain_count:
                    domain_count[subdomain] = count
                else:
                    domain_count[subdomain] += count
        result = []
        for key, value in domain_count.items():
            result.append(f"{value} {key}")
        return result
    cpdomains1 = ["9001 modern.artmuseum.com"]
    cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
                "1 contemporary.gallery.com", "5 medieval.org"]

    print(subdomain_visits(cpdomains1))
    print(subdomain_visits(cpdomains2))




###########################################################
def solve_problem(problem_number:int):
    if problem_number == 1:
        problem_1()
    if problem_number == 2:
        problem_2()
    if problem_number == 3:
        problem_3()
solve_problem(3)