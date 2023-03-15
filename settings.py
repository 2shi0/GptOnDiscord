import os
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数にToken等を入力
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

discord_token = os.environ.get('DISCORD_TOKEN')
openai_key = os.environ.get('OPENAI_KEY')
