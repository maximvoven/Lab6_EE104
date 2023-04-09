import os
import openai #remember to pip install pandas openai

#Sign up for OpenAI here https://beta.openai.com/signup
# and obtain an API key from here https://platform.openai.com/account/api-keys
#Replace the OPEN_API_KEY below with your own key:
openai.api_key = "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"

#If you are using Anaconda Spyder, make sure it is updated to version 5.3.3
# or later
# from the Anaconda prompt, type 2 commands
#  conda update anaconda
#  conda install spyder=5.3.3

def generate_response(prompt, max_tokens=2048,n=1,temperature=1):
    # More details about the different engines here
    #  https://beta.openai.com/docs/models/gpt-3
    model_engine = "text-davinci-003"  # https://platform.openai.com/docs/models/overview
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )

    message = completions.choices[0].text
    return message.strip()
prompt = "King Henery Died by Drinking Chocolate Milk"
print(generate_response(prompt, max_tokens=2048,n=1,temperature=1))
print(generate_response(prompt, max_tokens=2048,n=1,temperature=10))
print(generate_response(prompt, max_tokens=2048,n=3,temperature=1))
print(generate_response(prompt, max_tokens=10,n=1,temperature=1))