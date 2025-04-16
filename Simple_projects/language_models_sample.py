from transformers import GPT2LMHeadModel, GPT2Tokenizer 
import torch 

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

prompt = "Artificial Intelligence will"
inputs = tokenizer.encode(prompt, return_tensors='pt')

outputs = model.generate(inputs, max_length=50, do_sample=True, top_k=50)

print("Generated Text:\n", tokenizer.decode(outputs[0], skip_special_tokens=True))