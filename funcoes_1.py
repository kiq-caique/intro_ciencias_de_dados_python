# def é uma palavra reservada para definir uma função

def exibir_mensagem():
    print('Hello World') # Hello World

def exibir_mensagem_2(arg): # Lembrar de sempre declarar arg
    print(f"Hello {arg}") # Hello arg

def exibir_mensagem_3(arg="Kiq"):
    print(f"Hello {arg}") # Hello Kiq


exibir_mensagem()
exibir_mensagem_2(arg="arg")
exibir_mensagem_3()