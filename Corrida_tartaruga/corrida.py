import turtle
import time
import random

Largura = altura = 500
cores = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def numero_da_tartaruga():
    corredor = 0
    while True:
        corredor = str(input('Qual o numero da tartaruga você que apostara (1 a 10): '))
        if corredor.isdigit():
            corredor = int(corredor)
        else:
            print('O corredor digitado não corresponde a um número inteiro! tente novamente')
            continue
        if 2 <= corredor <= 10:
            return corredor
        else:
            print('Ops! o número não esta entre 1 e 10. tente novamente!')


def criar_tartarugas(cor):
    tartarugas = []
    espaçox = Largura // (len(cor) + 1)
    for i, cor in enumerate(cor):
        tartaruga = turtle.Turtle()
        tartaruga.color(cor)
        tartaruga.shape('turtle')
        tartaruga.left(90)
        tartaruga.penup()
        tartaruga.setpos(-Largura//2 + (i+1) * espaçox, -altura//2 + 20)
        tartaruga.pendown()
        tartarugas.append(tartaruga)
    return tartarugas

def inicio_jogo():
    screen = turtle.Screen()
    screen.setup(Largura, altura)
    screen.title('jogo das tartarugas')


tartaruga = numero_da_tartaruga()
inicio_jogo()
random.shuffle(cores)
cor = cores[:tartaruga]
criar_tartarugas(cor)


