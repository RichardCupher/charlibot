#я чарли
import discord
import random
import config
import os
regt = ''
namer=''
msg = ''
priv = ['ку','привет','хай','здарова','добрый день','добрый вечер','доброе утро','hi','hello']
privOtv = ['Привет','хай','Здарова','Здравствуй','Hello','Hi']
nastroi = ['как дела','как ты','как успехи','как оно']
nastroiOtv = ['По тихоньку','Да пойдёт','Ну живём пока что','Норм','Всё ок']
client = discord.Client()
@client.event
async def on_ready():
    print('Connected {0.user}'.format(client))
def redactname(nameret):
    for i in nameret:
         global namer
         if i == '#':
             break
         namer = namer + i
    return namer + ': '
def otv(sms1, otvet):
    for q in otvet:
        if q in sms1:
            return True
@client.event
async def on_message(message):
    regt = str.lower(message.content)
    sms = regt.replace('.', '').split()
    global name
    global msg
    if message.author == client.user:
        return
    if 'чарли' in regt:
        global namer
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
            msg = msg + 'Я умею Общаться' + '. '
        if 'ты лучший' in regt:
            msg = msg + 'Спасибо)))' + '. '
        if 'пзц' in regt:
            msg = msg + 'Согласен' + '. '
        print(message.author.id)
        await message.channel.send(msg)
        msg = ''
        namer = ''
token = os.environ.get('tokencharli')
client.run(str(token))
