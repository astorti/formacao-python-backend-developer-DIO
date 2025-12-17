# Recebe o valor limite como entrada do usuário e converte para float
limite = 150.0
# Recebe a string de transações como entrada do usuário
transacoes = "1:100.00;2:200.50;3:150.75"

# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')
    
    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)
        
        # TO DO: Compare o valor da transação com o limite e adiciona à lista filtrada se for maior
        if (valor >= limite):
            transacao = f"{id_transacao}:{valor}"
            transacoes_filtradas.append(transacao)

    return transacoes_filtradas
    
# Imprime as transações com valores acima do limite
print(filtrar_transacoes_acima_do_limite(limite, transacoes))