"""

Module      : test_highest_frequency.py
purpose     : This test module to test the calculate_highest_frequency method with different scenarios
Author      : Balaji Pandiyan K
version     : 0.1
Modified    : 31-05-2021

"""


# importing modules
import pytest

""" 
    Test case 1: validate digits are ignored and find highest frequency 
    Test case 2: validate special characters are ignored and find highest frequency
    Test case 3: validate exclusion of digits and special characters from alphabet, find highest frequency
    Test case 4: validate empty text 
    
    Input   : text: str (input string)
    Output  : expected: int - highest frequency of words in the input text
"""


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Be like 1 Bee, 1 picture is worth a 10 hundred words", 1),
        (
            "\tSun rises at east, sun sets at west!\n\tEast or West, Sun is Best!\n",
            3,
        ),
        (
            "\nThe Sun shine over ThE2 lake$, \n*SuN is very bright, \nsun-light gives us vitamin D, \nsun",
            4,
        ),
        ("", 0),
    ],
)
def test_calculate_highest_frequency(obj_creation, text, expected):
    assert obj_creation.calculate_highest_frequency(text) == expected
