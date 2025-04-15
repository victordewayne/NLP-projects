import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense
import re

# Load data
input_texts = []
target_texts = []

with open(r"C:\Users\victor\Desktop\Project Omega\NLP specialist\Projects\Simple_projects\sample_data.txt", "r", encoding="utf-8") as f:
    lines = f.read().split('\n')

for line in lines:
    if '\t' in line:
        input_text, target_text = line.split('\t')
        # Add <start> and <end> tokens to target
        target_text = '\t' + target_text + '\n'
        input_texts.append(input_text.lower())
        target_texts.append(target_text.lower())

# Create vocabulary
input_chars = set(''.join(input_texts))
target_chars = set(''.join(target_texts))
input_chars = sorted(list(input_chars))
target_chars = sorted(list(target_chars))

input_token_index = {char: i for i, char in enumerate(input_chars)}
target_token_index = {char: i for i, char in enumerate(target_chars)}
reverse_target_char_index = {i: char for char, i in target_token_index.items()}

max_encoder_seq_length = max(len(txt) for txt in input_texts)
max_decoder_seq_length = max(len(txt) for txt in target_texts)
num_encoder_tokens = len(input_chars)
num_decoder_tokens = len(target_chars)

# Vectorize input and target
encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, num_encoder_tokens), dtype='float32')
decoder_input_data = np.zeros((len(input_texts), max_decoder_seq_length, num_decoder_tokens), dtype='float32')
decoder_target_data = np.zeros((len(input_texts), max_decoder_seq_length, num_decoder_tokens), dtype='float32')

for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
    for t, char in enumerate(input_text):
        encoder_input_data[i, t, input_token_index[char]] = 1.0
    for t, char in enumerate(target_text):
        decoder_input_data[i, t, target_token_index[char]] = 1.0
        if t > 0:
            decoder_target_data[i, t - 1, target_token_index[char]] = 1.0

# Define encoder
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder_lstm = LSTM(256, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

# Define decoder
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=16, epochs=300, verbose=1)

# Inference setup
encoder_model = Model(encoder_inputs, encoder_states)

decoder_state_input_h = Input(shape=(256,))
decoder_state_input_c = Input(shape=(256,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_outputs, state_h, state_c = decoder_lstm(
    decoder_inputs, initial_state=decoder_states_inputs
)
decoder_states = [state_h, state_c]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states
)

def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, target_token_index['\t']] = 1.0

    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value
        )

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        if sampled_char == '\n' or len(decoded_sentence) > max_decoder_seq_length:
            break

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.0
        states_value = [h, c]

    return decoded_sentence.strip()

def preprocess_input(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z? ]", "", text)
    return text

# Chat loop
print("Chatbot is ready! Type 'exit' to quit.")
while True:
    input_text = input("You: ")
    if input_text.lower() == 'exit':
        print("🤖 Chatbot: Goodbye!")
        break
    input_text = preprocess_input(input_text)
    encoder_input = np.zeros((1, max_encoder_seq_length, num_encoder_tokens), dtype='float32')
    for t, char in enumerate(input_text):
        if char in input_token_index:
            encoder_input[0, t, input_token_index[char]] = 1.0
    decoded_response = decode_sequence(encoder_input)
    print("Chatbot:", decoded_response)
