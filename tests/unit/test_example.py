"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from pyospackage_mhowes.example import add_numbers, subtract_numbers, add_list_of_numbers

def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_subtract_numbers():
    """
    Test that substract_numbers works as expected.
    """
    out = subtract_numbers(3, 5)
    expected_out = -2
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_list_of_numbers():
    """
    Test that test_add_list_of_numbers works as expected.
    """
    out = add_list_of_numbers([3, 5])
    expected_out = 8
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_list_of_numbers_with_empty_list():
    """
    Test that test_add_list_of_numbers works on edge case of empty list.
    """
    out = add_list_of_numbers([])
    expected_out = 0
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_add_list_of_numbers_with_singleton():
    """
    Test that test_add_list_of_numbers works on edge case of singleton.
    """
    out = add_list_of_numbers([2])
    expected_out = 2
    assert out == expected_out, f"Expected {expected_out} but got {out}"