cor1 = input()
cor2 = input()
x1, y1 = cor1.split(" ")
x1 = float(x1)
y1 = float(y1)
x2, y2 = cor2.split(" ")
x2 = float(x2)
y2 = float(y2)
distancia = (((x2-x1)**2)+((y2-y1)**2))**(1/2)
print("{:.4f}".format(distancia))