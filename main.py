from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def sample_server():
    return {"message": "world"}
