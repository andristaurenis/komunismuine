
from os import getenv 
from os.path import join, dirname
from dotenv import load_dotenv
from sys import stdin
from crypto import decrypt_symetric

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SYMETRIC_KEY = getenv('SYMETRIC_KEY')

print(decrypt_symetric(SYMETRIC_KEY, stdin))
