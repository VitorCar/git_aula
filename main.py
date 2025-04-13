import random
from  mensagens import display_msn

print('New projecct em 3.. 2.. 1')

while True:
    resp = str(input('Quer continuar [S/N]: '))
    if resp == 'S' or resp == 's':
        msn = random.choice(display_msn)
        print(msn)
        print()