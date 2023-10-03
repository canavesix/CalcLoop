def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
    elif operacao == 0:
        return None
    else:
        return "Essa opção não existe"


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
op = int(input("Digite o número da operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão ou 0 para sair): "))

while op != 0:
    resultado = calculadora(numero1, numero2, op)
    
    if resultado is None:
        break
    else:
        print(f"Resultado: {resultado}")
    
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    op = int(input("Digite o número da operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão ou 0 para sair): "))

print("O programa foi encerrado.")
