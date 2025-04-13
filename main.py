import random

display_msn =['Vai dar certo',
              'Se estiver com medo va com medo mesmo',
              'Apenas continue'
]

while True:
    resp = str(input('Quer continuar [S/N]: '))
    if resp == 'S' or resp == 's':
        msn = random.choice(display_msn)
        print(msn)
        print()