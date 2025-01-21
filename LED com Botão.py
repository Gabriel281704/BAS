# Led com botão: O led integrado liga quando o botão é pressionado
###########################################################################################

import machine
import utime
###########################################################################################

# Definindo os pinos

led = machine.Pin(15, machine.Pin.OUT) #Pino integrado
alert = machine.Pin(14, machine.Pin.OUT)
botao = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
###########################################################################################

led.value(0)
alert.value(0)

while(True):
    if(botao.value() == 0):
        led.toggle() # Faz a troca do valor... Vai de 0 para 1 e vice-versa
        utime.sleep(3)
        alert.value(1)
        utime.sleep(0.5)
        alert.value(0)
        
