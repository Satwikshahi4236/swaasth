from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from ..config import settings


def generate_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Generate encryption key from password using PBKDF2.
    
    Args:
        password: Password to derive key from
        salt: Salt for key derivation
        
    Returns:
        bytes: Derived encryption key
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def encrypt_message(message: str, password: str = None) -> dict:
    """
    Encrypt a message using Fernet symmetric encryption.
    
    Args:
        message: The message to encrypt
        password: Optional password for encryption (uses JWT secret if not provided)
        
    Returns:
        dict: Contains encrypted message and salt
    """
    if password is None:
        password = settings.jwt_secret_key
    
    # Generate random salt
    salt = os.urandom(16)
    
    # Generate key from password
    key = generate_key_from_password(password, salt)
    
    # Create Fernet instance and encrypt
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    
    return {
        "encrypted_message": base64.urlsafe_b64encode(encrypted_message).decode(),
        "salt": base64.urlsafe_b64encode(salt).decode()
    }


def decrypt_message(encrypted_data: dict, password: str = None) -> str:
    """
    Decrypt a message using Fernet symmetric encryption.
    
    Args:
        encrypted_data: Dictionary containing encrypted message and salt
        password: Optional password for decryption (uses JWT secret if not provided)
        
    Returns:
        str: Decrypted message
        
    Raises:
        Exception: If decryption fails
    """
    if password is None:
        password = settings.jwt_secret_key
    
    try:
        # Decode salt and encrypted message
        salt = base64.urlsafe_b64decode(encrypted_data["salt"])
        encrypted_message = base64.urlsafe_b64decode(encrypted_data["encrypted_message"])
        
        # Generate key from password
        key = generate_key_from_password(password, salt)
        
        # Create Fernet instance and decrypt
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message)
        
        return decrypted_message.decode()
    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")


def generate_secure_token() -> str:
    """
    Generate a secure random token for various purposes.
    
    Returns:
        str: Base64 encoded secure token
    """
    return base64.urlsafe_b64encode(os.urandom(32)).decode()


def hash_sensitive_data(data: str) -> str:
    """
    Hash sensitive data using SHA256.
    
    Args:
        data: The data to hash
        
    Returns:
        str: Hexadecimal hash of the data
    """
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data.encode())
    return digest.finalize().hex()