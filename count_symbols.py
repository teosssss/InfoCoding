
def count_symbol(a: str, S: str) -> int:
    """
    Count the number of times a character appears in a string.

    Args:
    a (str): The character to search for.
    S (str): The string to search in.

    Returns:
    int: The number of times 'a' occurs in 'S', or 0 if 'a' is not in 'S'.

    Time Complexity: O(n), where n is the length of string S.
    Space Complexity: O(1), as we only use a single counter variable.
    """
    # Check if the input character 'a' is actually a single character
    if len(a) != 1:
        raise ValueError("The first argument 'a' must be a single character.")

    # Initialize a counter for occurrences
    count = 0

    # Iterate through each character in the string S
    for char in S:
        # If the current character matches 'a', increment the counter
        if char == a:
            count += 1

    # Return the final count
    return count

# Test data
test_cases = [
    ('a', 'banana'),  # Expected output: 3
    ('z', 'banana'),  # Expected output: 0
    ('o', 'Hello, World!'),  # Expected output: 2
    (' ', 'Hello, World!'),  # Expected output: 1
    ('l', 'Hello, World!'),  # Expected output: 3
]

# Run test cases
for a, S in test_cases:
    result = count_symbol(a, S)
    print(f"count_symbol('{a}', '{S}') = {result}")


