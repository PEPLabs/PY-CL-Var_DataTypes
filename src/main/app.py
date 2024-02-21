# src/main/app.py
from lab import (
    demonstrate_integer,
    demonstrate_float,
    demonstrate_boolean,
    demonstrate_sequence,
    demonstrate_set,
    demonstrate_dictionary,
    demonstrate_variable_scope,
)

if __name__ == "__main__":
    
    print("--- Integer ---")
    demonstrate_integer()
    
    print("--- Float ---")
    demonstrate_float()
    
    print("--- Boolean ---")
    demonstrate_boolean()
    
    print("--- Sequence ---")
    demonstrate_sequence()
    
    print("--- Set ---")
    demonstrate_set()
    
    print("--- Dictionary ---")
    demonstrate_dictionary()
    
    print("--- Variable Scope ---")
    demonstrate_variable_scope()
