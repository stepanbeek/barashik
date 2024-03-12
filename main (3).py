#задача 1
try:
    n = int(input("Введите размерность одномерного массива: "))
    if n <= 0:
        raise ValueError("Размерность массива должна быть положительным числом.")
    
    a = [i+1 for i in range(n)] 
    print("Исходный массив:", arr)
    
    b = [x**2 for x in arr]
    print("Квадраты элементов массива:", squared_arr)
    
    c = [x**3 for x in arr]
    print("Кубы элементов массива:", cubed_arr)
    
except ValueError as e:
    print(f"Ошибка: {e}")
#Задача 2
def find_minimum(a, b, c):
    return min(a, b, c)

go1 = int(input("Введите первое число: "))
go2 = int(input("Введите второе число: "))
go3 = int(input("Введите третье число: "))

result = minimum(go1, go2, go3)
print("Наименьшее число: ", result)
#Задача 3 
a = input("Введите символ: ")
b = int(input("Введите целое число: "))

c = ord(a) % b
print("Остаток от деления кода символа на число:", c)
#Задача 4
input_symbol = input("Введите символ: ")
input_number = float(input("Введите вещественное число: "))
result = int(input_number) // ord(input_symbol)
print("Целая часть от деления числа на код символа:", result)
#задача 5
x1, y1 = map(float, input("Введите координаты вершины A (x y): ").split())
x2, y2 = map(float, input("Введите координаты вершины B (x y): ").split())
x3, y3 = map(float, input("Введите координаты вершины C (x y): ").split())

a = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

print("Площадь треугольника:", a)
