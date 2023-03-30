import gzip
import base64

# Define the input prompt string
prompt = "This is an example prompt that we want to compress using gzip."

# Compress the input prompt using gzip
compressed_prompt = gzip.compress(prompt.encode())

# Encode the compressed prompt as a Base64 string
encoded_prompt = base64.b64encode(compressed_prompt).decode()

# Format the output string that can be copied and pasted into ChatGPT
output_str = f"compressed:{encoded_prompt}"

# Print the output string
print(output_str)
