# src/main/lab.py

def demonstrate_integer():
    """
    This function demonstrates the integer data type in Python.

    Create an integer variable named 'my_integer' and assign it any integer value.
    An integer is a whole number without any decimal points.
    """

    my_integer = None  # Assign any integer value to 'my_integer'
    print("Integer:", my_integer)


def demonstrate_float():
    """
    This function demonstrates the float data type in Python.
    
    Create a float variable named 'my_float' and assign it any floating-point value.
    A float is a number that has both an integer and fractional part, separated by a decimal point.
    """

    my_float = None  # Assign any floating-point value to 'my_float'
    print("Float:", my_float)


def demonstrate_boolean():
    """
    This function demonstrates the boolean data type in Python.
    
    Create a boolean variable named 'my_boolean' and assign it either True or False.
    A boolean represents one of two values: True or False.
    """

    my_boolean = None  # Assign either True or False to 'my_boolean'
    print("Boolean:", my_boolean)


def demonstrate_sequence():
    """
    This function demonstrates sequence data types in Python: string, tuple, and list.
    
    Create variables named 'my_string', 'my_tuple', and 'my_list' for string, tuple, and list respectively.
    Assign any values of these types to the variables.
    """

    # String: A sequence of characters enclosed within single or double quotes
    my_string = None

    # Tuple: An immutable sequence of elements, separated by commas and enclosed within parentheses
    my_tuple = None

    # List: A mutable sequence of elements, separated by commas and enclosed within square brackets
    my_list = None

    print("String:", my_string)
    print("Tuple:", my_tuple)
    print("List:", my_list)


def demonstrate_set():
    """
    This function demonstrates the set data type in Python.
    
    Create a set variable named 'my_set' and assign it any set value.
    A set is an unordered collection of unique elements enclosed within curly braces.
    """

    my_set = None  # Assign any set value to 'my_set'
    print("Set:", my_set)


def demonstrate_dictionary():
    """
    This function demonstrates the dictionary data type in Python.
    
    Create a dictionary variable named 'my_dict' and assign it any dictionary value.
    A dictionary is a collection of key-value pairs enclosed within curly braces,
    with keys and values separated by a colon.
    """

    my_dict = None  # Assign any dictionary value to 'my_dict'
    print("Dictionary:", my_dict)


def demonstrate_variable_scope():

    """
    This function demonstrates variable scope in Python.
    
    Scope:
    Scope refers to the visibility and accessibility of variables within a program. In Python, variables can have different scopes, 
    which determine where they can be accessed and modified. Understanding variable scope is crucial for writing maintainable and 
    bug-free code.
    
    Local Scope:
    Local scope refers to the scope of variables defined within a particular function or block of code. Variables defined within 
    a function have local scope, meaning they can only be accessed and modified within that function. These variables are not 
    visible to code outside the function and are destroyed once the function completes its execution.
    
    Global Scope:
    Global scope refers to the scope of variables defined outside of any function or block of code. Global variables are accessible 
    and modifiable from anywhere within the program, including within functions. However, when modifying global variables from 
    within a function, it's essential to use the 'global' keyword to explicitly declare that the variable is in the global scope.
    
    
    Instructions:
    1. Observe the error message generated when attempting to print local_var1 inside function1.
    2. Correct the error to successfully print local_var1 inside function1.
    3. Understand the concept of variable scope in Python and how it affects accessing variables inside nested functions.
    """

    # Global variable declaration
    global_var = "I am a global variable"

    def function1():
        """
        This nested function demonstrates variable scope within nested functions.
        
        Challenge:
        Correct the error to print local_var1 inside this function.
        
        Instructions:
        Identify and fix the error preventing the printing of local_var1 inside this function.
        """

        # Local variable declaration within function1
        local_var1 = "I am local to function1"
        print("Inside function1 - global_var:", global_var)
        

    function1()  # Call function1 to demonstrate variable scope
    print("Inside function1 - local_var1:", local_var1)  # Corrected error
    print("Outside function1 - global_var:", global_var)