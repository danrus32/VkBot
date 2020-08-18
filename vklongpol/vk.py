import requests
import bs4
import config 
import time 
import random 
import re
import sqlite3
import qrcode 
import os
from qrmap import QR as qr
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
#Citate 1
def SteevJobsCitate(text_citate,random_name,group_id,peer_id,user_id,messagetext):
    text_color = (0,0,0)
    text = text_citate
    font = ImageFont.truetype('font/19681.ttf',30)
    img = Image.open('imagetext/1_citate.jpg')
    draw = ImageDraw.Draw(img)
    MAX_W, MAX_H = 800, 600
    w, h = draw.textsize(text, font=font)
    draw.text(((MAX_W - w) / 2, (MAX_H - h) / 2),text,(0,0,0),font=font,align="center")
    img.save('imagetext/photo/'+str(random_name)+'.jpg')
    photo_citate = SendPhotoMessage('imagetext/photo/'+str(random_name)+'.jpg')
    MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage = '',messagetext=messagetext,attachment=photo_citate)


# citate 2
def GoldCitate(text_citate,random_name,group_id,user_id,peer_id,messagetext,user_name):
    text_color = (0,0,0)
    text = user_name + '\n' + text_citate
    font = ImageFont.truetype('font/19681.ttf',12)
    img = Image.open('imagetext/2_citate.jpg')
    draw = ImageDraw.Draw(img)
    MAX_W, MAX_H = 400, 200
    w, h = draw.textsize(text, font=font)
    draw.text(((MAX_W - w) / 2, (MAX_H - h) / 2),text,(0,0,0),font=font,align="center")
    img.save('imagetext/photo/'+str(random_name)+'.jpg')
    photo_citate = SendPhotoMessage('imagetext/photo/'+str(random_name)+'.jpg')
    MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage = '',messagetext=messagetext,attachment=photo_citate)

# citate 2
def WhiteCitate(text_citate,random_name,group_id,user_id,peer_id,messagetext,user_name):
    text_color = (0,0,0)
    text = text_citate
    font = ImageFont.truetype('font/19681.ttf',30)
    font_1 = ImageFont.truetype('font/19681.ttf',50)
    img = Image.open('imagetext/3_citate.jpg')
    draw = ImageDraw.Draw(img)
    MAX_W, MAX_H = 1300, 1200
    MAX_W_2, MAX_H_2 = 1850, 1900
    w, h = draw.textsize(text, font=font)
    draw.text(((MAX_W - w) / 2, (MAX_H - h) / 2),text,(0,0,0),font=font,align="center")
    draw.text(((MAX_W_2 - w) / 2, (MAX_H_2 - h) / 2),user_name,(0,0,0),font=font_1,align="center")
    img.save('imagetext/photo/'+str(random_name)+'.jpg')
    photo_citate = SendPhotoMessage('imagetext/photo/'+str(random_name)+'.jpg')
    MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage = '',messagetext=messagetext,attachment=photo_citate)


def QrGenerate(randomName,peer_id,group_id,user_id,messagetext):
    def ResubQR(messagetext):
        data= re.sub(_COMMANDS[10], "",messagetext)
        data= re.sub(_COMMANDS[11], "",data)
        return data
    date= ResubQR(messagetext)
    img = qrcode.make(date)  
    img.save("qrmap/"+str(randomName)+'.png')
    
    photo =  "qrmap/"+str(randomName)+".png"
    photoqr =SendPhotoMessage(photo)
    SendQR = MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage = 'Готово!',messagetext=messagetext,attachment=photoqr)
