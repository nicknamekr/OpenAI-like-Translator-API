# OpenAI-like Translator API

## Introduction

OpenAI-like Translaator API. (You can use this service with OpenAI modules, too. Like Python, Javascript, Csharp...)<br>
Powered by Google Translator.

## Our API
URL : `https://1aa2c4d6-97a9-4cb3-a7ab-461c04c3eb2d.id.repl.co/chat/completions`<br>
BaseURL, BasePath for OPENai Model :<br>`https://1aa2c4d6-97a9-4cb3-a7ab-461c04c3eb2d.id.repl.co`<br>
Model for OpenAI Module (Chat Completions) :<br>
```js
Input 'SRC(FROM)-DEST(TO)' to your OpenAI code.
``` 
For example (Python):
```py
import openai

openai.api_key = "You_Don_t_Have_To_Enter_Anything_On_This_Var"
openai.api_base = "https://1aa2c4d6-97a9-4cb3-a7ab-461c04c3eb2d.id.repl.co"

response = openai.ChatCompletion.create(
    model= "en-ko",
    messages = [
        {"role": "user", "content": 'Hello, World!'},
    ]
)

print(response.choices[0].message.content) # 안녕, 세계!
```
   
## Your Own-Host API (ex. Fork)

### Get the token
1. Fork The Repl
2. RUN
### Run 
Click RUN button on your repl
