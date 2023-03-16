import discord
import gpt
import settings
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print("Ready!")

@client.event
async def on_message(message):
    #自分だったら無視
    if message.author == client.user:
        return

    #Botでも無視
    if message.author.bot:
        return

    #DMに返信
    if isinstance(message.channel, discord.DMChannel):
        print('DM was received')
        await message.channel.typing()
        await message.channel.send(gpt.generate_gpt_response(message.content))
        return

    #このBotがメンションされたら反応
    if message.content.startswith('<@1081838674154635316>'):
        print('Mention was received')
        await message.channel.typing()
        await message.channel.send(gpt.generate_gpt_response(message.content[23:]))
        return

client.run(settings.discord_token)
