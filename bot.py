# https://discord.com/developers/applications/814711708026929193/information

import discord
import os
import random
from datetime import datetime
from datetime import date
client = discord.Client()
random.seed(datetime.now())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        rollHelp = '__**$roll [n]**__\nRolls a dice! Replace [n] with a number to roll an n-sided die, otherwise defaults to 6.\n'
        factHelp = '__**$fact**__\nSpits out a random fact.\n'
        rpsHelp = '__**$rps [action]**__\nPlay Rock Paper Scissors! Replace [action] with either rock, paper or scissors.\n'
        pokemonHelp = '__**$pokemon**__\nShows a countdown for the Pokemon remakes.\n'
        uwuHelp = '__**$uwu**__\nReturns a random uwu image.\n'
        copypastaHelp = '__**$copypasta**__\nI dont need to describe this one.\n'
        await message.channel.send(rollHelp + factHelp + rpsHelp + pokemonHelp + uwuHelp + copypastaHelp)

    if message.content.startswith('$roll'):
        arr = str.split(message.content)
        if len(arr) > 1:
            n = int(arr[1])
        else:
            n = 6
        value = random.randint(1,n)
        random.seed(datetime.now())
        await message.channel.send('The dice has rolled a ' + str(value) + '.')

    if message.content.startswith('$fact'):
        filename = 'facts.txt'
        with open(filename) as f:
            content = f.readlines()
        output = content[random.randint(0,len(content)-1)]
        random.seed(datetime.now())
        await message.channel.send(output)

    if message.content.startswith('$rps'):
        arr = str.split(message.content)
        rps = ['ROCK', 'PAPER', 'SCISSORS']
        userAction = arr[1].upper()
        botAction = random.choice(rps)
        win = False
        if userAction == botAction:
            await message.channel.send('You both used ' + botAction + ', its a tie!')
        elif userAction == 'ROCK':
            if botAction == 'PAPER':
                win = False
            elif botAction == 'SCISSORS':
                win = True
        elif userAction == 'PAPER':
            if botAction == 'ROCK':
                win = True
            if botAction == 'SCISSORS':
                win = False
        elif userAction == 'SCISSORS':
            if botAction == 'ROCK':
                win = False
            if botAction == 'PAPER':
                win = True
        if win == True and userAction != botAction:
            await message.channel.send('You used ' + userAction + ' and the bot used ' + botAction +  '. You win!')
        elif win == False and userAction != botAction:
            await message.channel.send('You used ' + userAction + ' and the bot used ' + botAction +  '. You lose...')

    if message.content.startswith('$pokemon'):
        present = datetime.now()
        release = datetime(2021, 12, 1)
        countdown = release - present
        await message.channel.send(str(countdown.days) + ' days till Pokemon Brilliant Diamond and Shining Pearl.')

    if message.content.startswith('$uwu'):
        imageList = os.listdir("Images")
        randImage = imageList[random.randint(0,len(imageList)-1)]
        print(randImage)
        await message.channel.send(file=discord.File("Images/"+randImage))
    

    if message.content.startswith('$copypasta'):
        filename = 'copypasta.txt'
        with open(filename) as f:
            copypasta = f.readlines()
        await message.channel.send(copypasta[0])


client.run('ODE0NzExNzA4MDI2OTI5MTkz.YDh1Zw.VMZwZOoSAjNn5FZDPIftpASBttA')