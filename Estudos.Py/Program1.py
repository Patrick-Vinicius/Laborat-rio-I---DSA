texto = """"
    Escolha uma das opções abaixo:
    (1) La creme da Cacau Show 
    (2) Alpino
    (3) Copenhage
    (4) Baccio del late
"""

opcao = input(texto)

value_item = 0

if opcao == "1":
    value_item = 22.5
elif opcao == "2":
    value_item = 8.90
elif opcao =="3":
    value_item = 32.50
elif opcao == "4":
    value_item = 57.89
    
else:
    print("Opção Invalida")
    
    
qt= input("Quantos chocolates?")
qt= int(qt)
 
valor_total = value_item * qt

print("Sua Conta deu :", valor_total)