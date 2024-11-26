# Criando um dicionário
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Pegando um valor de um dicionário
print(programming_dictionary["Function"])

# Adicionando mais itens em um dicionário
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Criando um dicionário vazio
empty_dicionary = {}

# Esvaziando um dicionário existente
# programming_dictionary = {}
# print(programming_dictionary)

# Editando um item em um dicionário
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary)