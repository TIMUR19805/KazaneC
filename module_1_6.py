# Тема: "Словари и множества"
# Работа со словарями:
my_dict = {"Ildar" : 1975, "Natalia" : 1977, "Timur" : 1980}
print(my_dict)
print(my_dict["Timur"])
print(my_dict.get("Ruslan"))
my_dict.update({"Rustem" : 1978, "Marat" : 1984})
print(my_dict)
a = my_dict.pop("Natalia")
print(my_dict)
print(a)

# Работа с множествами:
my_set = {2, 4, 5, 6, 7, 1, 2, 4, 5, True, (1, 2, 3), "String"}
print(my_set)
my_set.add(0)
print(my_set)
my_set.add(3)
print(my_set)
print(my_set.discard(7))
print(my_set)