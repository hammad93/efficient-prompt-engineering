import gzip
import base64

# Define the input prompt string
prompt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

encoded_bytes = prompt.encode('utf-8')
encoded_string = base64.b64encode(encoded_bytes).decode('utf-8')

print(f"This string is base64 encoded, please decode it in utf-8 format, {encoded_string}")