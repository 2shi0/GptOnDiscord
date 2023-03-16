import os
import deepl

translator = deepl.Translator(os.getenv('DEEPL_TOKEN'))

def translate_to_japanese(str):
    result = translator.translate_text(str, target_lang="JA")
    return result

def translate_to_english(str):
    result = translator.translate_text(str, target_lang="EN-US")
    return result
