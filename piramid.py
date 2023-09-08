tinggi_piramida = int(input('input tinggi piramida: '))
print ()
for i in range (tinggi_piramida):
    for j in range(tinggi_piramida-i):
        print(' ',end='')
    for k in range (i+1):
        print('* ',end='')
    print()