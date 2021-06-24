num = float(input("Digite um valor monetário:\n"))

print("O valor digitado se converte em:\n")
print("NOTAS:\n")
print("%.0f nota(s) de R$ 100.00" %(num // 100))
num %= 100
print("%.0f nota(s) de R$ 50.00" %(num // 50))
num %= 50
print("%.0f nota(s) de R$ 20.00" %(num // 20))
num %= 20
print("%.0f nota(s) de R$ 10.00" %(num // 10))
num %= 10
print("%.0f nota(s) de R$ 5.00" %(num // 5))
num %= 5
print("%.0f nota(s) de R$ 2.00" %(num // 2))
num %= 2
print("MOEDAS:\n")
print("%.0f moeda(s) de R$ 1.00" %(num // 1))
num %= 1
print("%.0f moeda(s) de R$ 0.50" %(num // 0.5))
num %= 0.5
print("%.0f moeda(s) de R$ 0.25" %(num // 0.25))
num %= 0.25
print("%.0f moeda(s) de R$ 0.1" %(num // 0.1))
num %= 0.1
print("%.0f moeda(s) de R$ 0.05" %(num // 0.05))
num %= 0.05
print("%.0f moeda(s) de R$ 0.01" %(num // 0.01))
num %= 0.01
