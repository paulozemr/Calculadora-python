saida = ''

#  parametros
def adicao (a, b):
    return a + b

def subracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        return "Não foi possivel realizar esta divisão."
    return a / b


#  calculadora

def calculadora (num1, num2, operacao):
    if operacao in ('+', 'adicao'):
        return adicao(num1, num2)
    elif operacao in ('-', 'subracao'):
        return subracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        return multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        return divisao(num1, num2)
    else:
        return "Selecione uma das opções validas."
    
# laço

while saida.lower() != 'n':

    try:
        num1 = float(input("Digite o primeiro numero."))
        num2 = float(input("Digite o segundo numero."))

        operacao = input("Digite a operação que deseja realizar")

        resultado = calculadora(num1, num2, operacao)

        print(f"Resultado da operação: {resultado}")

    except ValueError:
        print("entrada invalida, digite corretamente os numeros")

    saida = input("Deseja continuar? (S/N)").strip()