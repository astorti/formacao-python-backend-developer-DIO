# Recebe a entrada e armazena na variável "entrada"
entrada = input("Informar os emails separados por ponto e virgula (email;email;email;...): ")

# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')
    
    # TO DO: Implemente a lógica necessária para extrair os domínios
    dominios = []
    for email in lista_emails:
        dominio = email.split("@")
        dominios.append(dominio[1])
    
    return dominios

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))