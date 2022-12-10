import math

cato = float(input("Dê o comprimento do cateto oposto: "))
cata = float(input("Dê o comprimnto do cateto adjacente: "))
hip = math.hypot(cato, cata)
print("A hipotenusa é {:.2f}".format(hip))