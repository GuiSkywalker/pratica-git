from leitor_arquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.title('Gráfico de linhas')
    os.system("cls")
    plt.plot(valores)
    plt.show()



main()