'''
PNG解密为TXT模块
'''
from PIL import Image
import hashlib
import aes


def decrypt(file, passwdfile, passwd):
    assert str(type(file)) == '<class \'PIL.PngImagePlugin.PngImageFile\'>'
    assert str(type(passwdfile)) == '<class \'PIL.PngImagePlugin.PngImageFile\'>'
    width, height = file.size
    result = []
    passwd_result = []
    for i in range(passwdfile.size[1]):
        for j in range(passwdfile.size[0]):
            red, green, blue = passwdfile.getpixel((j, i))
            if (blue | green | red) == 0:
                break
            passwd_result.append(chr((green << 8) + blue))
    passwd_result_str = ''.join(passwd_result)
    for i in range(height):
        for j in range(width):
            red, green, blue = file.getpixel((j, i))
            if (blue | green | red) == 0:
                break
            result.append(chr((green << 8) + blue))
    result_str = ''.join(result)
    if hashlib.sha512(passwd.encode('utf-8')).hexdigest() == passwd_result_str:
        try:
            result_str = aes.decrypt(passwd, result_str)
            return_dict = {
                'content': result_str,
                'success': 'yes'
            }
        except:
            return_dict = {
                'content': 'Failed!',
                'success': 'no'
            }
    else:
        return_dict = {
            'content': 'Failed!',
            'success': 'no'
        }
    return return_dict
