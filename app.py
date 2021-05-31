"""
Module  : app.py
purpose : this module provides web interface using flask app to execute
            CWordFrequencyAnalyzer class functions via url routes
"""

# import modules
from flask import Flask
from src import text_process


def create_app():
    """
        Creates flask app defines functions to handle different url routes each function is responsible
        for executing different function of CWordFrequencyAnalyzer class

    Returns
        Instance of flask app
    """

    flask_app = Flask(__name__)
    word_frequency_analyzer = text_process.CWordFrequencyAnalyzer()

    # handle non-existent/invalid url routes
    @flask_app.errorhandler(404)
    def page_not_found(e):
        return "given url route does not exist, or is invalid"

    # to calculate highest frequency
    @flask_app.route("/calculate_highest_frequency/<text>/",
                     methods=['GET', 'POST'])
    def highest_frequency(text):
        """
        receives text from url request and executes
        calculate_highest_frequency() method of
        CWordFrequencyAnalyzer class
        Parameters
        ----------
        text : str
            input text received from user
        Returns
        -------
            : str
            final message for the user
        """
        try:

            result = word_frequency_analyzer.calculate_highest_frequency(text)
            return f"Highest Frequency in the given text is {result}"
        except ValueError as e:
            message = get_exception_message(e)
            return message

    # to calculate frequency for word
    @flask_app.route("/calculate_frequency_for_word/<text>/<word>",
                     methods=['GET', 'POST'])
    def calculate_frequency_for_word(text, word):
        """
        receives text and word from url request and executes
        calculate_frequency_for_word() method of
        CWordFrequencyAnalyzer class
        Parameters

        text : str
            input text received from user
        word : str
            word for which frequency has to be found
        Returns
        -------
            : int
            if error returns 0 otherwise word frequency for specific word
        """
        result = word_frequency_analyzer.calculate_frequency_for_word(text, word)
        return f"Frequency for {word} in the given text is {result}"



    @flask_app.route("/calculate_most_frequent_n_words/<text>/<n>",
                     methods=['GET', 'POST'])
    def calculate_most_frequent_n_words(text, n):
        """
        receives text and n(number in form of string) from url request
        and executes calculate_most_frequent_n_words() method of
        CWordFrequencyAnalyzer class

        Parameters

            text : str
            input text received from user
            n : str
            number of words to be found which are most common

        Returns

            : list
            if error returns empty list otherwise list out most frequent n words
        """

        n=int(n)
        result = word_frequency_analyzer.calculate_most_frequent_n_words(text, n)

        return f"Most frequent {n} words are {result}"



    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run()