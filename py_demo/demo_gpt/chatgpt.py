import openai #  pip install openai
import json

openai.api_key = "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"

def translate(text, target_language):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate '{text}' to {target_language}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    if response.choices[0].text:
        return response.choices[0].text
    else:
        return None

    

text = "Hello, how are you?"
target_language = "zh"

translation = translate(text, target_language)
print(f"Translation: {translation}")
