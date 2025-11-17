from passlib.context import CryptContext

# -------------------------------
# Password hashing configuration
# -------------------------------
# Using Argon2 algorithm which supports long passwords
# and is considered very secure.
pwd_context = CryptContext(
    schemes=["argon2"],  # Can replace/add others like "sha256_crypt"
    deprecated="auto"   # Automatically marks old algorithms as deprecated
)

# -------------------------------
# Function: hash_password
# -------------------------------
def hash_password(password: str) -> str:
    """
    Hashes a plaintext password using Argon2.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password as a string that can be stored in the database.

    Notes:
        - Supports passwords longer than 72 bytes.
        - Uses a secure, salted hashing algorithm (Argon2).
    """
    return pwd_context.hash(password)

# -------------------------------
# Function: verify_password
# -------------------------------
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password to check.
        hashed_password (str): The stored hashed password.

    Returns:
        bool: True if the password matches the hash, False otherwise.

    Notes:
        - Works for passwords of any length.
        - Automatically handles salt and algorithm verification.
    """
    return pwd_context.verify(plain_password, hashed_password)

# -------------------------------
# Function: get_password_hash
# -------------------------------
# Optional alias function if you want a clearer naming convention
def get_password_hash(password: str) -> str:
    """
    Alias for hash_password for semantic clarity.
    """
    return hash_password(password)
