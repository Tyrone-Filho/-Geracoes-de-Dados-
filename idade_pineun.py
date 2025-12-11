import matplotlib.pyplot as graf
import numpy as np
def rodar():
    idades = np.random.normal(18,1.5,1000)
    graf.hist(idades,bins=20,color='pink',edgecolor='black',lw=3,cumulative=True)
    graf.title('Idade medianas')
    graf.show()