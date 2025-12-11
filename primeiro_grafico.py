import matplotlib.pyplot as graf
def rodar():
    numero = list(range(1,100))
    quadrados = [(num*5)**2 for num in numero]
    graf.plot(numero,quadrados,linewidth=5)
    graf.title("Meu amor pela manu castro",fontsize=20)
    graf.xlabel("Tempo de namoro",fontsize=15)
    graf.ylabel("Meu amor",fontsize=25)
    graf.tick_params(axis="both",labelsize=20)
    graf.show()