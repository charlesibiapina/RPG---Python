print("Bem vindo ao jogo")

inventario = []

while True:

 print("\n1. Ir para a cabana")
 print("2.Ir para a floresta")
 print("3. Sair do jogo")
 print("4. Ver inventário")

 escolha = int(input("qual sua escolha?"))

 if escolha == 1:

    print("\nA casa tem uma espada")
    print("1. Pegar a espada")
    print("2. Ignorar a espada")
    print("3. Voltar para a floresta")

    espada = int(input("o que você faz?"))

    if espada == 1 :
        inventario.append("espada")
        print("o jogador conseguiu uma espada!")

    elif espada == 2 :
        print("seu inventário está vazio!")

    elif espada == 3 :
        print ("você voltou para a floresta")

    else :
        print("número inválido")

 elif escolha == 2 :
    print("você esta na floresta escura")

 elif escolha == 3 :
    print("você saiu do jogo")
    break
 elif escolha == 4 :
    print ("Seu inventário")
    for item in inventario:
        print(f"{item}")

 else:
    print("Número Inválido")
