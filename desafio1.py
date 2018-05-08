# -*- coding: utf-8 -*-
"""
DESAFIO 01
Encontre todos os números divisíveis por 7 mas que não são múltiplos de 5 no 
intervalo de 2000 a 3200, inclusive.
Imprimir esse resultado em uma só linha, separado por vírgula!
"""

d = [str(i) for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(','.join(d))
