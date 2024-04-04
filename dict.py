# dict não aceita repetir chave
pessoa = {"nome": "Carlos Henrique", "idade": 31}
pessoa = dict(nome="Carlos Henrique", idade=31)

print(pessoa["idade"]) # 31
print(pessoa["nome"]) # Carlos Henrique
pessoa["telefone"] = "98252-0093"
print(pessoa) #{'nome': 'Carlos Henrique', 'idade': 31, 'telefone': '98252-0093'}
pessoa["nome"] = "Caique"
print(pessoa) #{'nome': 'Carlos Henrique', 'idade': 31, 'telefone': '98252-0093'}

contatos = {
    "caique-kiq@hotmail.com":{"nome": "Carlos Henrique", "idade": 31},
    "mike@hotmail.com":{"nome": "Mike", "idade": 30},
    "mateus@hotmail.com":{"nome": "Mateus", "idade": 29}
    }

print(contatos["mike@hotmail.com"]["idade"])
idade = contatos["mike@hotmail.com"]["idade"]
print(pessoa["idade"])

contatos.update({"mateus@hotmail.com": {"nome": "Fuhr"}}) #mateus@hotmail.com {'nome': 'Fuhr'}

print(contatos.values()) #dict_values([{'nome': 'Carlos Henrique', 'idade': 31}, {'nome': 'Mike', 'idade': 30}, {'nome': 'Fuhr'}])

for chave in contatos:
    print(chave, contatos[chave])

# Ou de um jeito melhor com o método *items()*, retorna uma lista de tuplas
for chave, valor in contatos.items():
    print(chave, valor)




#Teste de Métodos o Dict
carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor")) #None
print(carro.get("motor", {})) #{}
print(carro.items()) #dict_items([('marca', 'Fiat'), ('modelo', 'palio'), ('placa', 'ABD-9826')]) 
print(carro.keys()) #dict_keys(['marca', 'modelo', 'placa'])
print(carro.pop("marca","Valor nao encontrado")) #Fiat
# print(carro.pop("marca")) #Error
print(carro.pop("marca","Valor nao encontrado")) #Valor nao encontrado

