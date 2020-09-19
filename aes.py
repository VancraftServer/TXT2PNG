'''
AES加密/解密模块
'''
from Crypto.Cipher import AES
import random
import base64


def pkcs7padding(text):
    bs = AES.block_size
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    return text + padding_text


def pkcs7unpadding(text):
    length = len(text)
    unpadding = ord(text[length - 1])
    return text[0: length - unpadding]


def encrypt(key, content):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        iv = key_bytes
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    except:
        print('Failed!')
        return True
    content_padding = pkcs7padding(content)
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result


def decrypt(key, content):
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    encrypt_bytes = base64.b64decode(content)
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    try:
        result = str(decrypt_bytes, encoding='utf-8')
        result = pkcs7unpadding(result)
    except:
        print('Failed!')
        return True
    else:
        return result
