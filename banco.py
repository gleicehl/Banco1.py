import numpy as np

menu = """
[0] Sair:
[1] Depositar: 
[2] Sacar:
[3] Extrato: 

"""

depositar = 0
sacar = 0
contSaques = 0
i=0
saqueTotal= np.array([i]) 
restoSaque = 0
extrato = ""
depositoTotal = 0
limiteDepositoPDia = 0


while True:

    print("\n Escolha uma das opções a seguir: ")
    opcao = int(input(menu))

    if opcao == 1:

        depositar = float(input("Digite um valor para depositar: "))

        if depositar > 0:

            depositoTotal = depositoTotal + depositar
            extrato = extrato + "Depósito total R$" + str(depositoTotal)

        else:

            print("Valor inválido, digite um valor acima de 0 para depositar!")

    if opcao == 2:

        sacar = float(input("Digite o valor do saque: "))

        if sacar <= 0:

            print("\nSaque inválido. O valor deve ser maior que 0!")

        elif contSaques >= 3:

            print("\nVocê atingiu o máximo de saques diários(3 p/dia)!")

        elif saqueTotal > 1500:

            print("\nSaque inválido. Você atingiu o máximo de valor nos saques(R$1500,00)!")

        elif sacar > depositoTotal:

            print("\nSaldo insuficiente para sacar!")

        elif sacar > 500:

            print("\nSaque inválido. Só é possível sacar até R$500,00!")

        else:

            saqueTotal += sacar
            contSaques += 1

            restoSaque = depositoTotal - saqueTotal
        
        print(saqueTotal)

        # if opcao == 3: 

            # i=0
            # for i in range(0,): 



        print("\nSaldo restante na conta R$" + str(restoSaque))