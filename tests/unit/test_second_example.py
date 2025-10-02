"""
Test module for second_example module.
"""

from pyospackage_mhowes.second_example import multiply_numbers

def test_multiply_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = multiply_numbers(1, 2)
    expected_out = 2
    assert  out == expected_out, f"Expected {expected_out} but got {out}"