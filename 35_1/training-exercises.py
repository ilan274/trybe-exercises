# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo
# a = 10 e b = 5. Mostre o resultado das 7 operações básicas
# (soma, subtração, multiplicação, divisão, divisão inteira,
# potenciação e módulo) envolvendo essas variáveis.
a = 10
b = 5
print(a + b, a - b, a * b, a / b, a // b, a ** b, a % b)

# Exercício 2: Declare e inicialize uma variável: hours = 6 .
# Quantos minutos têm em 6 horas? E quantos segundos?
# Declare e inicialize variáveis minutes e seconds que recebem os
# respectivos resultados das contas. Depois, imprima cada uma delas.

hours = 24
minutes = hours * 60
seconds = minutes * 60
print(hours, minutes, seconds)

# Exercício 3: Suponha que o preço de capa de um livro seja 24,20,
# mas as livrarias recebem um desconto de 40%.
# O transporte custa 3,00 para o primeiro exemplar e
# 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que
# receba o custo total e a imprima.
qtd_livros = 60
desc_percentage = 0.40
preco_livro = 24.2 * (1 - desc_percentage)
transporte = 0.75 * (qtd_livros - 1) + 3
total = transporte + qtd_livros * preco_livro
print(total)

# Exercício 4: Adicione o elemento "Ciência da Computação" à lista
# e a imprima para verificar a adição.
trybe_course = ["Introdução", "Front-end", "Back-end"]
trybe_course.append("Ciência da Computação")
print(trybe_course)

# Exercício 5: Acesse e altere o primeiro elemento da lista para "Fundamentos".
trybe_course.remove("Introdução")
trybe_course.insert(0, "Fundamentos")
print(trybe_course)

users = ("Ilan", "Herbach")
print(f"O tipo é {type(users)} (tupla)")
permissions = {"member", "group"}
print(f"O tipo é {type(permissions)} (set)")
permissions.add("root")
print(permissions)  # = {'member', 'root', 'group'}
print(permissions.union({"user"}))  # doesn't modify, only show
# {'member', 'root', 'group', 'user'}
print(permissions)  # = {'member', 'root', 'group'}
print(permissions.intersection({"user", "member"}))
# what both have in common = {'member'}
print(permissions.difference({"group"}))

# Exercício 6: Um conjunto ou set pode ser inicializado utilizando-se também
# o método set() . Inicialize uma variável com essa função var = set()
# e adicione seu nome ao conjunto utilizando um dos métodos vistos acima.
# Depois, imprima a variável e confira se o retorno é: {'seu_nome'}.
info_user = set()
info_user.add("Ilan")
info_user.add("Herbach")
print(info_user)

# frozenset([]) = set imutável
permissions = frozenset(["member", "group"])
print(permissions.union({"user"}))  # = frozenset({'member', 'group', 'user'})
print(permissions.intersection({"user", "member"}))  # = frozenset({'member'})
print(permissions.difference({"group"}))  # = frozenset({'member'})

# Dicionários (dict)
people_by_id = {
    1: "Cássio",
    2: "João",
    3: "Felipe",
}  # elementos no formato "chave: valor" separados por vírgula,
# envolvidos por chaves
people_by_name = {
    "Cássio": 1,
    "João": 2,
    "Felipe": 3,
}  # outro exemplo, dessa vez usando strings como chaves (ao contrário de JS,
# as aspas duplas são obrigatórias)
# elementos são acessados por suas chaves
people_by_id[1]  # saída: Cássio
# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Cássio"), (2, "João"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores
print(people_by_name["Cássio"])

# Exercício 6: Insira no objeto uma nova propriedade com o nome de chave
# "recorrente" e o valor "Sim". Em seguida, imprima o objeto no console.
info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
info["recorrente"] = "Sim"
print(info)

# Exercício 7 Remova a propriedade cuja chave é "origem"
# e imprima o objeto no console.
info.pop("origem")
print(info)
