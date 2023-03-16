import openai
import os
import trans
import settings

# アクセスキーを読み込み
openai.api_key = settings.openai_token

def generate_gpt_response(question):
    try:
        f = open('prompt.txt', 'r')
        prompt = f.read()
        f.close()
    except FileNotFoundError:
        prompt = ''

    try:
        # 入力文を英語に翻訳
        translated_question=str(trans.translate_to_english(question))

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": translated_question
                },
            ],
        )
        answer = res["choices"][0]["message"]["content"]

        translated_answer=str(trans.translate_to_japanese(answer))
        
        #print(res)
        print('Question           : '+question)
        print('Translated Question: '+translated_question)
        print('Translated Answer  : '+translated_answer)
        print('Answer             : '+answer)
        print('Spending Token     : '+str(res["usage"]["total_tokens"]))

        return translated_answer

    except:
        return 'にゃーん（エラー）'


# 使い方
# print(generate_gpt_response("あなたは誰ですか？"))