from ollama import Client, chat, ChatResponse

# https://github.com/ollama/ollama-python
# python -m venv .venv (vscode ask if you want to use)
# .venv/bin/pip install ollama
# then run with
# .venv/bin/python ollama_test.py

# custom client to programatically change localhost 
client: Client = Client(
  host='http://host.docker.internal:11434'
)
# use client to invoke chat
# response: ChatResponse = client.chat(model='llama3.2', messages=[

# OR

# use environment variable OLLAMA_HOST to set the host url with chat directly
response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
],
)
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)