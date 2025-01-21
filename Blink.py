# Blink: Faz o led interno da placa pico piscar

###########################################################################################

# É preciso importar uma biblioteca para fazer controle de tempo

import machine
import utime
###########################################################################################

# O pino 25 é usado no led interno da placa...
led = machine.Pin(25, machine.Pin.OUT)

# Agora basta ligar e desligar o led com o passar do tempo

while(True): # Garante uma repetição infinita do processo
    led.value(0)
    utime.sleep(0.4)
    led.value(1)
    utime.sleep(0.4)

