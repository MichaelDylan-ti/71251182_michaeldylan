data_list = eval(input("Sebelum konversi (List): ")) #[1, 2, 3, 2, 4, 1, 5]
data_set = set(data_list)
print(f"Sesudah konversi (Set) : {data_set}")
print()

data_set2 = data_set
print(f"Sebelum konversi (Set) : {data_set2}")
data_list2 = list(data_set2)
print(f"Sesudah konversi (List): {data_list2} ")
print()

data_tuple = eval(input("Sebelum konversi (Tuple): ")) #(7, 8, 9, 7, 8, 10)
data_set3 = set(data_tuple)
print(f"Sesudah konversi (Set)  : {data_set3}")
print()

data_set4 = data_set3
print(f"Sebelum konversi (Set)  : {data_set4}")
data_tuple2 = tuple(data_set4)
print(f"Sesudah konversi (Tuple): {data_tuple2}")