# Conjuntos nao são indexaveis
carros = set(('palio', 'gol', 'hb20', 'gol', 'palio', 'corsa'))
frutas = set(('uva', 'melancia', 'maça', 'laranja', 'uva'))
numeros = set([1,2,3,4,5,6,7,1,2,3,4,5,6,7,8])
letras = set('abacaxi')

linguagens = {'python', 'java', 'python'}


# conjunto_a.union(conjunto_b) = {1, 2, 3, 4, 5}
# conjunto_a.intersection(conjunto_b) = {2, 3, 4}
# conjunto_a.difference(conjunto_b) = {1}
# conjunto_a.symmetric_difference(conjunto_b) = {1, 5}
# conjunto_a.issuperset(conjunto_b) = False
# conjunto_a.issuperset(conjunto_c) = False
# conjunto_'C'.issuperset(conjunto_'A') = True
# conjunto_'A'.isdisjoint(conjunto_'C') = False
# conjunto_'C'.isdisjoint(conjunto_'D') = True
# conjunto_a.add(5) = {1,2,3,4,5}
# conjunto_a.add(45) = {1,2,3,4,45}
# conjunto_a.discard(3) = {1,2,4}
# conjunto_a.pop() = {2,3,4}
# conjunto_a.pop() = {3,4}
# conjunto_a.pop() = {4}
# conjunto_a.pop() = {}


conjunto_a = {1,2,3,4}
conjunto_b = {5,2,3,4}

conjunto_c = {1,2,3,4,5,6,7}
conjunto_d = {8,9}

conjunto_a.add(5)
conjunto_a.discard(3)

print(conjunto_a)
print(conjunto_a.isdisjoint(conjunto_c))