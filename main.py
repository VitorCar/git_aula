import random
from  mensagens import display_msn
import time

print('Iniciando o projeto')
time.sleep(3)

while True:
    resp = str(input('Quer continuar [S/N]: '))
    if resp == 'S' or resp == 's':
        msn = random.choice(display_msn)
        print(msn)
        print()