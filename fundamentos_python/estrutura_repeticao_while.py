import time 
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        time.sleep(0.5)
        print("Exibindo o extrato, um instante...")
else:
    print("Obrigado por usar nosso sistema bancário, tenha um ótimo dia!")