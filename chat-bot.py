#я чарли
import discord
import random
import os
import gorodaspisok
goroda = gorodaspisok.goroda
gorodar = ''
game = 0
regt = ''
namer=''
msg = ''
g = '$'
priv = ['ку','привет','хай','здарова','добрый день','добрый вечер','доброе утро','hi','hello']
privOtv = ['Привет','хай','Здарова','Здравствуй','Hello','Hi']
nastroi = ['как дела','как ты','как успехи','как оно']
nastroiOtv = ['По тихоньку','Да пойдёт','Ну живём пока что','Норм','Всё ок']
client = discord.Client()
@client.event
async def on_ready():
    print('Connected {0.user}'.format(client))
def redactname(nameret):
    global namer
    for i in nameret:
         if i == '#':
             break
         namer = namer + i
    return namer + ': '
def otv(sms1, otvet):
    for q in otvet:
        if q in sms1:
            return True
def gorod(e,z):
    global gorodar
    global g
    global h
    for f in e:
        if f == 'ь' or f == 'ъ' or f == 'й':
            break
        gorodar = f
    if e[-1] == 'й':
        e.replace('й','')
    if e[-1] == 'ь':
        e.replace('ь','')
    if e[-1] == 'ъ':
        e.replace('ъ','')
    for u in z:
        g = random.choice(goroda)
        h = str.lower(g)
        if e[-1] == h[:1]:
            return g
        
def gtr(v,d):
    global g
    if g[-1] == 'й':
        g.replace('й','')
    if g[-1] == 'ь':
        g.replace('ь','')
    if g[-1] == 'ъ':
        g.replace('ъ','')
    if g[-1] == v[:1] or g == '$':
        for t in d:
            th = str.lower(t)
            if v == th:
                return True
        return False
@client.event
async def on_message(message):
    regt = str.lower(message.content)
    sms = regt.replace('.', '').split()
    global name
    global goroda
    global msg
    global namer
    global game
    if message.author == client.user:
        return
    if 'чарли' in regt:
        msg = msg + redactname(str(message.author)) + ' '
        if otv(regt, priv):
            msg = msg + random.choice(privOtv) + '. '
        if 'кто ты' in regt:
            msg = msg + 'я чат-бот' + '. '
        if 'кто тебя создал' in regt:
            msg = msg + 'Меня создал "Richard Cupher"' + '. '
        if otv(regt, nastroi):
            msg = msg + random.choice(nastroiOtv) + '. '
        if 'что ты умеешь' in regt:
            msg = msg + 'Я умею Общаться и играть в города' + '. '
        if 'как начать играть' in regt:
            msg = msg + 'Напиши мне: давай поиграем \n Чтобы закончить игру напиши: Спасибо за игру' + '. '
        if 'ты лучший' in regt:
            msg = msg + 'Спасибо)))' + '. '
        if 'пзц' in regt:
            msg = msg + 'Согласен' + '. '
        if 'давай поиграем' in regt and game == 0:
            msg = msg + 'давай ты начинаешь' + '. '
            game = 1
            g = '$'
        if 'спасибо за игру' in regt:
            msg = msg + 'Ну ладно(' + '. '
            game = 0
            g = '$'
        if not msg == '':
            await message.channel.send(msg)
    elif game == 1:
        if gtr(regt,goroda):
            msg = gorod(regt,goroda)
            await message.channel.send(msg)
        else:
            await message.channel.send('Я не нашёл такой город, Попробуй ещё раз')
    msg = ''
    namer = ''
token = os.environ.get('tokencharli')
client.run(str(token))
