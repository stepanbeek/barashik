#Задача 1
def Baiden(P):
    i = 2
    result = []
    while True:
        microbaiden = (i)
        if root_i < P:
            result.append(microbaiden)
        else:
            break
        i += 1   
    return result
P = 5
Putin = Zelenskyi(P)
print(Putin)

#Задача 2
def Omerika (A, B):
    result = []
    for i in range(A+1, B):
        result.append(i)
    return result
A = 3
B = 8
skambaiden = Omerika(A, B)
print(skambaiden)

#Задача 3
def Bidan(A, B):
    result = []
    for i in range(B-1, A, -1):
        result.append(i)
    return result
A = 3
B = 8
bigbaiden = smoalbiden(A, B)
print(bigbaiden)

#Задача 4
def horoshbaiden:
    K = 1
    while 3**K <= N:
        K += 1
    return K
N = 20  
K = BaidenandZelensyi(N)
print("Наименьшее целое K, при котором выполняется неравенство 3^K > N:", K)
print("Значение 3^K в этом случае:", 3**K)

#Задача 5
def benten:
    K = 0
    while 3**K < N:
        K += 1
    return K - 1
N = 20  
K = mickrozelenckyi(N)
print("Наибольшее целое K, при котором выполняется неравенство 3^K < N:", K)