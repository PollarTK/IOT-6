import serial
import time
import os
from banco import Banco

PORTA = "COM6"
ARDUINO = serial.Serial(PORTA, 9600, timeout = 1)
time.sleep(2)


ALUNO = "Rian"
LED = 1
banco = Banco()
banco.criar_tabela()

while True:
    estado = banco.ler_estados(ALUNO)
    if estado.upper() == "Ligado":
        ARDUINO.write(b'1')
    else:
        ARDUINO.write(b'0')
    comando = input("digite 1 para ligar o LED 1, 0 para desligar o LED 1 , 2 para listar estados ou 8 Para encerrar o programa: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    match comando:
        case "1":
            estado = "Ligado"
            banco.inserir_ou_atualizar(ALUNO,LED,estado)

        case "0":
            estado = "Desligado"
            banco.inserir_ou_atualizar(ALUNO,LED,estado)

        case "2":
            banco.lista_estados()

        case "3":
            print("programa encerrado!")
            break
        case _:
            print("comando invalido!")