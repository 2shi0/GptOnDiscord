import os
import deepl
import settings

translator = deepl.Translator(settings.deepl_token)

def translate_to_japanese(str):
    result = translator.translate_text(str, target_lang="JA")
    return result

def translate_to_english(str):
    result = translator.translate_text(str, target_lang="EN-US")
    return result
