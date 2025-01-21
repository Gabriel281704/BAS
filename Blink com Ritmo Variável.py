# Blink com Ritmo Variável: A velocidade com que o led irá piscar mudará para cada apertar do botão.
# Um segundo led é usado para marcar o inicio e a mudança de ritmo.

###########################################################################################
# Importar apenas as partes necessárias pode reduzir a escrita do código
from machine import Pin
from utime import sleep
###########################################################################################

# Definindo as Funções

def inicio(): # Pisca os dois leds três vezes.
    for a in range(3):
        alert.value(1)
        led.value(1)
        sleep(1)
        led.value(0)
        alert.value(0)
        sleep(1)
        
def notifica(valor): # Apenas o led de alerta pisca indicando o ritmo a ser utilizado.
    for i in range(valor):
        alert.value(1)
        sleep(1)
        alert.value(0)
        sleep(0.5)
        
def blink(valor): # Faz o led principal piscar de acordo com o ritmo determinado.
    led.value(1)
    sleep((valor)/10)
    led.value(0)
    sleep((valor)/10)
        
###########################################################################################

# Inicialização

led = Pin(14, Pin.OUT)
alert = Pin(15, Pin.OUT)
botao = Pin(13, Pin.IN, Pin.PULL_UP)
cont = 1

###########################################################################################

# Parte Principal

inicio()
notifica(cont)

while(True):
        if(botao.value() == 0):
            if(cont < 5):
                cont += 1
            else:
                cont = 1
            notifica(cont)
        blink(cont)




