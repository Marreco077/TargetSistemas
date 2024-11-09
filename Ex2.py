# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
# soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
# pertence ou não a sequência.

def fibonacci(numero: int) -> int:
    if numero <= 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

def pertence_a_fibonacci(numero: int) -> bool:
    i = 0
    while True:
        fib_num = fibonacci(i)
        if fib_num == numero:
            return True
        elif fib_num > numero:
            return False
        i += 1

numero = 377
print(f"O número {numero} pertence à sequência de Fibonacci? {pertence_a_fibonacci(numero)}")
