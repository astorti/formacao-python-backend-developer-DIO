# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
temperaturas_celsius = input("Informe as temperaturas em Celsius (temperatura,temperatura,...): ").split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # TO DO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []
    for temperatura in temperaturas_celsius:
      fahrenheit = temperatura * 9/5 + 32
      temperaturas_fahrenheit.append(fahrenheit)
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))