from math import floor, sqrt
from random import randint


def isPrime(p):
    if p == 1 or p % 10 == 2:
        return 0
    if p == 3:
        return 1

    for i in range(2, floor(sqrt(p))):
        if p % i == 0:
            return 0
    return 1


# 选择软件状态
while True:
    S = int(input("单机测试版：1，双人版交流助手：2\n请输入："))
    if S == 1 or S == 2:
        break
    print("输入错误请重新输入")


# 单机测试版
if S == 1:
    # 获取P
    while(True):
        P = int(input("请输入P值："))
        if isPrime(P):
            break
        print('输入的不是素数，请重新输入')

    # 获取P的原根G
    g = []
    for i in range(2, P):
        t = True
        for j in range(2, P-1):
            if i ** j % P == 1:
                t = False
                break
        if t:
            g.append(i)
    print(g)
    while True:
        G = int(input("请输入选择的G："))
        if G in g:
            break
        print("所选择的G不在可用列表中，请重新选择")
    print(f"G = {G}, P = {P}")

    # 获得A、B
    while True:
        A = int(input("请输入你的A："))
        if A < P and A > 1:
            break
        print("输入不合法，请重新输入")
    while True:
        B = int(input("请输入你的B："))
        if B < P and B > 1:
            break
        print("输入不合法，请重新输入")

    # 计算AA，BB
    AA = G ** A % P
    BB = G ** B % P
    print(f"计算得AA = {AA}，BB = {BB}")

    # 计算共享密钥
    key1 = BB ** A % P
    key2 = AA ** B % P
    if key1 == key2:
        print(f"共享密钥是：{key1}")
    else:
        print(key1)
        print(key2)


# 双人交流助手
elif S == 2:
    # 获取P
    while(True):
        P = int(input("请输入P值："))
        if isPrime(P):
            break
        print('输入的不是素数，请重新输入')

    # 获取P的原根G
    t = True
    while t:
        t = False
        G = input("请输入已选择的G，或按回车自动选择：")
        if G == '':
            t2 = True
            while t2:
                t2 = False
                G = randint(2, P-1)
                for i in range(2, P-1):
                    if int(G) ** i % P == 1:
                        t2 = True
                        break
        G = int(G)
        for i in range(2, P-1):
            if int(G) ** i % P == 1:
                print("该G不可用，请重新选择")
                t = True
                break
    print(f"\nG = 【{G}】, P = 【{P}】\n")
  
    
    # 选择随机数
    A = randint(2, P)
    # print(f"取得随机数为：{A}")

    # 计算中间结果
    AA = G ** A % P
    print(f"计算得【{AA}】，请将这个公开数告知对方\n")

    # 计算共享密钥
    while True:
        BB = int(input("请输入对方的公开数："))
        if BB < P and BB >= 1:
            break
        print("输入不合法，请重新输入")
    key = BB ** A % P
    print("共享密钥计算完成！")
    print(f"共享密钥是：{key}")

    # 进行加密和解密消息
    while(input("是否继续通信？（y/n）") != 'n'):
        mission = input('加密(e) / 解密(d) / 退出(q)\n')
        while True:
            # 加密信息
            if mission == 'e':
                text = input("输入需要加密的消息：\n")
                secret = ''
                for i in text:
                    _c = str(ord(i))
                    while len(_c) < 5:
                        _c = '0' + _c
                    secret += _c
                secret = '1' + secret
                KEY = key
                k = 1
                while KEY < int(secret):
                    KEY *= key
                    k += 1
                secret = str(len(str(k))) + str(k) + str(int(secret) ^ KEY)
                print('\n加密完成\n\n', secret, sep='')
                print()

            # 解密信息
            elif mission == 'd':
                secret = input("输入需要解密的消息：\n")
                nk = int(secret[0])
                k = int(secret[1: nk+1])
                KEY = key ** k
                secret = int(secret[nk+1: ])
                t = str(secret ^ KEY)[1: ]
                text = ''
                for i in range(int(len(t)/5)):
                    text += chr(int(t[5*i: 5*i+5]))
                print("\n解密完成：\n\n", text, sep='')
                print()

            elif mission == 'q':
                input('Good Luck!')
                quit()
            mission = input('加密(e) / 解密(d) / 退出(q)\n')
    
    input('Good Luck!')