#commands
_COMMANDS = ["Привет", "привет", "начать","Начать", "Пока", "пока",'погода','Погода','pogoda','Pogoda','qr','Qr','png','Png','kubik','Kubik','ran','кости','Кости']
_COMMANDS_2 = ['Цитата','бот цитата','цитата','citate','стив цитата','голд цитата','белая цитата','бот','bot','Bot','Бот',"Droid",'/version']
_COMMANDS_3 = ['play','Play','Играть','играть']
#Data Base Users
def Users(user_id,chat_id):
    status = "User"
    db = sqlite3.connect("Users.db")
    sql = db.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS users(Nickname TEXT,user_id Text,chat_id Text,Status Text)")
    sql.execute('''SELECT user_id FROM users WHERE user_id=?''', (user_id,))
    exists = sql.fetchall()
    if not exists:
       sql.execute(f"INSERT INTO users VALUES(?,?,?,?)",(UserName(user_id),user_id,chat_id,status))
       db.commit()
       
    else:
       print("\n")
    db.close()
#true message save
#def DataBaseMessageSaveTrue(user_id,TextMessage):
    # db = sqlite3.connect("MessagesTrue.db")
    # sql = db.cursor()
    # sql.execute("CREATE TABLE IF NOT EXISTS Messages(Nickname TEXT,Time TEXT,user_id Text,TextMessage Text)")
    # db.commit()
    # sql.execute(f"INSERT INTO Messages VALUES(?,?,?,?)",(UserName(user_id),config.Time(),user_id,TextMessage))
    # db.commit()
#Data Base Messages
def DataBaseMessageSave(chat_id,user_id,message_text):
    db = sqlite3.connect("Botlog.db")
    sql = db.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS Messages(Nickname TEXT,Time TEXT,chat_id Text,user_id Text,message_text TEXT)")
    db.commit()
    sql.execute(f"INSERT INTO Messages VALUES(?,?,?,?,?)",(UserName(user_id),config.Time(),chat_id,user_id,message_text))
    db.commit()
    

#kubik 
def kubik (peer_id,group_id,user_id,messagetext):
    kubik_part = random.randint(1,6)
    if kubik_part == 1:
        TextMessage = '🎲Выпало 1!'
        attachament = "kubik/1.jpg"
    if kubik_part == 2:
        TextMessage = '🎲Выпало 2!'
        attachament = "kubik/2.jpg"
    if kubik_part == 3:
        TextMessage = '🎲Выпало 3!'
        attachament = "kubik/3.jpg"
    if kubik_part == 4:
        TextMessage = '🎲Выпало 4!'
        attachament = "kubik/4.jpg"
    if kubik_part == 5:
        TextMessage = '🎲Выпало 5!'
        attachament = "kubik/5.jpg"
    if kubik_part == 6:
        TextMessage = '🎲Выпало 6!'
        attachament = "kubik/6.jpg"
    Keyboard = open('kubik.json',"r",encoding="UTF-8").read()
    attachamentRes = SendPhotoMessage(attachament)
    MessageSend(group_id=group_id,user_id=user_id,messagetext=messagetext,TextMessage=TextMessage,peer_id=peer_id,jsonKeyboard=Keyboard,attachment=attachamentRes)
    

#pogoda    
def pogoda(peer_id,group_id,user_id,messagetext):
    def ResubPogoda(messagetext):
        localite= re.sub(_COMMANDS[6], "",messagetext)
        localite= re.sub(_COMMANDS[7], "",localite)
        localite= re.sub(_COMMANDS[8], "",localite)
        localite= re.sub(_COMMANDS[9], "",localite)
        return localite
    try: 
        localite = ResubPogoda(messagetext)
        ResPogoda = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params = {'q': localite, 'units': 'metric','lang':'ru','APPID':"b9930bca4efd191aba542903b134e0aa"})
        data = ResPogoda.json()
                #print(data)
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage = "В городе" + localite + "\nCейчас температура:\nСредняя:" + str(data['main']['temp']) +"\nMин:" + str(data['main']['temp_min']) +"\nМах"+str(data['main']['temp_min']) + "\nВлажность:" + str(data['main']['humidity'])+"\nВетер:" + str(data['wind']['speed'])+"\n"+data['weather'][0]['description'],messagetext=messagetext)
        if data['main']['temp'] <= 5:
            MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='На улице холодно оденитесь теплее!',messagetext=messagetext)
        elif data['main']['temp'] >= 5:
            MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='На улице нормально!',messagetext=messagetext)
        elif data['main']['temp'] >= 28:
            MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='На улице горечо!',messagetext=messagetext)
       
            
    except KeyError:
            TextMessage = "Город или страна неопознаны!\nГород или страну пиши английскими буквами!"
            MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)

