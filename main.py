from fastapi import FastAPI
app = FastAPI()
@app.get("/welcome")
async def hi():
    return {"message": "Hello World"}