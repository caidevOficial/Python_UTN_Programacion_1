mi_primer_set = {1,3,5,7,9,6}
mi_segundo_set = {2,4,6,8,10,3}
mi_tercer_set = {0,2,6}


# Agregar un elemento al set
mi_primer_set.add(11)

# Eliminar un elemento específico del set
mi_primer_set.discard(13)
print(mi_primer_set)

# Quitar un elemento del set
elemento = mi_primer_set.pop()


# Unir los elementos de dos sets en un set resultante
union_dos_set = mi_primer_set.union(mi_segundo_set)

# Obtener los elementos que existan en ambos sets
intersec_dos_set = mi_primer_set.intersection(mi_segundo_set)

# Actualizar un set, con otro  (Similar al union pero sobre si mismo)
mi_primer_set.update(tuple(mi_segundo_set))


print(mi_primer_set)

# Vaciar completamente el set
mi_primer_set.clear()

print(mi_primer_set)
print(elemento)