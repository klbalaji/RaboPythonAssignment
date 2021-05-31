"""

Module      : test_freq_specific_word.py
purpose     : This test module to test the calculate_frequency_for_word method with different scenarios
Author      : Balaji Pandiyan K
version     : 0.1
Modified    : 31-05-2021

"""


# importing modules
import pytest

""" 
    Test case 1: validate specific word available in string and their frequency 
    Test case 2: validate specific word not available
    Test case 3: validate input word is empty
    Test case 4: validate input word is not alphabet
    Test case 5: validate input word and text are empty
    Test case 6: validate input word is string 

    Input   : text: str (input string), word: str (specific word)
    Output  : excepted: int (frequency of specific word in input string)
"""


@pytest.mark.parametrize(
    "text,word,expected",
    [
        (
            "The Sun shine over ThE2 lake$, SuN is very bright, sun-light gives us vitamin D",
            "sun",
            3,
        ),
        ("sun rises at east, sun sets at west", "rise", 0),
        ("Be cool like Moon", "", 0),
        ("Think before you ink", "234", 0),
        ("", "", 0),
        ("Super Sun", 1, 0),
    ],
)
def test_calculate_frequency_for_word(obj_creation, text, word, expected):
    assert obj_creation.calculate_frequency_for_word(text, word) == expected
