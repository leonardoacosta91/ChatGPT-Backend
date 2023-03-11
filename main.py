from fastapi import FastAPI
from src.chatgpt import ChatGPT
from src.model.chatgptmodel import ChatGPTMessegeIn, ChatGPTMessageOut

app = FastAPI()


@app.get("/")
def root():
    return {"hello world"}


@app.post("/chatgpt", response_model=ChatGPTMessageOut)
def send_message(message: ChatGPTMessegeIn):
    chatgpt = ChatGPT()
    response = chatgpt.send_message(message.message)
    return response
