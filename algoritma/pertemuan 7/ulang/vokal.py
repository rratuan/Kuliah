kalimat = input('Kalimat : ')
banyak = 0
# vokal = ['A','I','U','E','O']
hurufVokal = ''

for huruf in kalimat:
    # if huruf.upper() == vokal:
    if huruf.upper() in ['A','I','U','E','O']:
        banyak = banyak + 1
        hurufVokal = hurufVokal + huruf
print(f'Huruf Vokal dari kalimat tersebut ada {banyak} yang terdiri dari "{hurufVokal}"')