from deep_translator import GoogleTranslator # pip install deep-translator

text = "こんにちは" # Japanese string
translated = GoogleTranslator(source='ja', target='zh-CN').translate(text=text) # Chinese translation
print(translated) # prints 你好