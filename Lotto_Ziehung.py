import random
import numpy as np
import matplotlib.pyplot as plt




def Lotto_Ziehen(array):
    lenght=len(array)-1
    for x in range(6):
        index = random.randrange(lenght)
        print(index)
        array[index], array[lenght] = array[lenght], array[index]
        lenght=lenght-1
    LottoZahlen = array[39:45]
    return LottoZahlen

Zahlen = np.arange(1, 46)

dic={}
for i in range(45):
    dic[i+1]=0

print(dic[1]+ "dslfkjsldkfjdslkfjdslkfjdslk")

for x in range(1000):
    zahlen = Lotto_Ziehen(Zahlen)
    for b in zahlen:
        dic[b]=dic[b]+1

names = list(dic.keys())
values = list(dic.values())

plt.bar(range(len(dic)), values, tick_label=names)
plt.show()


