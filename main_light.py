from math import floor, sqrt
from random import randint

# 使用内置的G和P
G, P = (2, 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559)
# print(f"\nG = 【{G}】, P = 【{P}】\n")

# 选择随机数
with open('light.txt', 'r+') as f:
    A = input('填写私钥(大小控制在10万内)，或回车使用上次的私钥：')
    if A == '':
        A = f.readline()
    else:
        f.write(A+'\n')
A = int(A)
print(f"您的私钥为：{A}，请不要透露")

# 计算中间结果
AA = G ** A % P
print(f"您的公钥计算如下，请随意发布：\n{AA}\n")

# 计算共享密钥
while True:
    BB = int(input("请输入对方的公钥："))
    if BB < P and BB >= 1:
        break
    print("输入不合法，请重新输入")
key = BB ** A % P
print("通讯建立成功！")
# print(f"共享密钥是：{key}")

# 进行加密和解密消息
while True:
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
            k = 0
            while KEY < int(secret):
                KEY *= 2
                k += 1
            secret = str(len(str(k))) + str(k) + str(int(secret) ^ KEY)
            print('\n加密完成\n\n', secret, sep='')
            print()

        # 解密信息
        elif mission == 'd':
            secret = input("输入需要解密的消息：\n")
            nk = int(secret[0])
            k = int(secret[1: nk+1])
            KEY = key * 2 ** k
            secret = int(secret[nk+1:])
            t = str(secret ^ KEY)[1:]
            text = ''
            for i in range(int(len(t)/5)):
                text += chr(int(t[5*i: 5*i+5]))
            print("\n解密完成：\n\n", text, sep='')
            print()

        elif mission == 'q':
            input('Good Luck!')
            quit()
        mission = input('加密(e) / 解密(d) / 退出(q)\n')
