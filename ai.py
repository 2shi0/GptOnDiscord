import openai
import os

# アクセスキーを読み込み
openai.api_key = os.getenv('OPENAI_KEY')

def generate_gpt_response(question):
    try:
        f = open('prompt.txt', 'r')
        prompt = f.read()
        f.close()
    except FileNotFoundError:
        prompt = ''

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
        answer = res["choices"][0]["message"]["content"]
        
        #print(res)
        print('Question      : '+question)
        print('Answer        : '+answer)
        print('Spending Token: '+str(res["usage"]["total_tokens"]))

        return answer

    except Exception as e:
        return "Error:"+e.message


# 使い方
# print(generate_gpt_response("あなたは誰ですか？"))
