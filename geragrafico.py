from leitor_arquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    os.system("cls")
    print(valores)
    os.system("cls")
    plt.plot(valores)
    plt.show()



main()