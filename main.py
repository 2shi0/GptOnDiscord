import discord
import gpt
import trans
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
        result = gpt.generate_gpt_response(message.content)
        await message.channel.send(result)
        return

client.run(settings.discord_token)
