import os
import requests
import numpy as np
import openai
import matplotlib.pyplot as plt
from scipy.stats import binom_test

prompt = "The most popular color is red."
# Set desired level of significance
alpha = 0.05

# Set up API credentials and endpoint
with open("openai.key", "r") as f:
    api_key = f.read().strip()
openai.api_key = api_key

# Calculate necessary sample size
#n = int(np.ceil((2 * power * (1 - p_expected)) / margin_of_error**2))
n = 40

# Collect sample of responses
# https://platform.openai.com/docs/guides/chat/introduction
responses = []
for i in range(n):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant. Please give the response as either True, False only and followed by a period."},
                {"role": "user", "content": prompt},
            ]
        )
    response_text = response["choices"][0]["message"]["content"]
    responses.append(response_text.split(' ')[0])
    print(f"The model responded ({i + 1}/{n}): {response_text}")

# Calculate number of "True" and "False" responses
n_true = responses.count("True.")
n_false = responses.count("False.")
n_other = n - (n_true + n_false)

# Calculate p-value using binomial test
p_value = binom_test(n_true, n_true + n_false, p=0.5)
print(f"p-value: {p_value}")

# Determine if p-value is less than alpha and draw conclusion
if p_value < alpha:
    print("There is evidence to suggest that the proportion of 'True' responses is significantly different from 0.5.")
else:
    print("There is not enough evidence to suggest that either response is significant.")

# Create bar chart of responses
labels = ["True", "False", "Other"]
values = [n_true, n_false, n - (n_true+n_false)]
plt.bar(labels, values)
plt.title(f"Responses to '{prompt}'")
plt.xlabel("Response")
plt.ylabel("Frequency")
plt.savefig(f"{prompt}.png", dpi=300)  # Save plot as PNG file with high resolution
plt.show()