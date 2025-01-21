# PWM: Simula uma saída analógica usando um pino digital
#################################################################

import machine

# É necessário definir um pino PWM a partir de um pino comum
led = machine.PWM(machine.Pin(15))

# Definir alguns valores para facilitar o uso do duty cicle
meio = 32700
forte = 65535 # É o valor máximo para o duty cicle
fraco = 2000

# Abaixo definimos a frequência e o ciclo de trabalho do pino
led.freq(1000)
led.duty_u16(0)


