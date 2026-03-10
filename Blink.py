# Blink: Faz o led da Pico piscar
############################################################################

import machine # Biblioteca necessária para acessar o hardware da placa
import utime # Biblioteca necessária para o controle de tempo
############################################################################

led = machine.Pin(25, machine.Pin.OUT) #O pino 25 é conectado ao led da placa

while(True): # Garante uma loop infinito
    led.value(0)		#Desliga o led
    utime.sleep(0.4)	#Tempo de espera
    led.value(1) 		#Liga o led
    utime.sleep(0.4)
