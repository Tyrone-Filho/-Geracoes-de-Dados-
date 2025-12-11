import matplotlib.pyplot as graf
def rodar():
    oie = ["C","C++","Java","Python","C#"]
    popularidade = [65,62,75,86,58]
    graf.title("Votacao da Popularidade das Linguagens de Programacao",fontsize=15)
    graf.bar(oie,popularidade,color='pink',align='center',width=0.6,edgecolor='black',lw=2)
    graf.show()