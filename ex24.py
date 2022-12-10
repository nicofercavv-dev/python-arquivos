cidade = str(input('Dê o nome de uma cidade: ')).strip()
cidade.split()
if cidade[0].upper() == 'SANTO':
    print('O nome da cidade não começa com SANTO')
elif cidade[0].upper() != 'SANTO':
    print('O nome da cidade começa com SANTO')