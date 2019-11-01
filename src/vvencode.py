from crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

apiKey = "VVuucskey201906".encode('utf-8') # 16位
secret = "VVuucs_sec201906".encode('utf-8')


def encode(word):
    mode = AES.MODE_CBC
    cryptos = AES.new(apiKey, mode, secret)
    cipher_text = cryptos.encrypt(word)   # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串

    return b2a_hex(cipher_text)


if __name__ == '__main__':
    str = '{"mpuId":309,"storeId":208}'
    e = encode(str)
    print(e)