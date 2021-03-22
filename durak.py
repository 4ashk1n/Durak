kolvo='начальное'
masti=['крести',"черви","буби","пики"]
numbers52=["2","3","4","5","6","7","8","9","10","валет","дама","король","туз"]
numbers36=["6","7","8","9","10","валет","дама","король","туз"]
numbers24=["9","10","валет","дама","король","туз"]

def skolko_kozir(kozir,cardsbot):
    res=0
    for k in cardsbot:
        if k.split(' ')[1]==kozir:
            res+=1
    return res



def proverka(a,b,kozir):
    #a on b     a,b='number mast'
    if a.split(' ')[-1] in b and kozir not in a and numbers52.index(a.split(' ')[0])>numbers52.index(b.split(' ')[0]):   #Обычная на обычную
        return 1        
    elif kozir in a and kozir not in b:    #Козырь на обычную
        return 1
    elif kozir in a and kozir in b and numbers52.index(a.split(' ')[0])>numbers52.index(b.split(' ')[0]): #Козырь козырь
        return 1
    else:
        return 0


def prov_podkid(a,stol):
    a1=a.split(' ')[0]
    stol1=set()
    #print(stol)
    #print(a1)
    
    for k in stol:
        stol1.add(k.split(' ')[0])
    if a1 in stol1:
        return True
    return False

def user_cards(cards,stol):
    print("Ваши карты:")
    for k in range(len(cards)):
        n=''
        if cards[k] in stol:
            n='(УЖЕ НА СТОЛЕ)'
        print(k+1,': ',cards[k],' ',n,sep='')

def podkid_bot(cardsbot,stol):
    stol1=set()
    delete=[]
    for k in stol:
        stol1.add(k.split(' ')[0])
    for k in cardsbot:
        if k.split(' ')[0] in stol1 and k not in stol:
            print("Подкидываю: ",k)
            stol.append(k)
            delete.append(k)
    for k in delete:
        cardsbot.remove(k)
    return cardsbot,stol

def sortirovka(cardsbot):
    #Сортировка массива по индексам в намберс52        n!
    #return sorted(cardsbot, key=lambda card: numbers52.index(card.split(' ')[0]))
    cardsbot=sorted(cardsbot, key=lambda card: numbers52.index(card.split(' ')[0]))
    cardsbot=sorted(cardsbot, key=lambda card: masti.index(card.split(' ')[1]))
    return cardsbot


def kozir_end(kozir,cardsbot):
    k=len(cardsbot)-1
    kolvo_kozir=skolko_kozir(kozir,cardsbot)
    for card in range(len(cardsbot)):
        if kolvo_kozir<=0:
                break
        if cardsbot[card].split(' ')[1]==kozir:
            while cardsbot[k].split(' ')[1]==kozir and k>=0:
                
                if cardsbot[k].split(' ')==cardsbot[card].split(' '):
                    break
                k-=1
                kolvo_kozir-=1
                #print(cardsbot[k])
            if cardsbot[k].split(' ')==cardsbot[card].split(' '):
                break
            
            
            vremennaya_fignya=cardsbot[card]
            cardsbot[card]=cardsbot[k]
            cardsbot[k]=vremennaya_fignya
            kolvo_kozir-=1
            
            if kolvo_kozir==0:
                break
            
            
            
    return cardsbot

def na4alo(cards,cardsbot,kozir):
    minimal=9999
    res=0   #0 - юзер, 1 - бот
    for k in cards:
        if kozir in k and numbers52.index(k.split(' ')[0])<minimal:
            minimal=numbers52.index(k.split(' ')[0])
            res=0
    for k in cardsbot:
        if kozir in k and numbers52.index(k.split(' ')[0])<minimal:
            minimal=numbers52.index(k.split(' ')[0])
            res=1
    return res


def k52():                                                                  #52 КАРТЫ
    global koloda
    #print(52)
    koloda=[]
    for number in numbers52:
        for mast in masti:
            koloda.append(number+' '+mast)
    koloda=set(koloda)
    koloda=list(koloda)
##    print(koloda)

def delete_stol(cards,cardsbot,stol):
##    print(stol)
    for k in stol:
        
##        print(k)
##        print(k in cards)
##        print(k in cardsbot)
        if k in cards:
            cards.remove(k)
        if k in cardsbot:
            cardsbot.remove(k)
    return cards,cardsbot