_Function_DroidALLIN = ['BalanceReplisment','balans','bought a case 10','bought a case 100','bought all-in']
#DroidALLIN
def DroidALLIN(group_id,user_id,peer_id,messagetext,Function,BalanceReplismentSumm =None):
    user_id = str(user_id)
    #База пользователя
    def userDataBase(user_id,comand,balance,changebalance):
        
        db = sqlite3.connect("DroidALLIN/Userdb/"+user_id+".db")
        sql = db.cursor()
        sql.execute("CREATE TABLE IF NOT EXISTS User(user_id Text,comand Text,balance INT,changebalance Text)")
        sql.execute(f"INSERT INTO User VALUES(?,?,?,?)",(user_id,comand,balance,changebalance))
        #
        sql.execute('''SELECT user_id,comand,balance,changebalance FROM User WHERE user_id=?''', (user_id,))
        results = sql.fetchall()
        results2 =  sql.fetchall()
        print("UserDataBase\n" +str(results2))
        #
        db.commit()
       
    #Проверка есть ли юзер
    def IfUserExist(user_id):
        user_id = str(user_id)
        db = sqlite3.connect("DroidALLIN/Users.db")
        sql = db.cursor()
        sql.execute("CREATE TABLE IF NOT EXISTS Users (Balance INT,user_id Text,Name Text)")
        db.commit()
        sql.execute('''SELECT user_id FROM Users WHERE user_id=?''', (user_id,))
        exists = sql.fetchall()
        if not exists:
            Name = UserName(user_id)
            sql.execute(f"INSERT INTO Users VALUES(?,?,?)",(0,user_id,Name))
            db.commit()
         
        else :
            sql.execute('''SELECT Balance,user_id,Name FROM Users WHERE user_id=?''', (user_id,))
            results = sql.fetchall()
            results2 =  sql.fetchall()
            print("|User |  V|")
            print(results)   
            print(str(results2))
        
    #Пополняем баланс
    def BalanceReplisment():
        print(BalanceReplismentSumm)
        db = sqlite3.connect("DroidALLIN/Users.db")
        sql = db.cursor()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        print("Balance   " + str(results[0]))
        Summ = results[0]+BalanceReplismentSumm
        print(Summ)
        sql.execute(f'UPDATE Users SET Balance = ? WHERE user_id = ?', ( Summ,user_id))
        db.commit()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        print("New balance   " + str(results[0]))
        
        userDataBase(user_id,Function,results[0],BalanceReplismentSumm)
        jsonKeyboard = open('DroidALLIN/play.json', "r",encoding="UTF-8").read()
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage ="Денги успешно зачислены на ваш баланс!\nДенег на балансе: " + str(Summ)+'$',peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)

    #Получение денег
    def BalancePlusPrize(Prize):
        print(BalanceReplismentSumm)
        db = sqlite3.connect("DroidALLIN/Users.db")
        sql = db.cursor()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        Summ = results[0]+Prize
        sql.execute(f'UPDATE Users SET Balance = ? WHERE user_id = ?', ( Summ,user_id))
        db.commit()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage ="Денги успешно зачислены на ваш баланс!\nДенег на балансе: " + str(Summ)+'$',peer_id=peer_id,messagetext=messagetext)

        
        userDataBase(user_id,_Function_DroidALLIN[3],results[0],'+'+str(Prize))
    def BuyCase(Price):
        print(BalanceReplismentSumm)
        db = sqlite3.connect("DroidALLIN/Users.db")
        sql = db.cursor()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        if results[0] >= Price:
            Summ = results[0]-Price
            sql.execute(f'UPDATE Users SET Balance = ? WHERE user_id = ?', ( Summ,user_id))
            db.commit()
            sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
            results = sql.fetchone()
            
            userDataBase(user_id,_Function_DroidALLIN[3],results[0],BalanceReplismentSumm)
            MessageSend(group_id=config.grupid,user_id=user_id,TextMessage ="Покупка прошла успешно!\nДенег на балансе: " + str(Summ)+'$',peer_id=peer_id,messagetext=messagetext)
            userDataBase(user_id,Function,results[0],'-'+ str(Price))
            balansMoney = True
        else:
            jsonKeyboard = open('DroidALLIN/no_money.json',"r",encoding="UTF-8").read()
            photo = SendPhotoMessage('DroidALLIN/no_money.jpg')
            MessageSend(group_id=config.grupid,user_id=user_id,TextMessage ="Недостаточно денег\nХотите пополнить баланс?",peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard,attachment=photo)
            balansMoney = False
        return balansMoney
    def Balans():
        db = sqlite3.connect("DroidALLIN/Users.db")
        sql = db.cursor()
        sql.execute('''SELECT Balance FROM Users WHERE user_id=?''', (user_id,))        
        results = sql.fetchone()
        Summ = results[0]
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage ="Денег на балансе: " + str(Summ)+'$',peer_id=peer_id,messagetext=messagetext)

    def Case_1 ():
        
        Price = 10
        prizes = [1,2,5,10,20,25,50,100]
        def randoms():
            a = random.randint(1,100)
            return a
        randomPrize = randoms()
        Prize = 0
        if randomPrize >= 25:
            Prize = prizes[0]
        if randomPrize >= 50:
            Prize = prizes[1]
        if randomPrize >= 75:
            Prize = prizes[2]
        if randomPrize >= 87:
            Prize = prizes[3]
        if randomPrize >= 93:
            Prize = prizes[4]
        if randomPrize >= 96:
            Prize = prizes[5]
        if randomPrize >= 98:
            Prize = prizes[6]
        if randomPrize >= 100:
            Prize = prizes[7]
        if Prize == 0 :
            return Case_2
        Buy = BuyCase(Price)
        if Buy == True:
            TextMessage = "Вам выпало :  "+ str(Prize) + '$'
                
            jsonKeyboard= open('DroidALLIN/esheo_raz_10.json',"r",encoding="UTF-8").read()
            MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
            BalancePlusPrize(Prize)
        else:
            pass
    def Case_2 ():
        
        Price = 100
        
        
        prizes = [10,20,30,100,200,500]
        def randoms():
            a = random.randint(1,100)
            return a
        randomPrize = randoms()
        Prize = 0
        if randomPrize >= 25:
            Prize = prizes[0]
        if randomPrize >= 50:
            Prize = prizes[1]
        if randomPrize >= 75:
            Prize = prizes[2]
        if randomPrize >= 90:
            Prize = prizes[3]
        if randomPrize >= 98:
            Prize = prizes[4]
        if randomPrize >= 100:
            Prize = prizes[5]
        if Prize == 0 :
            return Case_2
        Buy = BuyCase(Price)
        if Buy == True:
            TextMessage = "Вам выпало :  "+ str(Prize) + '$'
            
            jsonKeyboard= open('DroidALLIN/esheo_raz_100.json',"r",encoding="UTF-8").read()
            MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
            BalancePlusPrize(Prize)
        else:
            pass
    def Case_3 ():
        
        Price = 50
        
       
        prizes = [5,100]
        def randoms():
            a = random.randint(1,2)
            return a
        randomPrize = randoms()
        Prize = 0
        if randomPrize == 1:
            Prize = prizes[0]
        if randomPrize == 2:
            Prize = prizes[1]
        if Prize == 0 :
            return Case_2
        Buy = BuyCase(Price)
        if Buy == True:
            TextMessage = "Вам выпало :  "+ str(Prize) + '$'
            
            jsonKeyboard= open('DroidALLIN/esheo_raz_allin.json',"r",encoding="UTF-8").read()
            MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
            BalancePlusPrize(Prize)
        else:
            pass
    #Проверка есть ли юзер
    IfUserExist(user_id)       
    if Function == _Function_DroidALLIN[0]:
        BalanceReplisment()
    if Function == _Function_DroidALLIN[1]:
        Balans()
    if Function == _Function_DroidALLIN[2]:
            Case_1()
    if Function == _Function_DroidALLIN[3]:
            Case_2()
    if Function == _Function_DroidALLIN[4]:
            Case_3()


