print(27 * '-')
print('> Bem vindo a ContactCenter')
print(27 * '.')

id_global = 5579392 # Atribuindo meu id_global
lista_contatos = [] # Lista de contatos vazia


def edicao_contato(): # Função para editar contato
    while True:  # Loop para vlaidar o id, para assim entrar posteriomente no menu
        try: 
            id_busca = int(input('> Digite um ID válido: ')) # try/except para validar o id_busca 
            break
        except ValueError:
            print('> Digite apenas números no ID')

    encontrado = False # flag = false que está ligada com o ultimo if embaixo 

    for i in lista_contatos: # for para iterar sobre minha lista de contatos
        if id_busca == i['id']: 
            encontrado = True  
            print(60 * '-')
            print(f"> Contato encontrado com sucesso, {i['nome']}")


            while True: # loop novamente para entrar no menu edição, onde o usuário escolhe qual dado deseja mudar
                print(30 * '-')
                print('> Os dados disponiveis para mudança são: ')
                print('1 - Nome')
                print('2 - Atividade')
                print('3 - Telefone')
                print('4 - Finalizar edição')

                try:
                    mudar = int(input('> Qual dado deseja mudar: ')) # try/except para validar o mudar (só aceita números)
                except ValueError:
                    print('> Digite apenas números válidos')
                    continue

                # if, elif para os ajustes 
                if mudar == 1:
                    novo_nome = input('> Digite o novo nome: ')
                    i['nome'] = novo_nome # novo nome é atribuido para variavel nome na minha lista
                    print('> Operação concluída com sucesso, nome atualizado!')

                elif mudar == 2:
                    nova_atividade = input('> Digite a nova atividade: ')
                    i['atividade'] = nova_atividade  # nova atividae é atribuida para variavel atividade na minha lista
                    print('> Operação concluída com sucesso, atividade atualizada!')

                elif mudar == 3:
                    while True:
                        try:
                           novo_telefone = int(input('Digite o novo telefone: '))
                           i['telefone'] = novo_telefone  # novo telefone é atribuido para variavel telefone na minha lista  
                           print('> Operação concluída com sucesso, telefone atualizado!')

                           break
                        except ValueError:
                            print('> Digite apenas números')

                elif mudar == 4: # se o usuário digitar 4, retornamos para o menu principal.
                    print('> Encerrando o menu edição e voltando para menu principal...')
                    return
        
                else:
                    print('> Opção inválida')
    if not encontrado:
        print('> Contato não encontrado')            

# Criando função para cadastro de contato
def cadastrar_contato(id): # Recebe apenas o paramêtro (id)
    nome = input('> Digite o nome: ') 
    atividade = input('> Digite a atividade: ')

    while True:
        try:
            telefone = int(input('> Digite o telefone: '))
            break
        except ValueError:
            print('> Digite apenas números no telefone')
    # Dicionario de novo contato, com chave e valor que o usuario dar de entrada
    novo_contato = {'id': id,
                    'nome': nome,
                    'atividade': atividade,
                    'telefone': telefone} 

    lista_contatos.append(novo_contato.copy()) # Copiando os valores da meu dict, para a lista
 


# Criando função para remover contato
def remover_contato():
    # Loop infinito
    while True:
        try:
            id = int(input('> Digite um ID válido: '))
            break
        except ValueError:
            print('> Digite apenas números no ID')

    removido = False # minha flag, para ser útil na minha estrutura (if/else)
    for i in lista_contatos: # laço for, para iterar sobre cada item da minha lista
        if id == i['id']: # Iterando no valor (id) com meu i(iteração)
            lista_contatos.remove(i)
            removido = True # Se for removido com sucesso a minha flag assume True.
            break # Encerra o laço 
    if removido == False: # Minha flag assumindo o valor False, a mensagem de não exclusão entra
        print('> Contato não foi removido!')
    else:
        print('> Contato removido com sucesso! ')
         

