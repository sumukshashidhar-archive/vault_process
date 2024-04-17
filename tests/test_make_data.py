"""
Simple way to create new test data, should you need it.
"""
import os

# add current directory to path, so imports work
import sys
sys.path.append(os.getcwd())

# load env
from dotenv import load_dotenv
from src.utils.fileops import write_files

load_dotenv()

VAULT_DIR = os.environ['VAULT']

def delete_all_files():
    for filename in os.listdir(VAULT_DIR):
        file_path = os.path.join(VAULT_DIR, filename)
        os.remove(file_path)
        

def add_a():
    files_content = {
        "a.md": "This is a sample file with a [[cat]] and a [[dog]]. But oh wait, what's this! The cat is now not marked!"
    }
    write_files(files_content, VAULT_DIR)

if __name__ == "__main__":
    delete_all_files()
    add_a()
