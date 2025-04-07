from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import os

glove_input_file = "glove.6B.100d.txt"
word2vec_output_file = "glove.6B.100d.word2vec.txt"

if not os.path.exists(word2vec_output_file):
    glove2word2vec(glove_input_file, word2vec_output_file)

model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)

word = "king"
if word in model:
    print(f"Vector for '{word}':\n{model[word]}")

print("\nTop 5 similar words to 'king':")
print(model.most_similar("king", topn=5))

result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
print(f"\n'king' - 'man' + 'woman' = '{result[0][0]}'")
          