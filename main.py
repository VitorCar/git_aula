import random
from  mensagens import display_msn


print('Iniciando o projeto de estudo')


while True:
    resp = str(input('Quer continuar [S/N]: '))
    if resp == 'S' or resp == 's':
        msn = random.choice(display_msn)
        print(msn)
        print()