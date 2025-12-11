import matplotlib.pyplot as graf
def rodar():
    emocoes = ["UAUAU","Tedio","Felicidade","Preguiça","Sono"]
    porcentagens = [50,50,50,50,50]
    kabumm = [0,0,0.05,0,0]

    graf.title("Minhas Emocoes")
    graf.pie(porcentagens, labels=emocoes,explode=kabumm,autopct="%.1f%%",pctdistance=0.7,startangle=90) #frame radius counterclock
    graf.show()