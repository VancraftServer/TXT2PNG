from PIL import Image
import decrypt
import encrypt
import sys
import re

if __name__ == '__main__':
    filename = input('Filename?')
    operation = input('Encrypt or Decrypt?')
    passwd = input('Password?')
    if not len(passwd) == 16:
        raise Warning('密码长度错误，请输入长度为16的密码！', len(passwd))
    if operation == 'encrypt':
        try:
            with open(filename, encoding='utf-8') as f:
                try:
                    img = encrypt.encrypt(f, passwd)['img']
                    passwd_img = encrypt.encrypt(f, passwd)['passwd_img']
                    img.save(filename + '.png')
                    passwd_img.save(filename + '_passwd.png')
                except:
                    print('Failed!')
        except:
            print('Failed!')
    elif operation == 'decrypt':
        passwd_filename = re.sub('.png$', '_passwd.png', filename)
        try:
            text = decrypt.decrypt(Image.open(filename, 'r'), Image.open(
                passwd_filename, 'r'), passwd)['content']
            if decrypt.decrypt(Image.open(filename, 'r'), Image.open(passwd_filename, 'r'), passwd)['success'] == 'yes':
                with open(filename + '.txt', 'w', encoding='utf-8') as f:
                    f.write(text)
            else:
                print('Failed!')
        except:
            print('Failed!')
else:
    sys.exit()
