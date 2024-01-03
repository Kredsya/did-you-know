# You need to install 'pycryptodomex' with pip.
# document : https://www.pycryptodome.org/src/cipher/classic#cbc-mode

import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

with open('flag.txt', 'rb') as f:
    flag = f.readline()

with open('CREDENTIAL/key.txt', 'rb') as f:
    key = f.readline()

aes = AES.new(key, AES.MODE_CBC)
ct_bytes = aes.encrypt(pad(flag, AES.block_size))

iv = b64encode(aes.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

result = json.dumps({'iv':iv, 'ciphertext':ct})
with open('output.txt', 'w') as f:
    f.write(result)