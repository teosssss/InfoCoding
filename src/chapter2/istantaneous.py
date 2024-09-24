def is_istantaneous(source_alphabet, code_scheme):
    """
    Determines whether a given coding scheme is instaneous.

    Using Theorem 2.4.8. Equivalence condition for instantaneous codes
    A code C is instantaneous if and only if it is a prefix code. 

    Args:
    source_alphabet (list): List of characters in the source alphabet.
    code_scheme (dict): Dictionary mapping source characters to binary codes.

    Returns:
    bool: True if the code is instantaneous, False otherwise.

    Time complexity: O(n^2) where n is the size of the code, m is the length of the longest string, 
                     and i is the number of iterations until periodicity is detected
    Space complexity: O(1) no auxiliary space needed
    """
    # Convert the code scheme to a set of codewords
    C = list(set(code_scheme.values()))
    
    # Check for each element if it's a prefix of other elements
    for i,el1 in enumerate(C):
        for el2 in C[i:]:
            if (el1.startswith(el2) or el2.startswith(el1)) and el1 != el2:
                return False


    return True

# Test data
A = ['a', 'b', 'c', 'd']
C1 = {'a': '11', 'b': '0', 'c': '101', 'd': '100'}
C2 = {'a': '1', 'b': '0', 'c': '10', 'd': '01'}
C3 = {'a': '1', 'b': '0'}

# Test the function
print("Is C1 instantanous?", is_istantaneous(A, C1))
print("Is C2 instantaneous?", is_istantaneous(A, C2))
print("Is 3 instantaneous?", is_istantaneous(A, C3))
