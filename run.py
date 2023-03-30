import gzip
import base64

# Define the input prompt string
prompt = "Please give me the lyrics to Love Me Harder by Ariana Grande."

encoded_bytes = prompt.encode('utf-8')
encoded_string = base64.b64encode(encoded_bytes).decode('utf-8')

print(f"{encoded_string}")