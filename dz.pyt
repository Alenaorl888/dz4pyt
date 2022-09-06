#Задача 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#print ('Введите число обозначающую день недели')
#day = int(input())
#if 6 <= day <= 7:
   # print('Это выходной день недели')

#elif 0 < day < 6:
    #print('Это рабочий день недели')
#else:
    #print('введите число вне диапазона от 1 до 7')

#задача 2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#def logical_statement(x, y, z):
    #print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    #return (not (x or y or z)) == (not x and not y and not z)
#if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
#logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
#logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    #print("Истинно")
#else:
    #print("Ложно")

#x = int(input('Введите число x '))
#y = int(input('Введите число y '))
#z = int(input('Введите число z '))

#a = x * y * z
#b = x + y + z

#if a > 0:
     #a = 0
#elif a < 1:
 #   a = 1
#if b > 0:
#     b = 1
#elif b < 1:
#     b = 1

#if a == b:
 #    print('Утверждение истинно')
#elif a != b:
#     print('Утверждение ложно')

#leftSide = not (x or y or z)
#rightSide = not x and not y and not z
#result = leftSide == rightSide

#if result == True:
#     print('Утверждение истинно')
#else:
     #print('Утверждение ложно')

 #задача 3.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

#n = int(input('input quarter number: '))
#if n < 1 or n > 4:
     #print('Please, repeat the input')
#elif n == 1:
    # print('x > 0 and y > 0')
#elif n == 2:
   #  print('x < 0 and y > 0')
#elif n == 3:
    # print('x < 0 and y < 0')
#elif n == 4:
    # print('x > 0 and y < 0')

    #Напишите программу, которая принимает на вход координаты двух точек  и находит расстояние между ними в 2D пространстве.
    

print('Enter coordinates point А:')

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ввод целых чисел!")
                
    return a

def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment

print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")


