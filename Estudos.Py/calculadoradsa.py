def soma(numeros):
    return sum(numeros)

def subtracao(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado
def multiplicacao(numeros):
    resultado = numeros[0]
    for num1 in numeros[1:]:
       resultado *= num1 
    return resultado
def divisao(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado /= num
    return resultado
    
def obter_numeros():
    entrada = input("Digite os números separados por espaço: ")
    try:
        return list(map(float, entrada.split()))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return obter_numeros()
    
def menu():
    print("#################### Calculadora ###################")
    print("1-Somar")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("5-Sair")
    opcao = input("Escolha uma opção: ")
    return opcao
    
    
def main():
    while True:
        opcao = menu()
        if opcao == "5":
            print("Saindo...")
            break
        
        numeros = obter_numeros()
        
        if opcao == "1":
            resultado = soma(numeros)
        elif opcao == "2":
            resultado = subtracao(numeros)
        elif opcao == "3":
            resultado = multiplicacao(numeros)
        elif opcao == "4":
            resultado = divisao(numeros)    
        else:
            print("Opção inválida.")
            continue
        print(f"Resultado: {resultado}")
if __name__ == "__main__":
    main()