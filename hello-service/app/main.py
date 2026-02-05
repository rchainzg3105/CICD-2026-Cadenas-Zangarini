from fastapi import FastAPI

app = FastAPI(title="Hello Service")


@app.get("/hello")
def hello():
    return {"message": "42"}
