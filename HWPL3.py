# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


my_list = [2, 3, 5, 9, 3]
print(sum(my_list[1::2]))


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если остается 1 элемент без пары - умножаем его самого на себя.

my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list)


# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

a = int(input('Enter the number: '))
b = ''
while a > 0:
    b = str(a % 2)+b
    a = a//2
print(b)

# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

a = int(input('Enter the number: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')