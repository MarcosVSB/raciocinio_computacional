nota = float(input('Digite uma nota: '))
if nota < 0 or nota > 10:
    print('Nota inválida')
else:
    if nota >= 9:
        print('Nota excelente!')
    elif nota >= 7:
        print('Boa nota!')
    elif nota >= 5:
        print('Nota regular')
    elif nota >= 3:
        print('Nota ruim...')
    else:
        print('Vai se fuder...')
input('Pressione alguma tecla')