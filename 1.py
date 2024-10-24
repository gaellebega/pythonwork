def camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

camel_case = input("Enter the name: ")
print("The corresponding snake_case:", camel_to_snake(camel_case))

