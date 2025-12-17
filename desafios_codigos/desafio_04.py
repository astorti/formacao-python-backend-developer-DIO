# Recebe a entrada e armazena na variável "entrada"
entrada = "Laptop:1200:10;Mouse:20:0;Keyboard:50:5" 

# Função responsável por filtrar produtos em estoque
def filtrar_produtos_em_estoque(entrada):
    if not entrada:
        return []
        
    produtos = entrada.split(';')
    produtos_disponiveis = []
    
    for produto_str in produtos:
        # TO DO: Divida a substring do produto em nome, preço e quantidade usando ':' e converta a quantidade para inteiro
        nome, preco, quantidade = produto_str.split(":")
        quantidade = int(quantidade)
        
        # TO DO: Verifique se a quantidade é maior que zero, caso seja adicione o produto à lista de produtos disponíveis
        if (quantidade > 0):
            produtos_disponiveis.append(produto_str)

    return produtos_disponiveis

# Imprime a lista de produtos em estoque
print(filtrar_produtos_em_estoque(entrada))