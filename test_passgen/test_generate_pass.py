
from passgen import generate_pass
import pytest

import os 
print(os.getcwd())

def test_for_uppercase():
    password = generate_pass.generate_password(8)
    assert any(c.isupper() for c in password)

# ADD MORE TESTS HERE! :)
