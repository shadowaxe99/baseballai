```python
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Load the secret key from environment variable
SECRET_KEY = os.getenv('SECRET_KEY')

# Create a cipher suite
cipher_suite = Fernet(SECRET_KEY)

def encrypt_data(data):
    """
    Function to encrypt data
    """
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Function to decrypt data
    """
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data
```