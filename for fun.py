import openai
openai.api_key = "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"

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="text-davinci-003", prompt="how can i teach better?")

# print the completion
print(completion.choices[0].text)