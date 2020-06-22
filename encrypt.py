import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# Get file paths
dir_path = os.path.dirname(os.path.realpath(__file__))
mess_path = os.path.join(dir_path,"Messages")
inps = sorted(os.listdir(mess_path))


# Get public key
pub_key = os.path.join(dir_path,"Others-keys","public_key.pem")
with open(pub_key, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )


# Function to encrypt a file
def encrypt_message(dir_path,message_file, public_key):

    # Read message
    message_path = os.path.join(dir_path,"Messages",message_file)
    f = open(message_path, 'rb')
    message = f.read()
    f.close()



    # Encrypt message
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted message
    out_path = os.path.join(dir_path,"Encrypted-messages",message_file[:-4]+".encrypted")
    f = open(out_path, 'wb')
    f.write(encrypted)
    f.close()

# Loop to encrypt all messages in "Messages"
for f in inps:
    encrypt_message(dir_path,f, public_key)