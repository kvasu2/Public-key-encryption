import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# Get file paths
dir_path = os.path.dirname(os.path.realpath(__file__))
enc_mess_path = os.path.join(dir_path,"Encrypted-messages")
inps = sorted(os.listdir(enc_mess_path))


# Get private key
pri_key = os.path.join(dir_path,"Personal-keys","private_key.pem")
with open(pri_key, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )


# Function to encrypt a file
def decrypt_message(dir_path, message_file, private_key):

    # Read message
    enc_message_path = os.path.join(dir_path,"Encrypted-messages",message_file)
    f = open(enc_message_path, 'rb')
    encrypted = f.read()
    f.close()

    
    # Decrypt message
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save decrypted message
    out_path = os.path.join(dir_path,"Decrypted-messages",message_file[:-10]+".txt")
    f = open(out_path, 'wb')
    f.write(original_message)
    f.close()

# Loop to encrypt all messages in "Encrypted-messages"
for f in inps:
    decrypt_message(dir_path,f, private_key)