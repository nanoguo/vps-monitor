from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_root():
    return "pong"


@app.get("/tencent/check")
def check_tencent_sign(signature: str, echostr: int, timestamp: int, nonce: int):
    print(signature, echostr, timestamp, nonce)
    return echostr
