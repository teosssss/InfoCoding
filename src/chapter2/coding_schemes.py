import os

def define_code(source_alphabet, code_mapping):
    """
    Defines and stores a coding scheme using a dictionary data structure.

    Args:
        source_alphabet (str): The source alphabet, consisting of alphanumeric characters.
        code_mapping (dict): A dictionary mapping characters from the source alphabet to their corresponding binary code.

    Returns:
        dict: A dictionary containing the coding scheme.
    """
    # Validate the source alphabet
    if not all(char.isalnum() for char in source_alphabet):
        raise ValueError("Source alphabet must contain only alphanumeric characters.")

    # Load existing coding schemes from files
    coding_schemes = load_coding_schemes()

    # Check if the current coding scheme already exists
    if source_alphabet in coding_schemes:
        print(f"Coding scheme for source alphabet '{source_alphabet}' already exists.")
        return coding_schemes[source_alphabet]

    # Store the new coding scheme
    coding_schemes[source_alphabet] = code_mapping
    save_coding_schemes(coding_schemes)

    print(f"New coding scheme for source alphabet '{source_alphabet}' has been saved.")
    return code_mapping

def load_coding_schemes():
    """
    Loads existing coding schemes from files.

    Returns:
        dict: A dictionary containing the loaded coding schemes.
    """
    coding_schemes = {}
    for filename in os.listdir("coding_schemes"):
        if filename.endswith(".txt"):
            with open(os.path.join("coding_schemes", filename), "r") as file:
                source_alphabet = filename[:-4]
                code_mapping = eval(file.read())
                coding_schemes[source_alphabet] = code_mapping
    return coding_schemes

def save_coding_schemes(coding_schemes):
    """
    Saves the current coding schemes to files.

    Args:
        coding_schemes (dict): The dictionary containing the current coding schemes.
    """
    if not os.path.exists("coding_schemes"):
        os.makedirs("coding_schemes")

    for source_alphabet, code_mapping in coding_schemes.items():
        filename = os.path.join("coding_schemes", f"{source_alphabet}.txt")
        with open(filename, "w") as file:
            file.write(str(code_mapping))



source_alphabet = "abcde"
code_mapping = {
    "a": "00",
    "b": "01",
    "c": "10",
    "d": "11",
    "e": "000"
}

define_code(source_alphabet, code_mapping)