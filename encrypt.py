'''
TXT加密为PNG模块
'''
from PIL import Image
import base64
import hashlib
import math
import aes


def encrypt(file, passwd):
    assert str(type(file)) == '<class \'_io.TextIOWrapper\'>'
    try:
        assert len(passwd) == 16
    except AssertionError:
        print('Failed!')
        return True
    content = file.read()
    content = aes.encrypt(passwd, content)
    str_len = len(content)
    width = math.ceil(str_len ** 0.5)
    img = Image.new('RGB', (width, width), 0x0)
    passwd_sha512 = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
    passwd_img = Image.new('RGB', (len(passwd_sha512), 1), 0x0)
    x, y = 0, 0
    for i in passwd_sha512:
        index = ord(i)
        rgb = (0, (index & 0xFF00) >> 8, index & 0xFF)
        passwd_img.putpixel((x, y), rgb)
        x += 1
    x = 0
    for i in content:
        index = ord(i)
        rgb = (0, (index & 0xFF00) >> 8, index & 0xFF)
        img.putpixel((x, y), rgb)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return {
        'passwd_img': passwd_img,
        'img': img
    }
