"""
Module      : conftest.py
purpose     : This is test configuration file - entry point where object created for CWordFrequencyAnalyzer class
              to test all 3 modules of CWordFrequencyAnalyzer class
Author      : Balaji Pandiyan K
version     : 0.1
Modified    : 31-05-2021


"""

# import modules
import pytest
from RaboPythonAssignment.src import text_process


@pytest.fixture
def obj_creation():
    return text_process.CWordFrequencyAnalyzer()
