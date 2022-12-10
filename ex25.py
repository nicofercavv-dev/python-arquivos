nome = input('Dê o seu nome: ')
if nome.find('SILVA') == -1:
    print('O nome SILVA não existe no nome')
elif nome.find('SILVA') != -1:
    print('O nome SILVA existe no nome')