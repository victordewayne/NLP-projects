from transformers import BertTokenizer, BertModel
import torch

tokenizer =BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

sentence = "Natural Language Processing is amazing. "

inputs =tokenizer(sentence, return_tensors='pt')

with torch.no_grad():
    outputs = model(**inputs)


last_hidden_state = outputs.last_hidden_state

for token, vector in zip(tokenizer.tokenize(sentence), last_hidden_state[0]):
    print(f"Token: {token}\nVector: {vector[:5]}...")
    print()
