import time

# Implementação do modo contínuo do conversor
entrada = 1
num = 0

print ("Bem-vindo ao conversor de número decimais inteiros positivos para bases binárias, octais e hexadecimais!",
       "\n(Para encerrar o conversor, basta digitar um número negativo)")
num = int(input("Digite um número a ser convertido:\n"))

while entrada == 1:
       if num < 0:
              entrada = 0
              print("Agradecemos por usar nosso conversor!\nO conversor se encerrará dentro de 5 segundos!\nFIM")
              time.sleep(5)
       else:
              


# Conversão para binário
              casas_bin = []
              nbin = num

              while nbin > 0:
                     casas_bin.append(nbin % 2)
                     nbin //= 2
              if nbin == 0:
                     casas_bin.reverse()
                     nbin = casas_bin



# Conversão para octal
              casas_oct = []
              noct = num

              while noct > 0:
                     casas_oct.append(noct % 8)
                     noct //= 8
              if noct == 0:
                     casas_oct.reverse()
                     noct = casas_oct



# Conversão para hexadecimal
              casas_hex = []
              nhex = num

              while nhex > 0:
                     casas_hex.append(nhex % 16)
                     nhex //= 16
              if nhex == 0:
                     casas_hex.reverse()
                     nhex = casas_hex

              for i in range(len(casas_hex)):
                     if casas_hex[i] == 10:
                            casas_hex[i] = "A"
                     elif casas_hex[i] == 11:
                            casas_hex[i] = "B"
                     elif casas_hex[i] == 12:
                            casas_hex[i] = "C"
                     elif casas_hex[i] == 13:
                            casas_hex[i] = "D"
                     elif casas_hex[i] == 14:
                            casas_hex[i] = "E"
                     elif casas_hex[i] == 15:
                            casas_hex[i] = "F"



# Alteração da formatação de lista para formatação numérica
              resultado_bin = ""
              resultado_oct = ""
              resultado_hex = ""

              for i in range(len(casas_bin)):
                     resultado_bin += str(casas_bin[i])

              for i in range(len(casas_oct)):
                     resultado_oct += str(casas_oct[i])

              for i in range(len(casas_hex)):
                     resultado_hex += str(casas_hex[i])



# Print do resultado das conversões
              print("Decimal: ", num)
              print("Binário: ", resultado_bin)
              print("Octal: ", resultado_oct)
              print("Hexadecimal: ", resultado_hex)

              num = int(input("\nDigite um outro número a ser convertido:\n"))
