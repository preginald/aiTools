import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

initial = 'Tell me a choose your own adventure story. Give me multiple choices. Start the story and ask the first question.'

message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

# conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]
conversation = [{"role": "system", "content": initial}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)
