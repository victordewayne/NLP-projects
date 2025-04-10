from transformers import GPT2LMHeadModel, GPT2Tokenizer 
import torch


model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


prompt = "What’s the weather like in Tokyo?"


inputs = tokenizer.encode(prompt, return_tensors='pt')
outputs = model.generate(inputs, max_length=50, num_return_sequences=1, do_sample=True)


generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)