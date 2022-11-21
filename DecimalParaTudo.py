while True: 
    n = int(input('Digite um número: '))
    print('- - - - '* 5)
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[x] Sair')


    perguntanum = str(input('Digite a opção que deseja converter: '))
    if perguntanum == 'x'or perguntanum == 'X':
        break
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3':
        if perguntanum == '1':
            rio = str(bin(n))
            print(rio)
        elif perguntanum == '2':
            cta = str(oct(n))
            print(cta)

        elif perguntanum == '3':
            exa = str(hex(n))
            print(exa)

    else:
        print('Opção invalida!')