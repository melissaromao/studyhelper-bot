import discord
from bot_logic import estudos_temas, temas

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')
    
@client.event
async def on_message(message):
    def check(mensagem):
        return mensagem.author == message.author and mensagem.channel == message.channel
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')
    elif message.content.startswith('$bye'):
        await message.channel.send('\\U0001f642')
    elif message.content.startswith('$tema'):
        await message.channel.send('Qual é o nome do tema?')
        resposta = await client.wait_for('message', check=check)
        tema = resposta.content
        await message.channel.send('Qual é o status atual (em andamento/concluído/pendente?)')
        resposta = await client.wait_for('message', check=check)
        status = resposta.content
        await message.channel.send('Sobre o que é o conteúdo?')
        resposta = await client.wait_for('message', check=check)
        conteudo = resposta.content
        estudos_temas(tema, status, conteudo)
        await message.channel.send(
            f'## ✅ Tema registrado com sucesso!\n\n'
            f'> 📚 **{tema}**\n'
            f'> 🔍 **Status:** {status}\n'
            f'> ℹ️ **Conteúdo:** {conteudo}'
            )
    elif message.content.startswith('$meustemas'):
        if not temas:
            await message.channel.send('Nenhum tema registrado.')
        else:
            mensagem = '## 📚 Temas Registrados\n\n'
            for tema, info in temas.items():
                mensagem += (
                    f'> 📚 **{tema}**\n'
                    f'> 🔍 **Status:** {info["status"]}\n'
                    f'> ℹ️ **Conteúdo:** {info["conteudo"]}\n\n'
                )
            await message.channel.send(mensagem)
client.run("TOKEN")