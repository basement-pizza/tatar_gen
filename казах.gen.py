import random

first1 = ['Хан', 'Бан', 'Жыл', 'Ай', 'Тян', 'Чин', 'Дрын']
last1 = ['нур', 'бек', 'дыз', 'ник', 'гык', 'гис', 'кин']

first2 = ['Хан', 'Бан', 'Жыл', 'Ай', 'Тян', 'Чин', 'Дрын']
middle2 = ['нур', 'бек', 'дыз', 'ник', 'гык', 'гис', 'кин']
last2 = ['ов', 'ченко', 'ыч', 'ович', 'ус']

symb = ['@', '_', '#', '№', '', ' ']
smile = [' :3', '9_9', ' <3', ' 0_0', ' :/']

true_false_num = random.randint(0,1)
true_false_name1 = random.randint(1,3)
true_false_smile = random.randint(0,5)
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)

_symb = random.choice(symb)
_symb2 = random.choice(symb)

_1_1 = random.choice(first1)
_3_1 = random.choice(last1)

_1_2 = random.choice(first2)
_2_2 = random.choice(middle2)
_3_2 = random.choice(last2)

name1 = _1_1+_3_1
name2 = _1_2+_2_2+_3_2

if true_false_smile == 5:
    _smile = random.choice(smile)
else:
    _smile = ''
    
if true_false_name1 == 3:
    name1 = ''
else:
    name1 = name1
    
if true_false_num == 1:
    num_fin = num1 + num2
else:
    num_fin = ''  
    _symb = ''
    
print(name1, _symb2, name2, _symb, num_fin, _smile, sep='')