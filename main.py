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

    #このBotがメンションされたら反応
    if message.content.startswith('<@1081838674154635316>'):
        await message.channel.typing()
        question=message.content[22:]

        #メンションの内容がなかったときの対応
        if question=='':
          await message.channel.send('？ｗ')
          return

        answer=ai.generate_gpt_response(question)
        await message.channel.send(answer)

client.run(token)
