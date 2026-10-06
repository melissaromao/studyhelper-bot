import discord
from bot_logic import gen_pass

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')
    elif message.content.startswith('$bye'):
        await message.channel.send('\\U0001f642')
    else:
        await message.channel.send('Sua senha: ' + gen_pass(10))

client.run("TOKEN")