# Criando função para consultar contato
def consultar_contatos():
    # Loop infinto com menu de consulta
    while True:
        print('> MENU DE CONSULTA CONTATOS')
        print(30 * '-')
        print('Temos as seguintes opções: ')
        print(30 * '-')

        print('1 - Consultar todos')
        print('2 - Consultar por ID ')
        print('3 - Consultar por atividade')    
        print('4 - Retornar o menu')

        opcao = input('> Digite sua opção: ')

        print(25 * '-')


        if opcao == '1': # Se opção for igual a 1 que seria (1- Consultar a todos)
            if lista_contatos == []: # Imprime a mensagem caso a lista esteja vazia
                print('> A lista está vazia')   
                print(25 * '.')

            else:
                for i in lista_contatos: # Caso não esteja vazia, uso o laço for para iterar sobre cada item do dict
                    print(f"- Id: {i['id']}") 
                    print(f"- Nome: {i['nome']}")
                    print(f"- Atividade: {i['atividade']}")
                    print(f"- Telefone {i['telefone']}")

                    print(29 * '-')

        elif opcao == '2':  # Se opção for igual a 2 que seria (2 - Consultar por ID)
            while True:
                try:
                    id = int(input('> Digite um ID válido: '))
                    break
                except ValueError:
                    print('> Digite apenas números no ID')

            encontrado = False # Uso a estrutura flag, essencial para controle do (if/else)
            for i in lista_contatos: # Uso o laço para iterar sobre a minha lista de contato
                if id == i['id']: # Preciso iterar sobre o meu valor (id) 
                    # Mostro os itens da minha lista 
                    print(f"- Id: {i['id']}") 
                    print(f"- Nome: {i['nome']}")
                    print(f"- Atividade: {i['atividade']}")
                    print(f"- Telefone {i['telefone']}")
                    encontrado = True # Se for encontrado com sucesso, o break encerra o progama
                    break
            if encontrado == False: # Caso haja algum erro, e sinalizado pelo programa.
                print('> Contato não foi encontrado!')
            

        elif opcao == '3': # Se opção for igual a 3 que seria (3 - Consultar por atividade)
            atividade = input('Digite uma atividade: ')
            encontrado = False  # Uso a estrutura flag novamente para sinalizar
            for i in lista_contatos: # Uso o laço para iterar sobre a minha lista de contato
                if atividade == i['atividade']: # Preciso iterar sobre o meu valor (atividade) 
                    # Mostro os itens da minha lista 
                    print(f"- Id: {i['id']}") 
                    print(f"- Nome: {i['nome']}")
                    print(f"- Atividade: {i['atividade']}")
                    print(f"- Telefone {i['telefone']}")
                    encontrado = True # Se for encontrado com sucesso, o break encerra o progama
            if encontrado == False:  # Caso haja algum erro, e sinalizado pelo programa.
                print('Atividade não foi encontrado!')
        
        elif opcao == '4': # Se opção for igual a 4 que seria (4 - Retornar ao menu)
            print('Retornando ao menu principal...')
            return 
        else:
            print('Opção inválida...') 
            continue # Caso nenhuma opção digitada seja válida, erro e volta pro loop

# Menu principal com loop While True:
while True:
    print('--- > MENU PRINCIPAL < ---')
    print(29 * '-')
    print('> Temos as seguintes opções: ')
    print(29 * '-')

    print('1 - Cadastrar novo contato')
    print('2 - Consultar contato(s) ')
    print('3 - Editar contato')    
    print('4 - Remover contato')
    print('5 - Sair')


    print(29 * '-')
    escolha = input('> Escolha a opção desejada: ') 
    if escolha == '1': # Se opção for igual a 1 - Chamo minha variavél cadastrar_contato
        cadastrar_contato(id_global) # Função que recebe como paramêtro o meu id_global
        id_global += 1  # com o cadastro de um novo contato, 
        # a minha id_global soma mais 1, gerando outro ID.

    elif escolha == '2': 
        consultar_contatos()
      
    elif escolha == '3':
        edicao_contato()
       
    elif escolha == '4':
        remover_contato()

    elif escolha == '5': 
        print('> Encerrando programa..Volte Sempre!')
        break

    else:
        print('> Opção inválida, tente novamente...') 
        continue 

    

