import tiktoken

# get gpt2 BPE 
tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces "
     "of someunknownPlace."
)

encode_rst = tokenizer.encode(text, allowed_special={'<|endoftext|>'})
print(encode_rst)

print(tokenizer.decode(encode_rst))