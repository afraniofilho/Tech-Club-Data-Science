#Importar bibliotecas

import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import time

import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

Volt = []  # cria uma lista vazia para guardar os valores de voltagem

arduinoData = serial.Serial(port='com10', baudrate = 9600) # cria um objeto serial (arduinoData) na porta de comunicação 'com3'
plt.ion()       #Configura o matplotlib no modo interativo para atualizar automatico


def makeFig(): # Criar uma função para o gráfico
    plt.ylim(0, 7)
    plt.title('Voltagem')
    plt.grid(True)
    plt.ylabel('V')
    plt.plot(Volt, 'ro-')

#Função para checar se o valor lido pode ser convertido a float
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


while True:
    arduinoString = arduinoData.readline() #ler uma linha da porta serial
    dataArray = arduinoString[:3]  #ler os 3 primeiros caracteres (valor da temperatura)
    if check_float(dataArray):   # verifica se o valor lido pode ser convertido para float
        voltagem = float(dataArray)     # converte em float e guarda em temperatura
        Volt.append(voltagem)            # cria um array adicionando as leituras de Temp
        drawnow(makeFig)                # chama a função do gráfico
        arduinoData.reset_input_buffer()          
        print(voltagem)            # mostra valor da temperatura no terminal
        if voltagem == 5.0:
            messagebox.showinfo("Notification", "5 Volts atingido")
            root.update()
            time.sleep(2)
            arduinoData.reset_input_buffer()
    time.sleep(1)
