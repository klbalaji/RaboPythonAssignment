"""

Module      : text_process.py
purpose     : this module to implement IWordFrequency and IWordFrequencyAnalyzer interfaces to do text processing
              and to do manipulations such as calculate highest frequency of words in the text,
              calculate frequency of specific words and calculate most frequent n words.
Author      : Balaji Pandiyan K
version     : 0.8
Modified    : 31-05-2021

"""


# import modules
import re
from abc import ABC, abstractmethod
from operator import itemgetter
from typing import Dict


class IWordFrequency(ABC):
    """
    Define 'IWordFrequency' interface

    Attributes:
        Word: str
        Frequency: int
    """

    Word: str
    Frequency: int


class CWordFrequency(IWordFrequency):
    """
    CWordFrequency class for text process operations,
    which implements 'IWordFrequency' interface and
    implements 'get_word_freq' method.

    Attributes:
        None
    """

    # get_word_freq(self, text: str) ->  Dict
    @classmethod
    def get_word_freq(cls, text: str) -> Dict:
        """
        This method segregate words from input string and identify words are valid alphabets
        identify frequency for each word and store it in word_freq_dict

        Parameters:
            text (str): Input text

        Returns:
            word_freq_dict (Dict) : Dict of words and its frequency
        """
        if text is None:
            text = ""
        if text != "" or isinstance(text, str):
            # define alphabet pattern
            pattern = r"[a-zA-Z]+"

            # break the string into list of words as only alphabets
            word_list = re.findall(pattern, text)
            word_list = [word.lower() for word in word_list]

            # sort the words in the list
            unique_words = list(set(word_list))
            unique_words.sort()

            word_freq_dict = {}  # initialize frequency dictionary

            # utilize IWordFrequency interface attribute 'Word'
            for IWordFrequency.Word in unique_words:
                # utilize IWordFrequency interface attribute 'frequency'
                # frequency calculation for each words
                IWordFrequency.Frequency = word_list.count(IWordFrequency.Word)

                # frequency dictionary creation
                word_freq_dict[IWordFrequency.Word] = IWordFrequency.Frequency

            """ return frequency dictionary """
            return word_freq_dict
        else:
            return {}


class IWordFrequencyAnalyzer(ABC):
    """
    Define 'IWordFrequencyAnalyzer' interface

    Methods:
        calculate_highest_frequency(self, text: str) -> int
        calculate_frequency_for_word(self, text: str, word: str) -> int
        calculate_most_frequent_n_words(self, text: str, n: int) -> list
    """

    @abstractmethod
    def calculate_highest_frequency(self, text: str) -> int:
        pass

    @abstractmethod
    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        pass

    @abstractmethod
    def calculate_most_frequent_n_words(self, text: str, n: int) -> list:
        pass


class CWordFrequencyAnalyzer(IWordFrequencyAnalyzer, CWordFrequency):
    """
    CWordFrequencyAnalyzer class for text manipulations,
    which implements 'IWordFrequencyAnalyzer' interface and
    use 3 methods of it. Also inherits class 'CWordFrequency'

    Attributes:
        None
    """

    def calculate_highest_frequency(self, text: str) -> int:
        """
        This method calculates highest frequency of words in input text

        Parameters:
            text (str): Input text

        Returns:
            high_frequency (int) :
        """

        # identify frequency of all words in input text
        freq_dict = super().get_word_freq(text)

        # find max on non-empty dict
        if freq_dict:
            # highest frequency calculation
            return max(freq_dict.values())
        else:
            return 0

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        """
        This method calculates highest frequency of specific word

        Parameters:
            text (str): Input text,
            word (str): Input word

        Returns:
            high_frequency (int) : highest frequency of specific word identification
        """
        if word is None:
            word = ""
        if word != "" and isinstance(word, str) and word.isalpha():
            # identify frequency of all words in input text
            freq_dict = super().get_word_freq(text)

            # frequency for specific word
            if freq_dict and word in freq_dict:
                return freq_dict[word]
        return 0

    def calculate_most_frequent_n_words(self, text: str, n: int) -> list:
        """
        This method calculates most frequent n words from input text string

        Parameters:
            text (str): Input text,
            n (int): Input n

        Returns:
            most frequent words (list) : list out most frequent given n words from input text
        """
        # identify frequency of all words in input text
        if n is not None and isinstance(n, int):
            freq_dict = super().get_word_freq(text)

            freq_list = []
            # sorting dictionary by values
            # creating list by sorting
            if freq_dict:
                freq_list = sorted(freq_dict.items(), key=itemgetter(1), reverse=True)
            # return most_frequent n words
            if 0 < n <= len(freq_list):
                return freq_list[:n]
        return []
