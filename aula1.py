nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome tem {len(nome)} letras') 
    print(f'A primeira letra de seu nome é {nome[0]}')
    print(f'A última letra de seu nome é {nome[len(nome)-1]}')


    if ' ' in nome:
        print(f'Seu nome é composto')
    else: print('Seu nome não é composto')
    
else: print('Desculpe, você deixou campos vazios.')