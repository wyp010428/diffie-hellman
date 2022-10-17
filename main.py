from math import floor, sqrt


def isPrime(p):
    if p == 1 | p % 10 == 2:
        return 0
    if p == 3:
        return 1

    for i in range(2, floor(sqrt(p))):
        if p % i == 0:
            return 0
    return 1

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
    print("所选择的G不在可用列表中，请重新选择：")



