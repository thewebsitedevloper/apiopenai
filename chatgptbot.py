import openai

# Initialize the API key
openai.api_key = "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"

# Define a prompt for the model
prompt = "how to be a rich man? "

# Generate a response from the model
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
).choices[0].text

print(response)
