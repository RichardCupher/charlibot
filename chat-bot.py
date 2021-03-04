#я чарли
import discord
from discord.utils import get
import random
import os
import youtube_dl
yrlll = 'https://youtu.be/F4wIbPq6euM'
smd = ''
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
def smds():
    smd = ''
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
        if 'leave' in regt == False or 'join' in regt == False:
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
        if msg != '':
            await message.channel.send(msg)
    else:
        global voice
        if 'join' in regt:
            channel = message.author.voice.channel
            voice = get(client.voice_clients, guild = message.guild)
            print('444555')
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
                await message.channel.send(f'Чарли присоединился к каналу: {channel}')
        if 'leave' in regt:
            channel = message.author.voice.channel
            voice = get(client.voice_clients,guild = message.guild)
            if voice and voice.is_connected():
                await voice.disconnect()
                await message.channel.send(f'Чарли отключился от канала: {channel}')
        if 'play' in regt:
            song_there = os.path.isfile('song.mp3')
            try:
                if song_there:
                    os.remove('song.mp3')
                    print('[log] Старый фаил удалён')
            except PermissionError:
                print('[log] не удалось удалить фаил')

            await message.channel.send('Пожалуйста ожидайте')
            voice = get(client.voice_clients, guild = message.guild)
            print(voice)
            ydl_opts = {
                'format' : 'bestaudio/best',
                'postprocessors' : [{
                        'key' : 'FFmpegExtractAudio',
                        'preferredcodec' : 'mp3',
                        'preferredquality' : '192'
                    }]
                }
            with youtube_dl.YoutubeDL({}) as ydl:
                print('[log] Загружаем музыку...')
                ydl.download([yrlll])
            for file in os.listdir('./'):
                print(file)
                if file.endswith('.mp4') or file.endswith('.webm')or file.endswith('.mkv') :
                    namemp3 = file
                    print(f'[log] переименовываю фаил: {file}')
                    os.rename(file, 'song.mp3')
                    print(file)
                    
            voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {namemp3}, музыка закончила своё проигрывание'))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            vi=voice.source.volume = 0.07
            song_name = namemp3.rsplit('-', 2)
            await message.channel.send(f'Сейчас играет: {song_name[0]}')
    msg = ''
    namer = ''
token = os.environ.get('tokencharli')
client.run(str(token))