#clear tag 
def _clean_all_tag_from_str(string_line):
    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True
    
    return result



#User Name
def UserName(user_id):
    request = requests.get("https://vk.com/id"+str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")
    
    user_name = _clean_all_tag_from_str(bs.findAll("title")[0])
    
    return user_name.split()[0]
#Server authentification
def auth_server ():
    auth_vk = requests.get("https://api.vk.com/method/groups.getLongPollServer?group_id={0}&access_token={1}&v={2}".format(config.grupid,config.token,'5.95'))
    return auth_vk.json()

#Ceck events
def server_ceck(key,server,ts):
        ServerResponse = requests.get("{server}?act=a_check&key={key}&ts={ts}&wait=25".format(server=server,key=key,ts=ts))
        return ServerResponse.json()
#MessageCeckMessage):
def MessageCeck(Message):
    user_id = Message['object']["from_id"]
    peer_id = Message['object']["peer_id"]
    messagetext = Message['object']['text']
    group_id = Message["group_id"]
    #members
    if messagetext =='members' or messagetext == 'Members':    
        ConversationMembers(peer_id,user_id,messagetext)
        
    #random_id = config.random
    if messagetext == _COMMANDS[0] or messagetext == _COMMANDS[1] :
        TextMessage = "Привет {UserName} я бот!".format(UserName=UserName(user_id))
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
        Users(user_id = user_id,chat_id= peer_id)
    #commands
    if messagetext == '/comands':                                                      
        Text ="Play, play,играть, играть\nПривет привет \nначать Начать\nПока пока\nпогода Погода pogoda Pogoda\nПараметры для погоды:\n----------------------\nГород или страна англиискими буквами!\nqr Qr \nПараметры для qr:\n"
        TextMessage = Text+"----------------------\nСлово которое будет отображатьця при его сканирование!\npng Png\n\nПараметры для png\n----------------------\nВы можете написать png для рандомного png\nили png 1 или любое другое число для оприделёного png!\n 🎲 kubik,кости"
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
        Users(user_id = user_id,chat_id= peer_id) 
    #Start
    if messagetext == _COMMANDS[2] or messagetext == _COMMANDS[3] :
        TextMessage = "Выбери чтото {UserName} !".format(UserName=UserName(user_id))
        keyboard = open('start.json',"r",encoding="UTF-8").read()
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext,jsonKeyboard=keyboard)
    #mat
    if messagetext == 'ДА!' :
        TextMessage = "Выбери чтото {UserName} !".format(UserName=UserName(user_id))
        keyboard = open('keyboard_1.json',"r",encoding="UTF-8").read()
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext,jsonKeyboard=keyboard)
   
    if messagetext == '300' :
        TextMessage = "Отсоси у тракториста !".format(UserName=UserName(user_id))
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
    if re.search(r'Да!', messagetext) :
        TextMessage = "Пизда!".format(UserName=UserName(user_id))
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
    if re.search(r'Нет!', messagetext) :
        TextMessage = "Пидора ответ!".format(UserName=UserName(user_id))
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
    #mems
    if re.search(_COMMANDS[12], messagetext) or re.search(_COMMANDS[13], messagetext) :
        data= re.sub('png', "",messagetext)
        data= re.sub('Png', "",data)
        data= re.sub(' ', "",data)
        
        if data != '':
            mems = data
        else:
            mems = str(random.randint(1,149))
        
        attachment = SendPhotoMessage('pngmems/1 ('+mems+').png')
        # keyboard = open('mems.json',"r",encoding="UTF-8").read() 
        TextMessage = 'Мем №'+mems
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext,attachment=attachment)
    #kubik
    if re.search(_COMMANDS[14], messagetext) or re.search(_COMMANDS[15], messagetext) or re.search(_COMMANDS[16],messagetext) or  re.search(_COMMANDS[17],messagetext) or re.search(_COMMANDS[18],messagetext) or re.search(r'Бросить ещё раз!', messagetext) or re.search(r'🎲', messagetext):
        kubik(peer_id=peer_id,group_id=group_id,user_id=user_id,messagetext=messagetext)
    #mat   
    if re.search(r'сука', messagetext) or re.search(r'Сука', messagetext) or re.search(r'Хуй',messagetext) or  re.search(r'нахуй',messagetext) or re.search(r'Нахуй',messagetext):
        randomMessage = random.randint(1,3)
        if randomMessage == 1:
            TextMessage = " Сука ебаная не матерись!"
        if randomMessage == 2:
            TextMessage = "Сука не матерись!"
        if randomMessage == 3:
            TextMessage = "сука не матрерись 😡 !"
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
    #pogoda
    if re.search(_COMMANDS[6], messagetext) or re.search(_COMMANDS[7], messagetext) or re.search(_COMMANDS[8], messagetext) or re.search(_COMMANDS[9], messagetext):
        pogoda(peer_id=peer_id,group_id=group_id,user_id=user_id,messagetext=messagetext)
    #qr code
    if re.search(_COMMANDS[10],messagetext) or re.search(_COMMANDS[11],messagetext):
        randomName = config.RandomId()
        QrGenerate(randomName=randomName,peer_id=peer_id,group_id=group_id,user_id=user_id,messagetext=messagetext)
    #citate
    if messagetext == _COMMANDS_2[0] or messagetext == _COMMANDS_2[1] or messagetext == _COMMANDS_2[2]or messagetext == _COMMANDS_2[3]:
        reply_text = Message['object']['reply_message']['text']
        reply_user_name = UserName(Message['object']['reply_message']['from_id'])
        random_name = random.randint(1111,99999)
        random_citate = random.randint(0,2)
        if random_citate== 0:
            SteevJobsCitate(messagetext=messagetext,text_citate= reply_text,random_name=random_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
        if random_citate == 1:
            GoldCitate(messagetext = messagetext,text_citate= reply_text,random_name=random_name,user_name=reply_user_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
        if random_citate == 2:
            WhiteCitate(messagetext= messagetext,text_citate= reply_text,random_name=random_name,user_name=reply_user_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
    #Stev Jobs Citate
    if messagetext == _COMMANDS_2[4]:
        reply_text = Message['object']['reply_message']['text']
        reply_user_name = UserName(Message['object']['reply_message']['from_id'])
        random_name = random.randint(1111,99999)
        SteevJobsCitate(messagetext=messagetext,text_citate= reply_text,random_name=random_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
    #Gold Citate
    if messagetext == _COMMANDS_2[5]:
        reply_text = Message['object']['reply_message']['text']
        reply_user_name = UserName(Message['object']['reply_message']['from_id'])
        random_name = random.randint(1111,99999)
        GoldCitate(messagetext = messagetext,text_citate= reply_text,random_name=random_name,user_name=reply_user_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
    # White Citate
    if messagetext == _COMMANDS_2[6]:
        reply_text = Message['object']['reply_message']['text']
        reply_user_name = UserName(Message['object']['reply_message']['from_id'])
        random_name = random.randint(1111,99999)
        WhiteCitate(messagetext= messagetext,text_citate= reply_text,random_name=random_name,user_name=reply_user_name,group_id=config.grupid,peer_id=peer_id,user_id=user_id)
    #bot
    if re.search( _COMMANDS_2[7],messagetext) or re.search( _COMMANDS_2[8],messagetext) or re.search( _COMMANDS_2[9],messagetext) or re.search( _COMMANDS_2[10],messagetext) or re.search( _COMMANDS_2[11],messagetext):
        randomMessage = random.randint(1,8)
        def message(TextMessage):
            MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
        if randomMessage == 1:
            message("Я тут!")
        if randomMessage == 2:
            message("Чего тебе надо?")
        if randomMessage == 3:
            message("Чего тебе надо 😑?")
        if randomMessage == 4 or randomMessage == 8:
            message("😜")
        if randomMessage == 5:
            message("Я тут 😎")
        if randomMessage == 6:
            message( "Я на месте 😎")
        if randomMessage == 7:
            message("Я на месте")
        if user_id == 498475069:
            r = random.randint(1,2)
            if r == 2:
                TextMessageR = "Что тебе надо разроботчик 😎👑"
                MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage =TextMessageR,messagetext=messagetext)
        #play
    messagetext = re.sub('\[club187553500\|\@club187553500\] ','',messagetext)

    #play
    if  re.search( _COMMANDS_3[0],messagetext) or re.search( _COMMANDS_3[1],messagetext) or re.search( _COMMANDS_3[2],messagetext) or re.search( _COMMANDS_3[3],messagetext):
        jsonKeyboard = open('DroidALLIN/play.json', "r",encoding="UTF-8").read()
        photo = SendPhotoMessage('DroidALLIN/play.jpg')
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='Выберите деиствие!',messagetext=messagetext,jsonKeyboard=jsonKeyboard,attachment=photo)
    # Balance replisment
    print(messagetext)
    if messagetext == 'Пополнить счёт💵':
        jsonKeyboard = open('DroidALLIN/balans+.json', "r",encoding="UTF-8").read()
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='Выберите деиствие!',messagetext=messagetext,jsonKeyboard=jsonKeyboard)
    if messagetext == 'Пополнить на 10$':
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[0],BalanceReplismentSumm = 10)
    if messagetext == 'Пополнить на 20$':
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[0],BalanceReplismentSumm = 20)
    if messagetext == 'Пополнить на 50$':
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[0],BalanceReplismentSumm = 50)
    if messagetext == 'Пополнить на 100$':
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[0],BalanceReplismentSumm = 100)
    #buy case 10$
    if messagetext =='Купить кеис за 10$!🎰':
        jsonKeyboard = open('DroidALLIN/case10$.json', "r",encoding="UTF-8").read()
        TextMessage_1 = 'Соимость 10$\nВ кеисе есть:\n 1$\n2$\n5$\n10$\n20$\n25$\n50$\nCуперприз 100$\n'
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage_1,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
    #buy case 100$
    if messagetext =='Купить кеис за 100$!🎰':
        jsonKeyboard = open('DroidALLIN/case100$.json', "r",encoding="UTF-8").read()
        TextMessage_1 = 'Соимость 100$\nВ кеисе есть:\n 10$\n20$\n5$\n30$\n100$\n200$\n500$'
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage_1,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
    #buy case allin$
    if messagetext =='Купить кеис за 50$!🎰':
        jsonKeyboard = open('DroidALLIN/caseallin.json', "r",encoding="UTF-8").read()
        TextMessage_1 = 'Соимость 50$\nВ кеисе есть: 50% / 50%  вам может выпасть:\n 5$ и 100;'
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage_1,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
    #yes buy 10$
    if messagetext == 'Подтвердите покупку кейса за 10$!🎰':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[2])
    #yes buy 100$
    if messagetext =='Подтвердите покупку кейса за 100$!🎰':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[3])
     #yes buy 100$
    if messagetext =='Подтвердите покупку кейса за 50$!🎰':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[4])
    #return case 10$
    if messagetext =='Открыть ешщё раз кейс за 10$!':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[2])
    #return case 100$
    if messagetext =='Открыть ешщё раз кейс за 100$!':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[3])
    #return case 100$
    if messagetext =='Открыть ешщё раз кейс за 50$! 50%/50%':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[4])
    # -keuboard
    if messagetext =='Убрать клавиатуру!⌨':
        jsonKeyboard = open('DroidALLIN/null.json', "r",encoding="UTF-8").read()
        TextMessage = 'Напишьте play чтобы вернуть клавиатуру!'
        MessageSend(group_id=config.grupid,user_id=user_id,TextMessage =TextMessage,peer_id=peer_id,messagetext=messagetext,jsonKeyboard=jsonKeyboard)
    #blance
    if messagetext =='Баланс!💵':    
        DroidALLIN(group_id=config.grupid,user_id=user_id,peer_id=peer_id,messagetext=messagetext,Function=_Function_DroidALLIN[1])

    #version
    if messagetext == _COMMANDS_2[12]:
        MessageSend(peer_id= peer_id,group_id=group_id,user_id=user_id,TextMessage ='Version 0.1.2 BETA',messagetext=messagetext)
