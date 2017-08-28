# -*- coding: UTF-8 -*-

import functions
from functions import file_encrypt, file_decrypt, printCN, raw_inputCN

while 1:                                             # 相当于主程序了。。。
    printCN("这是一个加解密文件程序，请按照提示输入！\n")
    printCN("请选择：\n1.加密文件  2.解密文件 3.退出")
    select = input()
    if select == 1:
        file_encrypt()
        break
    elif select == 2:
        file_decrypt()
        break
    else:
        break

