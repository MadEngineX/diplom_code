from math import sin, pi
import matplotlib.pyplot as plt


####Объявление функции амплитудной манипуляции####
def FSK(fc, data):
    N = 100 * fc
    tiv = 1 / N
    t = 0
    s = []
    while(t < len(data)):
        if (int(data[int(t)]) == int(1)):
            s.append([sin(2 * pi * fc * t)])
            t += 0.5 *  tiv
        else:
            s.append([ sin(2 * pi * fc * t)])
            t += tiv
    return s

#print(ASDK(10, ASK(10, '101')))
#plt.plot(FSK(10, '101'))
#plt.plot(ASDK(10, ASK(10, '101')))
#plt.show()