tickets = int(input("Сколько билетов Вы хотите приобрести?:")) 
tickets_list = list(range(1, tickets +1)) 

price_all = []
for i in tickets_list:
    while True:
        try:
            age = int(input("Сколько лет посетителю ?:"))
        except ValueError:
            print ('Неправильный тип переменной') 
            continue 
        break
        

    if 18 <= age <= 25:
        price = 990
        price_all.append(int(price))
    elif age >25:
        price = 1390
        price_all.append(int(price))
    else:
        price = 0
        price_all.append(int(price))
        print ()
    print (price_all)
s = sum(price_all)
if tickets > 3: 
    s = s/100*90
    print ('Общая стоимость с учетом скидки :', s)
else:
    s = s
    print ("Общая стоимость : ", s)