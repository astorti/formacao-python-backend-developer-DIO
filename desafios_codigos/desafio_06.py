# Recebe a cidade de interesse da entrada do usuário e remove espaços em branco nas extremidades
cidade_interesse = input("Informe a cidade: ").strip()
# Recebe a lista de clientes da entrada do usuário e remove espaços em branco nas extremidades
clientes = input("Lista de clientes (nome:cidade;nome:cidade;...): ").strip()

# Função que filtra os clientes que moram na cidade especificada
def filtrar_clientes(lista_clientes, cidade_interesse):
    # Se a lista de clientes estiver vazia, retorna uma lista vazia
    if not lista_clientes:
        return []

    # Inicializa uma lista vazia para armazenar os clientes filtrados
    clientes_filtrados = []

    # TO DO: Percorra cada tupla (nome, cidade) na lista de clientes
    for cliente in lista_clientes:
        for nome, cidade in enumerate(cliente):
        # TO DO: Se a cidade do cliente for igual à cidade de interesse, adicione a tupla (nome, cidade) na lista de clientes filtrados
            if cidade == cidade_interesse:
                clientes_filtrados.append(cliente)     
               
    return clientes_filtrados

# Processa a entrada de clientes para converter a string de clientes em uma lista de tuplas (nome, cidade)
lista_clientes = [tuple(cliente.split(':')) for cliente in clientes.split(';')]

# Imprime a lista de clientes filtrados
print(filtrar_clientes(lista_clientes, cidade_interesse))