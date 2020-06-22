import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# This code generates private key and public key pairs
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()


pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)


dir_path = os.path.dirname(os.path.realpath(__file__))

# Save public key and private key
pri_key_file = os.path.join(dir_path,"Personal-keys","private_key.pem")
with open(pri_key_file, 'wb') as f:
    f.write(pem)


pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
pub_key_file = os.path.join(dir_path,"Personal-keys","public_key.pem")
with open(pub_key_file, 'wb') as f:
    f.write(pem)