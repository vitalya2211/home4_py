import random
import turtle as t
def turtle():
    t.shape('turtle')
    t.shapesize(2)
    t.color('black','blue')
    t.speed(200)
    t.begin_fill()

    for step in range(60):
        t.forward(6)
        t.right(6)
    t.end_fill()
   
def rle_encode(data):
   encoding = ''
   prev_char = ''
   count = 1
   if not data: 
       return ''
   for char in data:
      if char != prev_char:
          if prev_char:
             encoding += str(count) + prev_char
          count = 1 
          prev_char = char 
      else:
          count += 1
   else:
         encoding += str(count) + prev_char
   return encoding
def rle_decode(data):
   decode = ''
   count = '' 
   for char in data: 
      if char.isdigit(): 
         count += char
      else:
          decode += char * int(count)
          count = '' 
   return decode
def sieve(num:int)->set:
    """решето Эратосфена до заданного числа"""
    result = []
    for i in range(num + 1):
        result.append(i)
    result[1] = 0
    i = 2
    while i <= num:
        if result[i] != 0:
            j = i + i
            while j <= num:
                result[j] = 0
                j = j + i
        i += 1
    result = set(result)
    result.remove(0)
    result=list(result)
    return result
def mult_dig(num:int)->set:
    arr_set=sieve(num)
    i=0
    if num in arr_set:
        return num
    result=[]
    while num:
        
        while num % arr_set[i]==0:
            result.append(arr_set[i])
            num=num//arr_set[i]
            if num in arr_set: 
                result.append(num)
                return result
        i=i+1

    return result
def enigma(text:str)->str:
    """шифрование методом сдвига букв в ascii"""
    key = 1
    world=[]
    for i in text:
        world.append(ord(i)+1)
    
    del text
    text=[]
    for i in world:
        text.append(chr(i))
    result =''.join(map(str,text))
    return result
def encryption(text:str)->str:
    """расшифровка с помощью ascci и ключа"""
    key=1
    world=[]
    for i in text:
        world.append(ord(i)-1)
    del text
    text=[]
    for i in world:
        text.append(chr(i))
    result=''.join(map(str,text))
    return result


try:
#1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#N = 20 -> [2,5]
#N = 30 -> [2, 3, 5]
    N=int(input('введите натуральное число для составления списка простых множителей -> '))
    if N>0:
        print(mult_dig(N))
    else: print('введено отрицательное число!')

#2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
#элементов исходной последовательности. Не использовать множества.
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
    print('задать последовательность чисел, вывести уникальные элементы последовательности')
    rand_list=[random.randint(1,8) for i in range(15)]
    new_list_set=[rand_list[0]]
    i=0
    print(rand_list)
    while i < len(rand_list):
        if rand_list[i] in new_list_set:
            i+=1
            continue
        else:
            new_list_set.append(rand_list[i])
        i+=1
    print(new_list_set)

#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
#Нужно перезаписать файл.
#Пример:
#Ангела Меркель 5
#Андрей Валетов 5
#Фредди Меркури 3
#Анастасия Пономарева 4
#Программа выдаст:
#АНГЕЛА МЕРКЕЛЬ 5
#АНДРЕЙ ВАЛЕТОВ 5
#Фредди Меркури 3
#Анастасия Пономарева 4
    file = open('home_ed.txt','w')
    file.write('\
    Ангела Меркель 5\n\
    Андрей Валетов 5\n\
    Фредди Меркури 3\n\
    Анастасия Пономарева 4\n')
    file.close()
    arr=[]
    with open(r'home_ed.txt','r') as file:
        for line in file:
            arr.append(line)
    print(arr)
    j=0
    for i in arr:
        if i[-2]=='5':
            arr[j]=i.upper()
        j+=1
    with open('home_ed.txt','w') as file:
        for line in arr:
            file.write(line)
    print(arr)
#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество
# символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" 
# можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
#Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию,
# которая спрашивает ключ, считывает текст и дешифровывает его.
    string=input('шифр Цезаря\nВведите текст->')
    string=enigma(string)
    print(string)
    with open('encr_text','w') as file2:
        file2.write(string)
    file2=open('encr_text')
    string=file2.read()
    file2.close
    string=encryption(string)
    print(string)


#5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
#Входные и выходные данные хранятся в отдельных текстовых файлах.
#файл первый:
#AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
#файл второй:
#сжатый текст.
    val=rle_encode('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
    with open('файл2.txt','w') as file3:
        file3.write(val)
    #print(val)
    with open('файл2.txt','r') as file3:
        cripto=file3.read()
    with open('файл1.txt','w') as file3:
        file3.write(rle_decode(cripto))
    turtle_run=input('запустить черепашку?y/n -> ')
    if turtle_run=='y':
        target=turtle()
    else: print('by))')


except ValueError:
    print(EOFError)