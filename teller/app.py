
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
from flask_cors import CORS

import json

#os.environ['OPENAI_API_KEY'] = open(".openai").read().strip()

# Setup llamaindex here



# From here is Flask

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return redirect("/static/index.html", code=302)

@app.route('/chat')
def chat():
    return redirect("/static/chat/index.html", code=302)




@app.route('/postQuestion',  methods=['POST'])
def postQuestion():
    question = request.form['q']
    #completion = query_engine.query(question)
    completion = "Ok, got it, this is you question:" + question
    return f"{completion}"

# route with openAI syntax
@app.route('/v1/chat/completions',  methods=['POST'])
def completions():
    payload = request.json
    #print(f"payload: {payload}")
    question = payload["messages"][0]["content"]
    print(question)

    #answer = query_engine.query(question)
    answer = "Ok, got it, this is you question: " + question
    print("** ANSWER **")
    print(answer)

    # Creazione del JSON
    data = {
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": str(answer)
                }
            }
        ]
    }


    return json.dumps(data)

"""
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "ciao"
    }
  ],
  "max_tokens": 2048,
  "temperature": 0.2,
  "n": 1,
  "stop": null
}

response.choices[0].message.content.trim();
"""