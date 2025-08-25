class Calculadora:
    def soma( n1, n2):
        return n1 + n2

    def subtracao( n1, n2):
        return n1 - n2

    def multiplicacao( n1, n2):
        return n1 * n2

    def divisao( n1, n2):
        if n2 == 0:
            raise ZeroDivisionError("Err0! Tentativa de divisão por 0")
        return n1 / n2
