from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("hello")
    return {"message": "Hello World"}