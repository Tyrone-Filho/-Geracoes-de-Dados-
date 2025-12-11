#sem pie chart :(
import matplotlib.pyplot as graf
import numpy as np
def rodar():
    chapado = np.random.normal(160,10,1000)
    graf.boxplot(chapado)
    graf.show()