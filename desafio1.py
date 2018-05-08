# -*- coding: utf-8 -*-

"""
DESAFIO 01

Encontre todos os números divisíveis por 7 mas que não são múltiplos de 5 no 
intervalo de 2000 a 3200, inclusive.
Imprimir esse resultado em uma só linha, separado por vírgula!

"""

divisible_by_seven = [str(i) for i in range(2000, 3001) if i % 7 == 0]
print(','.join(divisible_by_seven))
