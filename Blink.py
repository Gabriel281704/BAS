# Blink: Faz o led interno da placa pico piscar

###########################################################################################

# É preciso importar uma biblioteca para fazer controle de tempo

import machine
import utime
###########################################################################################

# O pino 25 é usado no led interno da placa...
led = machine.Pin(0, machine.Pin.OUT)
led1 = machine.Pin(25, machine.Pin.OUT)

# Agora basta ligar e desligar o led com o passar do tempo

led1.value(1)
utime.sleep(0.4)
led1.value(0)
utime.sleep(0.4)

while(True): # Garante uma repetição infinita do processo
    led.value(0)
    utime.sleep(0.4)
    led.value(1)
    utime.sleep(0.4)

