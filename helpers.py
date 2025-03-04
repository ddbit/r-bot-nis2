# This file is used to interact with the OpenAI API
import json
import openai

from openai import OpenAI


with open('openai_key') as f:
    api_key = f.readline()


client = OpenAI(api_key=api_key)

def create_a_thread():
  thread = client.beta.threads.create()
  return thread.id

def check_access_code(code):
  print('code', code)
  return True
  

ASSISTANT = 'asst_SPXdcZNDwKVfiPX9IGYXe9VD'
print('server init', ASSISTANT)

def send_message(message, thread_id):  
  if thread_id == '' or thread_id is None: 
    thread_id = create_a_thread()
    
  client.beta.threads.messages.create(
      thread_id=thread_id,
      role="user",
      content=message,
  )
  run = client.beta.threads.runs.create(
      thread_id=thread_id,
      assistant_id=ASSISTANT,
  )

  return run.id
  
def check_run(run_id, thread_id):
    
  print('server run',run_id)
  run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id,
  )
  print('server run status',run.status)
  return run.status


def get_messages(run_id, thread_id):
    
  print('server get messages', thread_id)
  messages = client.beta.threads.messages.list(thread_id=thread_id)
  for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")

  response = [ (m.role , m.content[0].text.value) for m in messages]
  return response