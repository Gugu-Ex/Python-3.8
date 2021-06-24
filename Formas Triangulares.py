ABC = []

ABC.append(float(input("Digite o valor A:\n")))
ABC.append(float(input("Digite o valor B:\n")))
ABC.append(float(input("Digite o valor C:\n")))

ABC.sort()
ABC.reverse()

if ABC[0] >= ABC[1] + ABC[2]:
       print("NAO FORMA TRIANGULO")
else:
       if ABC[0] == ABC[1] + ABC[2]:
              print("TRIANGULO RETANGULO")
       if ABC[0] > ABC[1] + ABC[2]:
              print("TRIANGULO OBTUSANGULO")
       if ABC[0] < ABC[1] + ABC[2]:
              print("TRIANGULO ACUTANGULO")
       if ABC[0] == ABC[1] and ABC[0] == ABC[2]:
              print("TRANGULO EQUILATERO")
       elif ABC[0] == ABC[1] and ABC[0] != ABC[2]:
              print("TRIANGULO ISOSCELES")
       elif ABC[1] == ABC[2] and ABC[1] != ABC[0]:
              print("TRIANGULO ISOSCELES")
       elif ABC[0] == ABC[2] and ABC[0] != ABC[1]:
              print("TRIANGULO ISOSCELES")
