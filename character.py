personagens = []
defesa_big = 0
ataque_big = 0
nome_big_ataque = ""
nome_big_defesa = ""

for i in range(3):
    nome = str(input(""))
    ataque = (int(input("")))
    defesa = (int(input("")))
    personagens.append([nome,(ataque,defesa)])
    if ataque > ataque_big:
        ataque_big = ataque
        nome_big_ataque = nome
    if defesa > defesa_big:
        defesa_big = defesa
        nome_big_defesa = nome

print("Ataque ", nome_big_ataque, ataque_big)
print("Defesa ", nome_big_defesa, defesa_big)