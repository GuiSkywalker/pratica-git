import os

def menu():
    print("1 - soma\n2 - subtração")
    return

def main():
    os.system("cls")
    menu()
    x = int(input())
    if x == 1:
        soma()
    else:
        subtracao()

def subtracao():
    os.system("cls")
    a = float(input("Insira o primeiro número: "))
    os.system("cls")
    b = float(input("Insira o segundo número: "))
    os.system("cls")
    y = a - b

    print("O resultado é: ", y)
    z = input("Retornar ao menu? (y/n)")
    if z == "y" or z == "ye" or z == "yes":
        main()
    else:
        print("Adeus!")
def soma():
    os.system("cls")
    a = float(input("Insira o primeiro número: "))
    os.system("cls")
    b = float(input("Insira o segundo número: "))
    os.system("cls")
    y = a + b

    print("O resultado é: ",y)
    z = input("Retornar ao menu? (y/n)")
    if z == "y" or z ==  "ye" or z == "yes":
        main()
    else:
        print("Adeus!")



if __name__ == "__main__":
    main()