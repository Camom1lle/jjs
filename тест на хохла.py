import time
import random
num=int(0)
k=int(50)
print('тест на хохла, отвечйте "да" или "нет"')
print('вы любите сало?')
answer1=str(input())
if answer1=='да':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('ваша фамилия заканчивается на "о"?')
answer1=str(input())
if answer1=='да':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('вы любите хрюкать?')
answer1=str(input())
if answer1=='да':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('вы знаете украинский язык?')
answer1=str(input())
if answer1=='да':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('вы хохол?')
answer1=str(input())
if answer1=='да':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('у вас дома есть газ?')
answer1=str(input())
if answer1=='нет':
    k=k+1
else:
    k=k-1
answer1=str(0)
print('вас зовут Лёша?')
answer1=str(input())
if answer1=='да':
    k=k+100
else:
    k=k-1
answer1=str(0)
print('идет определение нации')
time.sleep(2)
num=[random.randint(0,25)]
print('загрузка звершена на',num)
num=0
time.sleep(2)
num=[random.randint(26,50)]
print('загрузка звершена на',num,'%')
num=0
time.sleep(2)
num=[random.randint(51,75)]
print('загрузка звершена на',num,'%')
num=0
time.sleep(2)
num=[random.randint(76,100)]
print('загрузка звершена на',num,'%')
num=0
time.sleep(2)
print('загрузка звершена на [100] %')
time.sleep(2)
if k>=50:
    print('пошел нахуй хохлятина')
else:
    print('поздравляю вы не хохол')