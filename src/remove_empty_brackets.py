"""
The idea of this script is to essentially release you from the worry of
having to manually add 
"""
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.getcwd())
load_dotenv()
from src.utils.fileops import read_files, write_files

import re
from typing import Set
import logging

logging.basicConfig(level=logging.DEBUG)


VAULT = os.environ["VAULT"]

def remove_empty_wikilinks(text: str) -> str:
    """
    Removes all empty wikilinks from the given text.
    
    Args:
    text (str): The text from which to remove empty wikilinks.
    
    Returns:
    str: The text with empty wikilinks removed.
    """
    # Regex to find empty wikilinks
    empty_wikilink_pattern = r'\[\[\s*\]\]'
    # Replace empty wikilinks with an empty string
    modified_text = re.sub(empty_wikilink_pattern, '', text)
    return modified_text


if __name__ == "__main__":
    # Read all files in the vault
    files = read_files(VAULT)
    logging.debug(f"Length of files: {len(files)}")
    for filename in files:
        file_content = files[filename][0]
        modified_text = remove_empty_wikilinks(file_content)
        if modified_text != file_content:
            logging.debug(f"Modified file: {filename}")
        files[filename] = modified_text, files[filename][1]
    # Write the modified files back to the vault
    
    write_files(files, VAULT)
