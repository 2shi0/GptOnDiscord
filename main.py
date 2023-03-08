import discord
import ai

#アクセストークンを読み込み
try:
  f=open('doscord_token.key','r')
  token=f.read()
  f.close()
except FileNotFoundError:
  print('token.key was not exist.')
  exit()

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
        answer=ai.generate_gpt_response(message.content)
        await message.channel.send(answer)
        return

    #このBotがメンションされたら反応
    if message.content.startswith('<@1081838674154635316>'):
        print('Mention was received')
        await message.channel.typing()
        question=message.content[22:]

        answer=ai.generate_gpt_response(question)
        await message.channel.send(answer)

client.run(token)
