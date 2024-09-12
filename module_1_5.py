# Тема: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = "Integer", 7, 5, True
print(immutable_var)
# immutable_var[3] = 10 # кортеж не поддерживает обращение по элементам
# print(immutable_var)
mutable_list = ([2, 4, 6, 7], 5)
print(mutable_list)
mutable_list[0][3] = 9
print(mutable_list)
