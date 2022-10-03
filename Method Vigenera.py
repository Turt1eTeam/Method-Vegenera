alf = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

list1 = []
list2 = []
list3 = []

index1=[]
index2=[]
index = 0

message = input('Введите сообщение: ')
key = input('Введите ключ: ')
change = input('Кодирование / Декодирование :')

list1 = list(message)
key = list(key)

def Code():
    k=0
    for i in range(len(message)):
        list2.append(key[k])
        if(k<len(key)):
            k+=1
        if(k>=len(key)):
            k=0
    for i in range(len(message)):
        for sym in alf:
            if(list1[i] == sym):
                index1.append(alf.index(sym))
            if(list2[i] == sym):
                index2.append(alf.index(sym))

    for i in range(len(index1)):
        index = index1[i] + index2[i]
        if (index <=33):
            list3.append(alf[index])
        if (index > 33):
            list3.append(alf[index-33])

    print('Результат: ',end='')
    for i in list3:
        print(i,end='')
    print()
            

def Decode():
     k=0
     for i in range(len(message)):
        list2.append(key[k])
        if(k<len(key)):
            k+=1
        if(k>=len(key)):
            k=0
     for i in range(len(message)):
        for sym in alf:
            if(list1[i] == sym):
                index1.append(alf.index(sym))
            if(list2[i] == sym):
                index2.append(alf.index(sym))

     for i in range(len(index1)):
        index = index1[i] - index2[i]        
        if (index > 0):
            list3.append(alf[index])
            #print(index)
           
        if (index < 0):
            
            list3.append(alf[index+33])
            #print(index+33)
           

     print('Результат: ',end='')
     for i in list3:
        print(i,end='')
     print()

if(change == 'K' or change == 'k' or change == 'К' or change == 'к' ):
    Code()

if(change == 'D' or change == 'd' or change == 'Д' or change == 'д' ):
    Decode()