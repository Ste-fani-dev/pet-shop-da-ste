def main():
    clientes = []
    pets = []

    # Menu principal 
    while True: 
        print("=========================")
        print("    PET SHOP DA STE      ")
        print("=========================")
        print()  #pula uma linha 
        print("1- Cadastrar Clientes")
        print("2- Listar Clientes")
        print("3- Cadastrar Pet")
        print("4- Listar Pets")
        print("0- Sair")

        opcao = input("Escolha uma opção:")  # Pede uma ação pro usuário

        if opcao == "1":
            print("Cadastrar Clientes")
            nome = input("Digite o nome do cliente: ")
            celular = input("Digite o celular: ")

            cliente = {
                "nome": nome,
                "celular": celular
            }

            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao == "2":
            print("Listar Clientes")
                        
            for cliente in clientes:
                print(cliente["nome"], cliente["celular"])

        elif opcao == "3":
            print("Cadastrar Pet")
            nome = input("Nome do pet: ")
            idade = int(input("Idade do pet: "))
            especie = input("Gato ou Cachorro: ")
            tutor = input("Tutor do pet: ")

            pet = {
                "nome": nome,
                "idade": idade,
                "especie": especie,
                "tutor": tutor
            }

            pets.append(pet)
            print("Pet cadastrado com sucesso!")

        elif opcao == "4":
            print("Listar Pets")

        elif opcao == "0":   
            print("Saindo do Sistema...")
            break

        else:
            print("Opção Inválida!")





main()