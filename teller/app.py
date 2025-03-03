
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
from flask_cors import CORS

import json, os, sys

# Ottieni il percorso assoluto della directory superiore
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print("parent dir",parent_dir)
print("sys.path", sys.path)


# FOO is just to make sure imports work
from utils import send_message, check_run, get_messages, create_a_thread




# load the thread from the assistant
thread_id = create_a_thread()
print("thread_id",thread_id)

# From here is Flask

app = Flask(__name__)
CORS(app)




@app.route('/')
def chat():
    return redirect("/static/chat/index.html", code=302)






# route with openAI syntax
@app.route('/v1/chat/send',  methods=['POST'])
def sendQuestion():
    payload = request.json
    #print(f"payload: {payload}")
    question = payload["messages"][0]["content"]
    print("question",question)

    #answer = query_engine.query(question)
    answer = "Ok, got it, this is you question: " + question
    

    run_id = send_message(question, thread_id)
    print("run_id",run_id)

    print("** ANSWER **", answer)

    return json.dumps({"run_id": run_id})



# route with openAI syntax
@app.route('/v1/chat/receive',  methods=['POST'])
def receiveAnswer():
    # Creazione del JSON
    payload = request.json
    print(f"payload: {payload}")
    run_id = payload["run_id"]
    print("run_id",run_id)
    status = check_run(run_id, thread_id)
    print("status",status)
    if status == 'completed':
        messages = get_messages(run_id, thread_id)
        print("messages",messages)
        answer = messages[-1][1]
    else:
        answer = "I'm still thinking about it, please wait a moment"

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

