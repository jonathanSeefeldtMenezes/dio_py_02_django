from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('Hello World, Django!!')


def somar(request, numero1, numero2):
    calc = Calculadora(numero1, numero2)
    resposta = calc.somar()
    return HttpResponse(f'<p>Resultado da soma: {resposta}</p>')


def subtrair(request, numero1, numero2):
    calc = Calculadora(numero1, numero2)
    resposta = calc.subtrair()
    return HttpResponse(f'<p>Resultado da subtração: {resposta}</p>')


def dividir(request, numero1, numero2):
    calc = Calculadora(numero1, numero2)
    resposta = calc.dividir()
    return HttpResponse(f'<p>Resultado da divisão: {resposta}</p>')


def multiplicar(request, numero1, numero2):
    calc = Calculadora(numero1, numero2)
    resposta = calc.multiplicar()
    return HttpResponse(f'<p>Resultado da multiplicação: {resposta}</p>')


class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2

    def dividir(self):
        return self.numero1 / self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2
