from math import floor, sqrt


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


# 单机测试版
if S == 1:
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
    # 计算公开数
    while True:
        A = int(input("请输入一个小于P的正整数："))
        if A < P and A > 1:
            break
        print("输入不合法，请重新输入")

    # 计算中间结果
    AA = G ** A % P
    print(f"计算得 {AA}，请将这个公开数告知对方")

    # 计算共享密钥
    while True:
        BB = int(input("请输入对方的公开数："))
        if BB < P and BB >= 1:
            break
        print("输入不合法，请重新输入")
    key = BB ** A % P
    print(f"共享密钥是：{key}")

