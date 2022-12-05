#

#Напишите программу, печатающую столбик таблицу умножения такого вида:
print('Таблица умножения') 
n = int(input('Введите n: '))
for i in range(1, 11):
    print(f'{n} * {i} = {n*i}')
#Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.
a=0
for i in range (1,51):
    if i %7==0 or i %5==0:
        a+=i
print(a)
#Найти сумму чисел от 100 до 200, кратных 17
summ=0
a=100
while a<=200:
    if a%17==0:
        summ+=a
    a+=1
print(summ)
#Вводят 8 чисел. Найти их произведение (только положительных).
i=0
j=0
while i<8:
    i+=1
    a=float(input(f"{i} Sisesta A: "))
    if int(a)>0: 
        j=i*i*i*i*i*i*i*i
print(j)
#Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
n=int(input("Sisesta arv: "))
j=0
for i in range(1,n+1):
    j+=i
print(j)
#В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
S=float(input("Panusesumma: "))
N=float(input("Aeg:  ", ))
a=S+S*0.03*N
print("Panusesumma kokku", a)
#Вводят 15 чисел. Определить, сколько среди них целых.
j=0
i=0
while i<15:
    i+=1
    a=float(input(f"{i} Sisesta A: "))
    if int(a)==a: j+=1 
print(j)


