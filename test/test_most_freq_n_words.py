"""

Module      : test_most_freq_n_words.py
purpose     : This test module to test the calculate_most_frequent_n_words method with different scenarios
Author      : Balaji Pandiyan K
version     : 0.1
Modified    : 31-05-2021

"""

# importing modules
import pytest

""" 
    Test case 1: validate most frequent 5 words - check the order by frequency 
    Test case 2: validate most frequent 0 words
    Test case 3: validate most frequent 8 words -  arrange alphabetic if frequency is same 
    Test case 4: validate when text is None and n=1
    Test case 5: validate whether n is integer
    Test case 6: validate greater n value than available list items

    Input   : text: str (input string), n: int (no. of most frequent words)
    Output  : expected: list[IWordFrequency] - list the words and its frequency in an ordered way
"""


@pytest.mark.parametrize(
    "text,n,expected",
    [
        (
            "The Sun shine over ThE lake",
            5,
            [("the", 2), ("lake", 1), ("over", 1), ("shine", 1), ("sun", 1)],
        ),
        ("sun rises at east, sun sets at west", 0, []),
        (
            "Let's meet at noon and near park",
            8,
            [
                ("and", 1),
                ("at", 1),
                ("let", 1),
                ("meet", 1),
                ("near", 1),
                ("noon", 1),
                ("park", 1),
                ("s", 1),
            ],
        ),
        (None, 1, []),
        ("Sun is bright", "", []),
        ("Knowledge is power", 4, []),
    ],
)
def test_calculate_most_frequent_n_words(obj_creation, text, n, expected):
    assert obj_creation.calculate_most_frequent_n_words(text, n) == expected
