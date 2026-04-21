from pwdlib import PasswordHash
from backend import schemas

password_hash = PasswordHash.recommended()

def hash_password(plain):
    return password_hash.hash(plain)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def authenticate_user(db, username: str, password: str, hashed):
    user = get_user(db, username)
    if not user:
        verify_password(password, hashed)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user