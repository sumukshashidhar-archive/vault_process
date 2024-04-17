"""
Simple way to create new test data, should you need it.
"""
# load env
from dotenv import load_dotenv
import os
load_dotenv()

VAULT_DIR = os.environ['VAULT']

def add_root_dir_files():
   pass

if __name__ == "__main__":
    raise NotImplementedError
