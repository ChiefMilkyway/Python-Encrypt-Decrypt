import os 
from cryptography.fernet import Fernet

#fetch files...
files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "encryption.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("encryption.key", "rb") as encryptionkey:
    key = encryptionkey.read()

print(key)
f = Fernet(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        decrypted_contents = f.decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
