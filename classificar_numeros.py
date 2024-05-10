def classificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            print(f"{positivos} números positivos, {negativos} números negativos")
            break  # Encerra o loop se o usuário digitar 0.
        
        classificacao = classificar_numero(numero)
        print(f"{classificacao}!")
        
        # Incrementa o contador de positivos ou negativos
        if classificacao == "positivo":
            positivos += 1
        elif classificacao == "negativo":
            negativos += 1
    
    # Imprime a quantidade de números positivos e negativos inseridos

if __name__ == "__main__":
    main()