def k36():
    global koloda
    #print(36)
    koloda=[]
    
    for number in numbers36:
        for mast in masti:
            koloda.append(number+' '+mast)
    koloda=set(koloda)
    koloda=list(koloda)
##    print(koloda)

def k24():
    global koloda
    #print(24)
    koloda=[]
    for number in numbers24:
        for mast in masti:
            koloda.append(number+' '+mast)
    koloda=set(koloda)
    koloda=list(koloda)
##    print(koloda)

endkoloda=0
def vidacha(cards,koloda,kozir):
    global endkoloda
    for k in range(6-len(cards)):
        if len(koloda)==0:
            endkoloda=1
            break
        cards.append(koloda[0])
        koloda.pop(0)
    #print(cards)
    cards=sortirovka(cards)
    #print(cards)
    cards=kozir_end(kozir,cards)
    cards[len(cards)-skolko_kozir(kozir,cards):len(cards)]=sortirovka(cards[len(cards)-skolko_kozir(kozir,cards):len(cards)])
    cards[0:len(cards)-skolko_kozir(kozir,cards)]=sortirovka(cards[0:len(cards)-skolko_kozir(kozir,cards)])
    return cards,koloda
    
    

def game(koloda): #ИГРA
    proverkaoshibki = 0
    proverkaoshibki1 = 0
    cards=[]
    cardsbot=[]
    kozir=koloda[-1].split(' ')[-1]
    cards,koloda=vidacha(cards,koloda,kozir)
    cardsbot,koloda=vidacha(cardsbot,koloda,kozir)
    #Карты раздал
    bito=[]
    stol=[]
    beginner=na4alo(cards,cardsbot,kozir)
    print('КОЗЫРЬ: ',kozir)
    #print('КАРТЫ ИГРОКА: ',cards)
    
    #0 - юзер, 1 - бот
    if beginner==0:
        print("Вы начинаете")
    while True:
        cards,koloda=vidacha(cards,koloda,kozir)
        cardsbot,koloda=vidacha(cardsbot,koloda,kozir)
