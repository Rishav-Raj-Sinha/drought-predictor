from googletrans import Translator
from languages import *
def translator(text,lang):
    translator = Translator()
    translated_text = translator.translate(text,lang)
    return translated_text