# Lista initiala
lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f"Lista initiala este -> {lista_initiala}")

# lista sortata ascendent
lista_sortata_asc = sorted(lista_initiala)
print(f"Lista sortata este ascendent -> {lista_sortata_asc}")

# lista sortata descendent
lista_sortata_desc = lista_sortata_asc[::-1]
print(f"Lista sortata descendent este -> {lista_sortata_desc}")

# Afisarea numerlor cu indici pari din lista
lista_indici_pare = lista_initiala[0::2]
print(f"Numerele de pe indicii pare din lista -> {lista_indici_pare}")

# Afisarea numerelor cu indici impari din lista
lista_indici_impari = lista_initiala[1::2]
print(f"Numerele de pe indicii impari din lista -> {lista_indici_impari}")

# Afisarea numerelor din lista care sunt multipli ai lui 3
lista_multipli_3 = lista_sortata_asc[2::3]
print(f"Numerele care sunt multiplii ai lui 3 -> {lista_multipli_3}")

print(f"Lista initiala a ramas -> {lista_initiala}")