#Message send
def MessageSend(group_id,user_id,TextMessage,peer_id,messagetext,jsonKeyboard=None,attachment=None):
    parans={'access_token' : config.token,
            'group_id'     : config.grupid,
            'random_id'    : config.RandomId(),
            'peer_id'      : peer_id,
            'message'      : TextMessage,
            'keyboard'     : jsonKeyboard,
            'attachment'   : attachment,
            'v'            : '5.95'
            }
           
    _MessageSend = requests.get("https://api.vk.com/method/messages.send?", params=parans)
    DataBaseMessageSave(chat_id=peer_id,user_id=user_id,message_text=messagetext)
    print(_MessageSend.text)
#Message messages.getConversationMembers
def ConversationMembers(peer_id,user_id,messagetext):
    parans={'access_token' : config.token,
            'group_id' :  config.grupid,
            'peer_id'  : peer_id,
            'fields' :'id,first_name,last_name',
            'v'            : '5.95'
            }
           
    _ConversationMembers = requests.get("https://api.vk.com/method/messages.getConversationMembers", params=parans)
    print(_ConversationMembers.text)
    members = _ConversationMembers.json()
    count = members['response']['count']
    profiles= members['response']['profiles']
    indexrange = count
    i = -1 
    _profiles = '\n'
    for i in range(indexrange):
        try:
            num = i + 1 
            _profiles =  str(_profiles) + str(num) + ': ' +str(profiles[i]['first_name'])+' ' +str(profiles[i]['last_name'])+'\n'
        except:
            pass
    TextMessage = 'Участники беседы:' + _profiles
    MessageSend(peer_id= peer_id,group_id=config.grupid,user_id=user_id,TextMessage =TextMessage,messagetext=messagetext)
