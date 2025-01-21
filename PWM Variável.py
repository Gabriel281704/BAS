'''
PWM Variável: Vamos mudar a luminosidade de um led variando
o ciclo de trabalho de acordo com a sinalização de um botão.
'''
import machine
import utime

# Define o ciclo de trabalho do pino, e consequentemente a luminosidade do led
def brilho(numero):
    led.duty_u16(numero*10000)

# Define o contador que será usado para definir o brilho  do led
def muda_Brilho(valor):
    if(valor < 6):
        valor += 1
    else:
        valor = 1

# Definindo os pinos para o botão(saída) e o led(PWM)
botao = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.PWM(machine.Pin(15), freq = 1000)
cont = 1


# Parte Principal
'''
Parte de inicialização: O led irá alternar a sua luminosidade, entre forte
e fraco, três vezes no início.
'''

for n in range(3):
    brilho(6)
    utime.sleep(0.5)
    brilho(0)
    utime.sleep(0.5)

'''
É a parte mais relevante. É aqui que o led terá sua luminosidade alterada de acordo
com o apertar do botão.
'''

while(True):
    if(botao.value() == 0):
        muda_Brilho(cont)
        brilho(cont)
        utime.sleep(0.3)




