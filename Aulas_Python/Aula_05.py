# Aula 05 - Introdução ao Python: Sub-rotinas e Módulos

def soma(op1, op2):
    """
    Função que retorna a soma de dois números
    :param op1: primeiro operando
    :param op2: segundo operando
    :return: soma dos operandos
    """
    return  op1 + op2

def divisao(dividendo, divisor):
    """
    Função que retorna a divisão do dividendo pelo divisor
    :param dividendo: dividendo da operação
    :param divisor: divisor da operação
    :return: divisão do dividendo pelo divisor
    """
    return  dividendo/divisor

print(soma(1.75,2))
print(divisao(50, 2.75))