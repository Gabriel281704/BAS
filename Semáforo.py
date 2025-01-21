# Semáforo: Três leds são acesos alternadamente, um por vez.
###########################################################################################

import machine
import utime
###########################################################################################

# Definindo os pinos

green = machine.Pin(13, machine.Pin.OUT)
red = machine.Pin(14, machine.Pin.OUT)
yellow = machine.Pin(15, machine.Pin.OUT)

# Inicializando os pinos e uma variável para determinar o tempo

green.value(0)
red.value(0)
yellow.value(0)
x = 0.6 # Quanto maior o valor, mais lentamente os leds serão alternados
###########################################################################################

while(True):
    green.value(1)
    utime.sleep(x)
    green.value(0)
    red.value(1)
    utime.sleep(x)
    red.value(0)
    yellow.value(1)
    utime.sleep(x)
    yellow.value(0)
    

