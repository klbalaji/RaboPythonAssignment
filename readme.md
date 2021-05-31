> Project title

Risk Model management IT Python assessment

> Project description

This project implements part of a text processing library. My task is to create and test class which implements two interfaces - 
 'IWordFrequency'  and 'IWordFrequencyAnalyzer' 

	interface IWordFrequency 
	{
		string Word   { get; }
		int Frequency { get; }
	}

	interface IWordFrequencyAnalyzer 
	{
		int calculate_highest_frequency(string text);
		int calculate_frequency_for_word(string text, string word);
		IList<IWordFrequency> calculate_most_frequent_n_words(string text, int n);
	}
        
> Directory Structure

	RaboPythonAssignment
	├── src                    # python package
	│   ├── __init__.py        # to make directory into package
	│   ├── text_process.py    # implements IWordFrequency and IWordFrequencyAnalyzer interfaces
	│    
	├── test # test directory 
	│   │  
	│   ├── __init__.py
	│   ├── conftest.py  		   # contains text fixtures   
	│   ├── test_highest_frequency.py  # to test highest frequency method in CWordFrequencyAnalyzer class
	│   ├── test_most_freq_n_words.py  # to test most frequency n words method in CWordFrequencyAnalyzer class
	│   └── test_freq_specific_word.py # to test frequency of specific word method in CWordFrequencyAnalyzer class
	│
	├── __init__.py 
	├── app.py  			   # contains flask app interface for user
	└── README.md			
	└── test_cases_res_ss.png

> Installation required

	Use of 3rd Party Python Libraries
	1. Flask 2.0.1
	2. pytest 6.2.4

	Note :
	Please mimic folder/files structure as given in above directory_structure
	python 3.8.8 is used for developing this project

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest & flask

```bash
pip install pytest
pip install flask
```

> Usage sample

```python
import pytest
import text_process

@pytest.fixture
def obj_creation():
    return text_process.CWordFrequencyAnalyzer()

```

> references

test_cases_res_ss.png - screenshot of test cases of all test modules using 'pytest -v' terminal


> This projects supports user interaction interface

	app.py a flask application
	after running app.py , flask application is hosted on localhost (127.0.0.1) and port number 5000

	app supports only 3 url routes for 3 different functions, text refers to input text, word refers to the group of 	
	alphabetic chars for which frequency has to be found from text, n : number of most common words from text to be 	
	found, user can use url via browser or any request package

	127.0.0.1:5000/calculate_highest_frequency/<text> for getting the highest frequency from the text
	try example 127.0.0.1:5000/calculate_highest_frequency/The sun shines over the lake
	127.0.0.1:5000/calculate_frequency_for_word/<text>/<word> for getting the frequency for the word from given text
	try example 127.0.0.1:5000/calculate_frequency_for_word/The sun shines over the lake/the
	127.0.0.1:5000/calculate_most_frequent_n_words/<text>/<n> for getting the most frequent n words
	try example 127.0.0.1:5000/calculate_most_frequent_n_words/The sun shines over the lake/2
	user will get appropriate string response as a result after using any of the above mentioned route

	Note: 
		input text and word should be in unicode format in query string for above url
