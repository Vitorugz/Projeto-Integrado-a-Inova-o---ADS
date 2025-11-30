# Lista para salvar os pacientes
pacientes = []

# Função que permite cadastrar um novo paciente
def cadastrar_paciente():
    """Permite cadastrar um novo paciente (nome, idade, telefone)."""
    print("\n=== CADASTRO DE PACIENTE ===")
    # Recebe o nome do paciente
    nome = input("Nome do paciente: ").strip()

    # Recebe a idade do paciente, garantindo que ela seja um número inteiro positivo
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. A idade deve ser um número inteiro.")
    
    # Recebe o telefone do paciente
    telefone = input("Telefone: ").strip()
    
    novo_paciente = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }
    
    # Adiciona o novo paciente na lista
    pacientes.append(novo_paciente)
    print(f"\nPaciente '{nome}' cadastrado com sucesso!")

# Função que calcula e exibe as estatísticas básicas da clínica
def ver_estatisticas():
    """Calcula e exibe as estatísticas básicas da clínica."""
    
    # Verifica se algum paciente foi cadastrado
    if not pacientes:
        print("\nNenhum paciente cadastrado para calcular estatísticas.")
        return

    # Cria uma lista com as idades dos pacientes, usando o list comprehension
    idades = [p['idade'] for p in pacientes]
    
    # 1. Número total de pacientes
    total_pacientes = len(pacientes)
    
    # 2. Idade média dos pacientes
    idade_media = sum(idades) / total_pacientes
    
    # 3. Paciente mais novo e mais velho
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])

    # Exibe as estatísticas na tela
    print("\n=== ESTATÍSTICAS DA CLÍNICA VIDA+ ===")
    print(f"Número total de pacientes cadastrados: {total_pacientes}")
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")
    print("-" * 30)
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos) ")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos) ")
    print("-" * 30)

# Função que permite buscar um paciente pelo nome
def buscar_paciente():
    """Permite buscar um paciente pelo nome."""
    print("\n=== BUSCAR PACIENTE ===")
    nome_busca = input("Digite o nome do paciente que deseja buscar: ").strip().lower()
    
    # Cria uma lista com os pacientes que contem o nome buscado
    encontrados = [p for p in pacientes if nome_busca in p['nome'].lower()]
    
    # Valida se algum paciente foi encontrado
    if encontrados:
        print(f"\n--- {len(encontrados)} Paciente(s) Encontrado(s) ---")
        for p in encontrados:
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
    else:
        print(f"\nPaciente com o nome '{nome_busca}' não foi encontrado.")

# Função que serve para listar todos os pacientes
def listar_todos_pacientes():
    """Exibe todos os pacientes cadastrados de forma organizada."""
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===")
    
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    # Organização visual da lista para melhor visualização
    print(f"{'#':<3} {'Nome':<25} {'Idade':<8} {'Telefone':<15}")
    print("-" * 51)
    
    # Iteração para exibir os pacientes
    for i, p in enumerate(pacientes):
        print(f"{i+1:<3} {p['nome']:<25} {p['idade']:<8} {p['telefone']:<15}")

# Função que implementa o menu principal
def menu_principal():
    """Implementa o menu principal e o loop do programa."""
    
    # aqui é onde se inicia o programa, com um while 
    # esperando que o usuário escolha uma opção, ou sair para encerrar 
    while True:
        print("\n" + "="*25)
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("="*25)
        
        # Recebe a opção escolhida
        opcao = input("Escolha uma opção: ")

        # Executa a opção escolhida
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_todos_pacientes()
        elif opcao == '5':
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")

# Inicia o programa
if __name__ == "__main__":
    menu_principal()
