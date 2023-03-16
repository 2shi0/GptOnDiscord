# GptOnDiscord
ChatGPTは英語のほうが回答の精度がいいらしい…せや！

Discord上で話しかけると、質問をDeepLで翻訳してChatGPTに投げ、返ってきた英文を翻訳した日本語を返信します。

# 設定方法
.envファイルを作成し、
```
DISCORD_TOKEN=''
OPENAI_TOKEN=''
DEEPL_TOKEN=''
```
各種トークンを入力してからmain.pyを実行すれば動きます（多分）