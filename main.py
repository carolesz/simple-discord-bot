import discord
import asyncio
import random
import os
cliente_discord = discord.Client()

@cliente_discord.event
async def on_ready():
    print('Bot ONLINE')

@cliente_discord.event
async def on_message(texto):
    if (str(texto.author.id) == 'BOT_ID'): return
    if texto.content.lower().startswith('YOUR PREFIX'): #Se a mensagem tiver o prefixo desejado ele passará a executar
        frase = texto.content[len(texto.content):].strip() #Tira o prefixo da frase
        if frase.lower().startswith('d6'): # prefix d6
            numr = random.randint(1,6) # "roda o dado"
            await texto.channel.send(str(numr)) # mostra o numero que caiu no chat do discord
            return

cliente_discord.run('your bot secret token')