#Send photo
def SendPhotoMessage(PhotoUpload):
    params_1={'access_token' : config.token,   
                'v':'5.95'
                }
    #server link
    request_1= requests.get(url = 'https://api.vk.com/method/photos.getMessagesUploadServer?',params=params_1)
    res_1= request_1.json()
    upload_url=res_1['response']['upload_url'] 
    files = { 'photo' : open(PhotoUpload,'rb')}
    #upload photo
    #POST
    request_2 = requests.post(url=upload_url, files=files)
    res_2 =request_2.json()
    photo = res_2['photo']
    server = res_2['server']
    hashphoto = res_2['hash']
    params_2={
        'access_token' : config.token,
        'photo':photo,
        'server':server,
        'hash':hashphoto,
        'v':5.59
            }
    #save photo
    requests_3= requests.get(url = 'https://api.vk.com/method/photos.saveMessagesPhoto?',params=params_2)
    res_3 = requests_3.json()   
    print(res_3)
    owner_id = res_3['response'][0]['owner_id']
    object_id = res_3['response'][0]['id']
    photo= 'photo'+str(owner_id)+'_'+str(object_id)
    print(photo)
    return photo


#Main    
def main ():
    ServerRespons  = auth_server()
    key = ServerRespons ["response"]["key"]
    server = ServerRespons ["response"]["server"]
    ts = ServerRespons ["response"]["ts"]
    ServerCeckRespons = server_ceck(key,server,ts)
    print(ServerCeckRespons)
    a ={'ts': '668', 'updates': []}
    if ServerCeckRespons["updates"] == a['updates']:
        pass
    else:
        print (ServerCeckRespons["updates"][0]["group_id"])
        MessageCeck(ServerCeckRespons["updates"][0])

for ceck in range (10000000): 
    # try:
    #       main()
    # except:
    #     time.sleep(3)
        main()
        
        


