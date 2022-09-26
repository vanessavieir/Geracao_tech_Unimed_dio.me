nome = "VaNessA"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá , seja bem vindo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))



nome = "Vanessa"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Vanessa", "idade": 21}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")


nome = "Vanessa Ferreira Vieira"

print(nome[0])
print(nome[-2])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])

nome = "Vanessa"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============
    1 - Depositar
    2 - Sacar
    0 - Sair
    ================================
            Obrigado por usar nosso sistema!!!!
"""
)