# from deep_translator import GoogleTranslator
# from pykakasi import kakasi
# # pip install Cython
# # pip install pykakasi


# # 要翻译的日语句子
# japanese_text = "こんなに幸せで良いんだろうかってか?"

# # 使用GoogleTranslator模块将日语翻译为英语
# english_text = GoogleTranslator(source='ja', target='en').translate(japanese_text)

# # 使用pykakasi库将日语文本转换为罗马音
# kakasi = kakasi()
# kakasi.setMode("J", "H") # 设置转换模式
# kakasi.setMode("K", "H") # 设置转换模式
# conv = kakasi.getConverter()
# romaji_text = conv.do(japanese_text)

# # 打印英语翻译和罗马音转换结果
# print("英语翻译: ", english_text)
# print("罗马音: ", romaji_text)


import pykakasi
kks = pykakasi.kakasi()
# text = "かな漢字"
text = "こんなに幸せで良いんだろうかってか?"
result = kks.convert(text)
sentence = ""
for item in result:
    word = item['orig']+"(%s)"%item['hira'] if not item['orig']==  item['hira'] else item['orig']
    sentence+=word
print(sentence)
