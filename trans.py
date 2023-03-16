import os
import deepl
import settings

translator = deepl.Translator(settings.deepl_token)


def translate_to_japanese(text):
    result = translator.translate_text(text, target_lang="JA")
    return result


def translate_to_english(text):
    result = translator.translate_text(text, target_lang="EN-US")
    return result

# コードブロック以外を日本語に翻訳
def translate_code_to_japanese(text):
    result = ''
    l = text.split('```')
    for i, s in enumerate(l):
        if i % 2 == 0:
            result += str(translate_to_japanese(s))
        else:
            result += '```'
            result += s
            result += '```'
    return result
