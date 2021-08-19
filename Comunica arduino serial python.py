#Importar bibliotecas Serial
import serial

# cria um objeto serial (arduinoData) na porta de comunicação
arduinoData = serial.Serial(port='com10', baudrate = 9600)

# Loop para  ler a porta Serial
while (arduinoData.readable()):  ## verifica se a porta está pronta para ser lida
    arduinoString = arduinoData.readline() #ler uma linha da porta serial
    print ('Valor lido: {} ' .format(arduinoString))  ## Mostra valor lido
    print ('Status Porta: {} '.format(arduinoData.isOpen())) ## Mostra o estado da Porta
    print ('Device conectado: {} '.format(arduinoData.name))  ## Mostra o nome do dispositivo
    print ('Velocidade: {}'.format(arduinoData.baudrate))

    