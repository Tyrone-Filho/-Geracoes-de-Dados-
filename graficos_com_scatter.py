import matplotlib.pyplot as graf
import numpy as np
def rodar():
    x_valor = np.random.random(1000) * 100
    y_valor = np.random.random(1000) * 100
    graf.scatter(x_valor,y_valor,c="#ff007f",edgecolors="none",s=90,marker="*",alpha=0.5)
    graf.tick_params(axis='both',which="major", labelsize=15)
    graf.show()