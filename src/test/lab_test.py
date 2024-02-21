# src/test/test_lab.py
import unittest
from io import StringIO
from contextlib import redirect_stdout
from ..main.lab import (
    demonstrate_integer,
    demonstrate_float,
    demonstrate_boolean,
    demonstrate_sequence,
    demonstrate_set,
    demonstrate_dictionary,
    demonstrate_variable_scope,
)

class TestLab(unittest.TestCase):
    def test_demonstrate_integer(self):
        # Test if demonstrate_integer function prints an integer value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_integer()
            output = buffer.getvalue()
            self.assertIn("Integer:", output)  # Check if "Integer:" is printed

    def test_demonstrate_float(self):
        # Test if demonstrate_float function prints a float value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_float()
            output = buffer.getvalue()
            self.assertIn("Float:", output)  # Check if "Float:" is printed

    def test_demonstrate_boolean(self):
        # Test if demonstrate_boolean function prints a boolean value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_boolean()
            output = buffer.getvalue()
            self.assertIn("Boolean:", output)  # Check if "Boolean:" is printed

    def test_demonstrate_sequence(self):
        # Test if demonstrate_sequence function prints a string, tuple, and list
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_sequence()
            output = buffer.getvalue()
            self.assertIn("String:", output)  # Check if "String:" is printed
            self.assertIn("Tuple:", output)  # Check if "Tuple:" is printed
            self.assertIn("List:", output)   # Check if "List:" is printed

    def test_demonstrate_set(self):
        # Test if demonstrate_set function prints a set value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_set()
            output = buffer.getvalue()
            self.assertIn("Set:", output)  # Check if "Set:" is printed

    def test_demonstrate_dictionary(self):
        # Test if demonstrate_dictionary function prints a dictionary value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_dictionary()
            output = buffer.getvalue()
            self.assertIn("Dictionary:", output)  # Check if "Dictionary:" is printed

    def test_demonstrate_variable_scope(self):
        # Test if demonstrate_variable_scope function prints the global variable correctly
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_variable_scope()
            output = buffer.getvalue()
            self.assertIn("Outside function1 - global_var:", output)  # Check if "Outside function1 - global_var:" is printed

if __name__ == '__main__':
    unittest.main()
