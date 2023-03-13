from fastapi import FastAPI, Depends
from src.chatgpt import ChatGPT
from src.model.chatgptmodel import ChatGPTMessegeIn, ChatGPTMessageOut
from src.model.loginmodel import Login
from src.jwt_handler import signJWT
from src.jwt_bearer import JWTBearer

app = FastAPI()


@app.get("/")
def root():
    return {"hello world"}


@app.post(
    "/chatgpt", response_model=ChatGPTMessageOut, dependencies=[Depends(JWTBearer())]
)
def send_message(message: ChatGPTMessegeIn):
    chatgpt = ChatGPT()
    response = chatgpt.send_message(message.message)
    return response


@app.post("/login")
def user_login(user: Login):
    if user.user == "Leo" and user.passwd == "password123":
        return signJWT(user.user)
    return {"error": "Wrong login details!"}
