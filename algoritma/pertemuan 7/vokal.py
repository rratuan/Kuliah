kalimat = input('Kalimat : ')
banyak = 0
hurufVokal = ''
for huruf in kalimat:
    if huruf.upper() in ['A','E','I','U','E','O']:
        banyak = banyak + 1
        hurufVokal = hurufVokal + huruf
print(f'Banyak huruf vokal {banyak} : {hurufVokal}')