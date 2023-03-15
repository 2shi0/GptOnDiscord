import os
import openai

import settings

# アクセスキーを読み込み
openai.api_key = settings.openai_key

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
        print(res)
        print('\nQuestion:')
        print(question)
        print('\nAnswer:')
        print(answer)
        print('\nSpending Token:')
        print(res["usage"])

        return answer

    except Exception as e:
        return "Error:"+e.message


# 使い方
# print(generate_gpt_response("あなたは誰ですか？"))
