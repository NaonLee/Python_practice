import random

f = open("Assignment#1_2012244011 이나온.txt", 'w')
list = ["Apple", "Orange", "Mango", "Grape", "Banana", "Berry", "Tomato", "Melon"]
f.write("  Item   수량 단가\n")
for i in range(1,1001):
    data = "%7s, %2d, %4d\n"%(random.choice(list),random.randrange(0,10),random.randrange(100,1000)//10*10)
    f.write(data)
f.close()
