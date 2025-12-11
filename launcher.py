rodando = True
print("escolha 1 script")
while rodando:
    print("1 - scatter")
    print("2 - grafico uau")
    print("3 - medianas")
    print("4 - pizza")
    print("5 - primeiro grafico")
    print("6 - sem pizza")

    dec = input(">")
    if dec == "1":
        rodando = False
        from graficos_com_scatter import rodar
    elif dec == "2":
        rodando = False
        from graficos_uau import rodar
    elif dec == "3":
        rodando = False
        from idade_pineun import rodar
    elif dec == "4":
        rodando = False
        from pizza import rodar
    elif dec == "5":
        rodando = False
        from primeiro_grafico import rodar
    elif dec == "6":
        rodando = False
        from sem_pizza import rodar
    else:
        print("insira uma opcao Valida")
    try:
        rodar()
    except:
        ...