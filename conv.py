print('conversor de temperatura (Fº - Cº)')
print('escolha a temperatura para a qual deseja converter (digite F para Farenheit ou C para Celsius')
esc = input()
if esc == 'F':
    C = float(input('dê o valor em Cº: '))
    conv = ((C * 9)/5) + 32
    print('valor em Fº:', conv)
elif esc == 'C':
    F = float(input('dê o valor em Fº: '))
    conv = 5 * ((F - 32) / 9)
    print('valor em Cº:', conv)
else : 
    print('por favor, digite F ou C')