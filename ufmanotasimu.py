print("------------SISTEMA DE NOTAS UFMA------------")
n1 = float(input("\nDÊ SUA PRIMEIRA NOTA: "))
menor = n1
n2 = float(input("\nDÊ SUA SEGUNDA NOTA: "))
if n2 < menor:
    menor = n2
n3 = float(input("\nDÊ SUA TERCEIRA NOTA: "))
if n3 < menor:
    menor = n3

res = (n1 + n2 + n3)/3

if res >= 7:
    print("PARABÉNS! VOCÊ PASSOU!!!")
elif res < 7 and res >= 4:
    print("NOTA NÃO APROVATIVA!!!")
    rep = float(input("\nADICIONE SUA NOTA DE REPOSIÇÃO: "))
    if menor == n1:
        rescrep = (rep + n2 + n3)/3
    elif menor == n2:
        rescrep = (n1 + rep + n3)/3
    else:
        rescrep = (n1 + n2 + rep)/3
        
        if rescrep >= 7:
            print("PARABÉNS! VOCÊ PASSOU!!!")
        elif rescrep < 7 and rescrep >= 2:
            print("NOTA NÃO APROVATIVA!!!")
            final = float(input("\n ADICIONE SUA NOTA DE FINAL: "))
            rescfinal = (rescrep + final)/2
            if rescfinal >= 6:
                print("PARABÉNS VOCÊ PASSOU!!!")
            elif rescfinal < 6:
                print("REPROVADO!!!")
            else:
                print("REPROVADO SEM DIREITO A FINAL!!!")
elif res < 4:
    print("REPROVADO SEM DIREITO A REPOSIÇÃO!!!")