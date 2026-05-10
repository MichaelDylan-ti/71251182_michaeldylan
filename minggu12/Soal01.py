dictionary = eval(input("Dictionary : "))
print("\nkey\tvalue\titem")

for key in dictionary:
    print(key, "\t", dictionary[key], "\t", key)