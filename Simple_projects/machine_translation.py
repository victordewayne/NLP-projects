from transformers import MarianMTModel, MarianTokenizer


src_text = ["Good morning!"]

model_name = 'Helsinki-NLP/opus-mt-en-de'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

tokens = tokenizer(src_text, return_tensors="pt", padding=True)

translated = model.generate(**tokens)
output = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

print("Input:", src_text[0])
print("Translated:", output[0])
