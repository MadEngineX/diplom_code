from math import sin, pi
import matplotlib.pyplot as plt

####Объявление функции амплитудной манипуляции####
def ASK(fc, data):
    N = 100 * fc
    tiv = 1 / N
    t = 0
    s = []
    while(t < len(data)):
        s += [int(data[int(t)]) * sin(2 * pi * fc * t)]
        t += tiv
    #print(s)
    return s

####Объявление функции амплитудной деманипуляции####
def ASDK(fc, data):
    N = 100 * fc
    tiv = 1 / N
    t = 0
    s = []
    bits = []
    bits_out = []
    while (t < 10):
        s += [sin(2 * pi * fc * t)]
        t += tiv
    print(len(data))
    for i in range(0, len(data)):
        if (int(s[i]) == 0) and (int(data[i]) == 0):
            bits.append(0)
        elif (int(s[i]) == 0) and (int(data[i]) != 0):
            bits.append(1)
        else:
            bits.append(int(data[i])//int(s[i]))
    # for i in range(N//(fc*2)//2, len(data), N):
    #     bits_out.append(bits[i])
    #for i in range(0, len(data), N):
    #    bits_out.append(bits[i])
    #print('bitslen ' + str(len(bits)))
    return  bits

#print(ASDK(10, ASK(10, '101')))
#plt.plot(ASK(10, '101'))
#plt.plot(ASDK(10, ASK(10, '101')))
#plt.show()