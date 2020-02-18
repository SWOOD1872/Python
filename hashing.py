import hashlib
import secrets


def hashpw(password, salt):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def comparepw(pw):
    if hashpw(pw, salt) == password:
        return False
    return True


salt = secrets.token_hex(8)
password = hashpw('abc123', salt)

print(comparepw(password))
print(comparepw('abc_123'))