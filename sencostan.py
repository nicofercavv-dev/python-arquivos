import math

ang = float(input("Dê um ângulo: "))
rad = math.radians(ang)
print("O seno de {:.2f} é {:.2f}".format(ang, math.sin(rad)))
print("O cosseno de {:.2f} é {:.2f}".format(ang, math.cos(rad)))
print("A tangente de {:.2f} é {:.2f}".format(ang, math.tan(rad)))