##        print('КАРТЫ БОТА: ',cardsbot)
        if beginner==0:                                             #юзер, бот отбивается
            if proverkaoshibki1==0:
                user_cards(cards,stol)
                print("Ваш ход")
            
            card=input()
            try:
                card=int(card)-1
                if card>=len(cards) or card<0:
                    print("Ошибка. Попробуйте еще раз")
                    proverkaoshibki1=1
                    continue
            except:

                if card.lower()=='бито':
                    for biti in stol:
                        bito.append(biti)
                    cards,cardsbot=delete_stol(cards,cardsbot,stol)
                    stol.clear()     
                    beginner=1
                    proverkaoshibki1 = 0
                    continue

                elif card.lower()=='беру':                                                                #ЮЗЕР БЕРЕТ
                    cards,cardsbot=delete_stol(cards,cardsbot,stol)
                    cardsbot,stol=podkid_bot(cardsbot,stol)
                    
                    for vzal in stol:
                        cards.append(vzal)
                        try:
                            cardsbot.remove(vzal)
                        except:
                            continue
                    stol.clear()
                    beginner=1
                    proverkaoshibki1 = 0
                    continue

                else:
                    print("Ошибка. Попробуйте еще раз")
                    proverkaoshibki1 = 1
                    continue

            if cards[card] in stol:
                print("Карта уже на столе. Выберите другую")
                continue
            if prov_podkid(cards[card],stol)==False and len(list(stol))>0:
                print("Невозможно положить эту карту. Выберите другую")
                continue
            proverkaoshibki1 = 0
            stol.append(cards[card])
            if len(koloda) == 0 and len(cards) == 1:
                print("Вы выиграли")
                break
            endc=0
            for k in cardsbot:
                if proverka(k,cards[card],kozir)==1 and k not in stol:
                    print(' ')
                    print(k.capitalize())
                    print(' ')
                    stol.append(k)
                    endc=1
                    break
            if len(koloda) == 0 and len(cardsbot) == 1 and endc==1:
                print("Вы проиграли")
                break
            if endc==0:
                user_cards(cards, stol)
                print("Беру")                                                                               #БОТ БЕРЕТ, ПОДКИДЫВАНИЕ
                print("Если вы хотите подкинуть карты, то напишите, пожалуйста, их номера через пробел")
                print('В конце ввода введите ОК')
                while True:
                    proverkapodkida=0
                    podkid=input().split()
                    for podkidi in range(len(podkid) - 1):
                        try:
                            proverkapodkida=int(podkid[podkidi])
                            if proverkapodkida<1 or proverkapodkida>len(cards):
                                print("Некорректная карта. Попробуйте еще раз")
                                proverkapodkida = 999
                                break
                        except:
                            print("Некорректный ввод. Попробуйте еще раз")
                            proverkapodkida=999
                            break
                    if proverkapodkida==999:
                        continue
                    for podkidi in range(len(podkid)-1):
                        if prov_podkid(cards[int(podkid[podkidi])-1],stol)==True and cards[int(podkid[podkidi])-1] not in stol:
                            stol.append(cards[int(podkid[podkidi])-1])
                        else:
                            print("Карта",cards[int(podkid[podkidi])-1],"не может быть подкинута")
                    for vzal in stol:
                        if vzal not in cardsbot:
                            cardsbot.append(vzal)
                        #print(cardsbot)
                        try:
                            cards.remove(vzal)
                        except:
                            continue
                    #print(cardsbot)
                    #print(stol)
                    stol.clear()
                    #print(cardsbot)
                    #print(stol)
                    beginner=0
                    break
                continue




        elif beginner==1:#БОТ ХОДИТ
            if proverkaoshibki==0:
                print('ХОД БОТА')
                pokaz=0
                minimalcard=0
                cardboti=0
                if len(stol)==0:
    ##                print(3)
                    pokaz=1
                    while cardsbot[cardboti].split()[-1]!=kozir:
                        if cardsbot[cardboti].split()[0]<cardsbot[minimalcard].split()[0]:
                            minimalcard=cardboti
                        cardboti+=1
                        if cardboti>=len(cardsbot):
                            break
                else:
                    for cardboti in range(len(cardsbot)):
                        if prov_podkid(cardsbot[cardboti],stol)==True and cardsbot[cardboti] not in stol:
                            minimalcard=cardboti
                            pokaz=1
                            break
                if pokaz==0:
                    print("Бито")
                    for biti in stol:
                        bito.append(biti)
                    cards,cardsbot=delete_stol(cards,cardsbot,stol)
                    stol.clear()
                    beginner=0
                    continue
                user_cards(cards,stol)
                print('')
                print(cardsbot[minimalcard])
                stol.append(cardsbot[minimalcard])
                if len(koloda) == 0 and len(cardsbot) == 1:
                    print("Вы проиграли")
                    break
                #В стол занесено


##            print('КАРТЫ БОТА: ',cardsbot)
            card=input()
            try:
                card=int(card)-1
                if card>=len(cards) or card<0:
                    print("Ошибка. Попробуйте еще раз")
                    proverkaoshibki = 1
                    continue
            except:
                if card.lower()=='беру':                                                                #ЮЗЕР БЕРЕТ
                    cards,cardsbot=delete_stol(cards,cardsbot,stol)
                    cardsbot,stol=podkid_bot(cardsbot,stol)
                    
                    for vzal in stol:
                        cards.append(vzal)
                        try:
                            cardsbot.remove(vzal)
                        except:
                            continue
                    
                   
                    stol.clear()
                    beginner=1
                    #print(1)
                    proverkaoshibki = 0
                    continue
                else:
                    print("Ошибка. Попробуйте еще раз")
                    proverkaoshibki = 1
                    continue
            
            if cards[card] in stol:
                print("Карта уже на столе. Выберите другую")
                proverkaoshibki=1
                continue
            if proverka(cards[card],cardsbot[minimalcard],kozir)==False:
                print("Невозможно положить эту карту. Выберите другую")
                proverkaoshibki = 1
                continue
            stol.append(cards[card])
            if len(koloda) == 0 and len(cards) == 1:
                print("Вы выиграли")
                break
            proverkaoshibki = 0
            




while kolvo not in ['1','2','3']:
    kolvo=input("Выберите количество карт:\n1. 52\n2. 36\n3. 24\n")
    if kolvo=='1':
        k52()
    elif kolvo=='2':
        k36()
    elif kolvo=='3':
        k24()
    else:
        print("Ошибка. Попробуйте еще раз")
        continue
    game(koloda)