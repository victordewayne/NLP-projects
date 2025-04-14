from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load pretrained T5 model
model_name = "t5-small"  # You can try 't5-base' for better results
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Context and Question
context = """
The Mona Lisa is a half-length portrait painting by Italian artist Leonardo da Vinci. 
It is considered an archetypal masterpiece of the Italian Renaissance, and has been described 
as "the best known, the most visited, the most written about, the most sung about, the most parodied work of art in the world."
"""

question = "Who painted the Mona Lisa?"

# T5 expects a prompt like this:
input_text = f"question: {question}  context: {context}"

# Tokenize input and generate answer
inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
outputs = model.generate(inputs, max_length=50, num_beams=4, early_stopping=True)

# Decode the answer
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Question:", question)
print("Answer:", answer)
