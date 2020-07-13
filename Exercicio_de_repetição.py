
"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido """
__author__    = "Edilmar Junior"


condicao = True   ### Sempre utilizar um validador para uma condições

while condicao:
    nota = int(input('Digite uma nota entre 0  e 10 : '))
    if nota >= 0 and nota <= 10:
        print(f'Valor válido!')
        break
    else:
        print(' Valor inválido ')
        continue ### utilizar essa condição para voltar









