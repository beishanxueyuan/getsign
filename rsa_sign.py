# -*- coding: utf-8 -*-
import rsa
import base64

def get_pwd(pwd):
    public_key_str = """公钥！！"""

    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key_str.encode())

    data = pwd.encode()
    encrypted_data = rsa.encrypt(data, public_key)
    base64_encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    return base64_encoded_data

# print(get_pwd("9"))
f = open("要加密的文件",encoding='utf-8')
while True:
    line = f.readline()
    if line:
        with open('/Users/chenguang/code/test/example.txt', 'a') as f2:
            f2.write(get_pwd(line.replace('\n','').replace(' ',''))+'\n')
    else:
        break
f.close()
