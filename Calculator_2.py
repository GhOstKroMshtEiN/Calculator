def Calculator(a,operation,b):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
namber_1 = int(input("Введиет первое число: "))
op = input("Какую операцю вы хотите провести: (+, -) ")
namber_2 = int(input("Введите второе число: "))
print(Calculator(namber_1, op, namber_2))