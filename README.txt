1. Key generation

To generate private and public key pairs use keygen.py.
The keys will be stored in 'Personal-keys' forlder


2. Encryption

Save the public of the person you are trying to send a message to in the 'Others-keys' folder
Save all message files as .txt files in the 'Messages' folder
Run encrypt.py
The encrypted messages will be in 'Encrypted-messages' folder

Remark: This works for multiple files at the same time


3. Decryption

Make sure that the keys in the 'Personal-keys' folder is the one used to encrypt the message.
Save the encrypted messages on 'Encrypted-messages' folder
Run decrypt.py
The decrypted messages will be in 'Decrypted-messages' folder.