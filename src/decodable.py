def is_uniquely_decodable(source_alphabet, code_scheme):
    """
    Determines whether a given coding scheme is uniquely decodable.
    Using Sardinas-Patterson theorem:
    A code C is uniquely decodable if and only if the sets C and L-INF are disjoint.

    Args:
    source_alphabet (list): List of characters in the source alphabet.
    code_scheme (dict): Dictionary mapping source characters to binary codes.

    Returns:
    bool: True if the code is uniquely decodable, False otherwise.

    Time complexity: O(i*n^2*m) where n is the size of the code, m is the length of the longest string, 
                     and i is the number of iterations until periodicity is detected
    Space complexity: O(i*n*m) in the worst case (L_history array of sets of strings), where n is the size of the code and m the length of the longest string 
                    and i is the number of iterations until periodicity is detected
    """
    # Convert the code scheme to a set of codewords
    C = set(code_scheme.values())
    
    # Step 1: Calculate L1
    # L1 = {b | ab ∈ C and a ∈ C}
    L1 = set()
    for a in C:
        for ab in C:
            if ab.startswith(a) and ab != a:
                L1.add(ab[len(a):])

    # Step 2: Calculate Ln using iteration
    # L_n = {b | ab ∈ L_n-1 and a ∈ C} U {b | ab ∈ C and a ∈ L_n-1}
    L_inf = set()
    L_prev = L1
    L_history = [set(), L1]  # To detect periodicity

    while True:
        L_n = set()
        
        # {b | ab ∈ L_n-1 and a ∈ C}
        for a in C:
            for ab in L_prev:
                if ab.startswith(a):
                    L_n.add(ab[len(a):])
        
        # {b | ab ∈ C and a ∈ L_n-1}
        for a in L_prev:
            for ab in C:
                if ab.startswith(a):
                    L_n.add(ab[len(a):])
        
        # Add L_n to L_inf
        L_inf.update(L_n)
        
        # Check for periodicity  
        # exit condition 1: looking if a word of L_n is in C
        for el in L_n:
            if el in C:
                break

        # exit condition 2 : check if L_n is equal to another previous set 
        if L_n in L_history:
            break

        # exit condition3: if the size of L_n is 0
        if len(L_n) == 0:
            break
        
        L_history.append(L_n)
        L_prev = L_n

    # Step 3: Check if the sets C and L_inf are disjoint
    return len(C.intersection(L_inf)) == 0

# Test data
A = ['a', 'b', 'c', 'd']
C1 = {'a': '11', 'b': '0', 'c': '101', 'd': '100'}
C2 = {'a': '1', 'b': '0', 'c': '10', 'd': '01'}

# Test the function
print("Is C1 uniquely decodable?", is_uniquely_decodable(A, C1))
print("Is C2 uniquely decodable?", is_uniquely_decodable(A, C2))
