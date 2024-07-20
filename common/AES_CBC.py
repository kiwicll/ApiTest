import base64
import yaml
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class EncryptDate:
    def __init__(self, key, iv):
        self.key = key.encode("utf-8")  # 初始化密钥
        self.iv = iv.encode("utf-8")  # 初始化IV
        self.length = AES.block_size  # 初始化数据块大小
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """填充函数 ，使被加密数据的字节码长度是block_size的整数倍 """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)  # 初始化AES实例
        res = aes.encrypt(self.pad(encrData).encode("utf-8"))
        # base64是网络上最常见用于传输8bit字节码的编码方式之一
        msg = base64.b64encode(self.iv + res).decode("utf-8")  # 将IV和密文一起编码
        return msg

    def decrypt(self, decrData):  # 解密函数
        raw = base64.b64decode(decrData)
        iv = raw[:AES.block_size]  # 提取IV
        encrypted_data = raw[AES.block_size:]  # 提取密文
        aes = AES.new(self.key, AES.MODE_CBC, iv)  # 使用相同的IV初始化AES实例
        msg = self.unpad(aes.decrypt(encrypted_data).decode("utf-8"))
        return msg

# if __name__ == '__main__':
#     # 从YAML文件中读取配置
#     with open('config.yaml', 'r') as file:
#         config = yaml.safe_load(file)
#         key = config['encryption']['key']
#         iv = config['encryption']['iv']
#
#     print("----------------加密------------")
#     data = "tony"  # 数据
#     eg = EncryptDate(key, iv)  # 这里密钥和IV的长度必须是16的倍数
#     res = eg.encrypt(str(data))
#     print(res, end='')
#
#     print("\n------------解密---------")
#     data = res  # 使用上一步加密得到的数据
#     res = eg.decrypt(str(data))
#     print(res, end='')
