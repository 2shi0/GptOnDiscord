import openai

#アクセスキーを読み込み
try:
  f=open('openai_api.key','r')
  openai.api_key=f.read().replace('\n', '')
  print(openai.api_key)
  f.close()
except FileNotFoundError:
  print('token.key was not exist.')
  exit()

def generate_gpt_response(question):
  try:
    f=open('prompt.txt','r')
    prompt=f.read()
    f.close()
  except FileNotFoundError:
    prompt=''

  try:
    res = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
         messages=[
             {
                 "role": "system",
                 "content": prompt
             },
             {
                 "role": "user",
                 "content": question
             },
         ],
    )
    print("-----------------")
    #print(res["usage"])
    print('Injected prompt:')
    print(prompt)
    #print(res)
    return res["choices"][0]["message"]["content"]

  except:
    return "予算を使い切ったため、gpt-3.5-turboからレスポンスが帰ってきませんでした。<@830791139179102239> に問い合わせてください。"


#使い方
#print(generate_gpt_response("あなたは誰ですか？"))
