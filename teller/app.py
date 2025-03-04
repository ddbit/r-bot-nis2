
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect
from flask_cors import CORS

import json
import helpers

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




@app.route('/sendMessage',  methods=['POST'])
def sendMessageToAssistant():
    question = request.form['q']
    print('question', question)

    if 'thread_id' in request.form:
        thread_id = request.form['thread_id']
    else:
        thread_id = helpers.create_a_thread()
    print('thread_id', thread_id)



    run_id = helpers.send_message(question, thread_id)
    return {'status': 'success', 'run_id': run_id, 'thread_id': thread_id}


@app.route('/checkRun',  methods=['GET'])
def checkRunStatus():
    run_id = request.args.get('run_id')
    thread_id = request.args.get('thread_id')
    print('run_id', run_id)
    print('thread_id', thread_id)
    run_status = helpers.check_run(run_id, thread_id)
    return {'status': 'success', 'run_id': run_id, 'thread_id': thread_id, 'run_status': run_status}

