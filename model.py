#Arquivo modelo

import this
this.soma = 0
this.num = 0

def somarInicioFim(inicio, fim):
    soma = 0
    for i in range(inicio, fim+1, 1):
        soma += i
    return soma

def taboada(num, fim):
    multiplicacao = ""
    for i in range(1, fim+1, 1):
        multiplicacao += "{} * {} = {}\n".format(num, i, num * i)
    return multiplicacao

def inicioFim(inicio, fim):
    mostrar = ""
    for i in range(inicio, fim+1, 1):
        mostrar += "{}\n".format(i)
    return mostrar


def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar


def somar10Numeros(num):
    this.soma += num
    return this.soma


def calcularMedia (soma, quantidade):
    return soma / quantidade

def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def contarValores(valor):
    if valor < 0:
       this.num += 1
    return this.num

def fatorial(num):
    aux = num
    fat = 1
    while(num > 1):
        fat = fat * num
        num -= 1
    return f"O fatorial de {aux} é {fat}"

