import sys
import os
from dotenv import load_dotenv
sys.path.append(os.getcwd())
load_dotenv()

import pytest
from src.add_backlinks import wikilink_unmarked

# Test Cases for wikilink_unmarked function
@pytest.mark.parametrize("text, expected", [
    ("Here is a simple link to a [[cat]] and here is a text mentioning cat.", 
     "Here is a simple link to a [[cat]] and here is a text mentioning [[cat]]."),
    ("No links here but needs links for dog and cat", 
     "No links here but needs links for [[dog]] and [[cat]]"),
    ("Edge cases like [[dog]] appearing already should not double link [[dog]].", 
     "Edge cases like [[dog]] appearing already should not double link [[dog]]."),
    ("Check this unique [[case|case]] and case should link", 
     "Check this unique [[case|case]] and [[case]] should link"),
])
def test_wikilink_unmarked(text, expected):
    wikilinks = {"cat", "dog", "case"}
    assert wikilink_unmarked(text, wikilinks) == expected