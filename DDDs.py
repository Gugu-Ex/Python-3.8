DDD = [61, 71, 11, 21, 32, 27, 31, 19]
Destination = ["Brasília", "Salvador", "São Paulo", "Rio de Janeiro", "Juíz de Fora", "Vitória", "Belo Horizonte", "Campinas"]

num = int(input("Digite um DDD:\n"))
encontrado = 0

for i in range(len(DDD)):
       if num == DDD[i]:
              encontrado = 1
              print("Cidade de: ", Destination[i])

if encontrado == 0:
       print("DDD não cadastrado")
