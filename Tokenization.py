# import tiktoken

# encoder = tiktoken.encoding_for_model('gpt-4o')

# print("Vocab size", encoder.n_vocab) #(200k)

# text = "Cats are running"
# tokens = encoder.encode(text)

# print("Tokens", tokens) # Tokens [126947, 553, 6788]

# my_tokens = [126947, 553, 6788]
# decoder = encoder.decode(my_tokens)

# print("Decoded", decoder)





# import tiktoken

# encoder = tiktoken.encoding_for_model('gpt-4o')

# print("Vocab Size", encoder.n_vocab)

# text = "What are you doing"

# tokens = encoder.encode(text)

# print("Tokens", tokens)

# Decoder = encoder.decode(tokens)

# print("Decoded", Decoder)


import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab)

text = "My name is Priyabrata"

print(encoder.encode(text))

print(encoder.decode(encoder.encode(text)))
